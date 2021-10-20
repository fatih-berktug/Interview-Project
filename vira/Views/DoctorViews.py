from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render

from vira.Form.PatiendForm import PatiendForm
from vira.Model.Patient import Patient

@login_required
def view_doctor(request):
    patiend_form=PatiendForm()
    if request.method == "POST" and request.is_ajax():
        if request.POST.get("custId"):
            patiend=Patient.objects.get(pk=request.POST.get('custId'))
            patiend_form = PatiendForm(request.POST or None,instance=patiend)
        else:
            patiend_form = PatiendForm(request.POST)
        patiend=patiend_form.save(request,commit=False)
        patiend.save()
        return JsonResponse({'status': 'Success', 'messages': 'save successfully',"count":Patient.objects.count(),"pk":patiend.pk})
    patinets=Patient.objects.all()
    return render(request, 'Doctor/view_doctor.html',{
        'patinets':patinets,
        'patiend_form':patiend_form
    })




@login_required
def delete_patient(request):

    try:
        with transaction.atomic():
            if request.method == 'POST' and request.is_ajax():
                pk = request.POST['pk']
                patient=Patient.objects.get(pk=pk)
                patient.delete()
                return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
            else:
                return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})
    except Exception as e:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


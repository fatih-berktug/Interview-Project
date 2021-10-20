from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from vira.Form.PatiendForm import PatiendForm
from vira.Model.Patient import Patient


@login_required
def view_doctor(request):
    patiend_form=PatiendForm()
    if request.method == "POST" and request.is_ajax() :
        patiend_form = PatiendForm(request.POST)
        patiend_form.save(request)
        return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
    patinets=Patient.objects.all()
    return render(request, 'Doctor/view_doctor.html',{
        'patinets':patinets,
        'patiend_form':patiend_form
    })
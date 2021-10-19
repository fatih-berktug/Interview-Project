
from django.shortcuts import render
def view_doctor(request):

    return render(request, 'Doctor/view_doctor.html')
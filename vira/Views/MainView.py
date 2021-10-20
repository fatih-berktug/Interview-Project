from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def view_main(request):

    return render(request, 'Main/main.html')
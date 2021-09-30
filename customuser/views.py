from django.shortcuts import render
from customuser.models import customUser
# Create your views here.

def home(request):
    context = {
        'customUsers': customUser.objects.all()
    }
    #Other Method
    # customUsers = customUser.objects.all()
    # user_data = { 'customUsers': customUsers }
    #return render (request,"customuser/home.html",context=user_data)
    return render (request,"customuser/home.html",context)
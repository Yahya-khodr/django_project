
import json
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render 
from customuser.models import customUser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

newUser= {
    'firstName' :'Yahya'
    ,'lastName':'khodr'
    ,'email':'yahya@gmail.com',},


def home(request):
    context = {
        'customUsers': customUser.objects.all()
    }
    return render (request,"customuser/home.html",context)
    #Other Method
        # customUsers = customUser.objects.all()
        # user_data = { 'customUsers': customUsers }
        #return render (request,"customuser/home.html",context=user_data)

def index(request):
    name = request.GET["name"]
    return HttpResponse(f"Hello {name}")

@csrf_exempt
def user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        fname=data['firstName']
        lname=data['lastName']
        email=data['email']
        customuser = customUser(firstName=fname,lastName=lname,email=email)
        customuser.save()
        context = {"customuser": customuser.serialize()}
    else:
        if request.GET.get("uid") is not None:
            uid=request.GET["uid"]
            context= {
                "customuser":customUser.objects.get(id=uid).serialize()
            }
        else: context = {
            "customUsers": list(customUser.objects.all().values("id","firstName","lastName","email"),)
            }
    return JsonResponse(context)


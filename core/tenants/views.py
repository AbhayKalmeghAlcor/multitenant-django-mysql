from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import random
from django.db import connection


#
# # Create your views here.
# def getUserProfile(request):
#     print(request.tenant)
#     User.objects.create_user(username=request.tenant, email="robin.malik@alcortech.com", password="Abhay@786")
#     User.objects.filter(username=random.randint(2000, 10000),email="robin.malik@alcortech.com", password="Abhay@786")
#     return HttpResponse("Hello")


def getUserProfile(request):
    print(request.tenant)
    print(connection.settings_dict)
    User.objects.create_user(username=random.randint(2000, 10000),
                             email=f"robin.malik{random.randint(2000, 10000)}@alcortech.com", password="Abhay@786")

    return HttpResponse("This is Testing Mode")

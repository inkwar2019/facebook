from django.shortcuts import render
from django.http import JsonResponse
from .models import MyUser
import json


# Create your views here.
def first(request):
    return JsonResponse({"name": "Sozib", "roll": 1603039})


def second(request):
    return JsonResponse({"name": "Sabdul", "roll": 1603050})


def create_user(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        obj = MyUser(first_name=body["first_name"],
                     last_name=body["last_name"],
                     username=body["username"],
                     password=body["password"])
        obj.save()
        return JsonResponse({"status": 400, "ID": obj.ID})
    else:
        return JsonResponse({"status": 400, "Error": "This is post method, get method not supported."})

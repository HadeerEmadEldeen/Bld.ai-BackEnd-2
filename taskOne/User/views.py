from urllib import response
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import status
from rest_framework.response import Response
import json , uuid , os
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django import forms
from .models import User
from .forms import BookForm

class SingleUser(View):
    #GET
    def get(self, request, *args, **kwargs):
        userId = kwargs["id"]
        todos = User.objects.filter(id = userId)
        return HttpResponse(todos)

    #Update
    def put(self, request, *args, **kwargs):
        userId = kwargs["id"]
        data = request.body
        body = json.loads(data)
        User.objects.filter(id = userId).update(first_name = body["first_name"],last_name = body["last_name"], birth_date = body["birth_date"],email = body["email"],password = body["password"] )
        return HttpResponse("Data Update", status=status.HTTP_202_ACCEPTED)

    #Create
    def post(self, request, *args, **kwargs):
        data = request.body
        body = json.loads(data)
        first_name = body["first_name"]
        last_name = body["last_name"]
        birth_date = body["birth_date"]
        email = body["email"]
        password = body["password"]
        bodyValidation = BookForm({"first_name" : first_name ,"last_name" : last_name ,"birth_date" : birth_date , "email" : email , "password" : password })
        if bodyValidation.is_valid():
            user= User(first_name = body["first_name"],last_name = body["last_name"], birth_date = body["birth_date"],email = body["email"],password = body["password"] )
            user.save()
            return HttpResponse("Data Created", status=status.HTTP_201_CREATED)
        return HttpResponse("Data NOT Created", status=status.HTTP_406_NOT_ACCEPTABLE)

        

    #Delete
    def delete(self, request, *args, **kwargs):
        userId = kwargs["id"]
        deletebook =  get_object_or_404(User,id=userId)
        deletebook.delete()
        return HttpResponse("Data Deleted", status=status.HTTP_200_OK)



class Users(View):
    def get(self, request, *args, **kwargs):
        todos = User.objects.all()
        return HttpResponse(todos)


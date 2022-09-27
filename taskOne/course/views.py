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
from .models import *
from .forms import *

class oneCourse(View):
    #GET
    def get(self, request, *args, **kwargs):
        userId = kwargs["id"]
        todos = Course.objects.filter(id = userId)
        return HttpResponse(todos)

    #Update
    def put(self, request, *args, **kwargs):
        userId = kwargs["id"]
        data = request.body
        body = json.loads(data)
        Course.objects.filter(id = userId).update(name = body["name"],description = body["description"],tital = body["tital"] )
        return HttpResponse("Data Update", status=status.HTTP_202_ACCEPTED)

    #Create
    def post(self, request, *args, **kwargs):
        data = request.body
        body = json.loads(data)

        name = body['name']
        description = body['description']
        nametCheck = nameValidation({"name": name})
        discraptionCheck = descriptionValidation({"description": description})

        if nametCheck.is_valid() and discraptionCheck.is_valid():
            user= Course(name = body["name"],description = body["description"],tital = body["tital"])
            user.save()
            return HttpResponse("Data Created", status=status.HTTP_201_CREATED)
        return HttpResponse("Data NOT Created", status=status.HTTP_406_NOT_ACCEPTABLE)

        

    #Delete
    def delete(self, request, *args, **kwargs):
        userId = kwargs["id"]
        deletebook =  get_object_or_404(Course,id=userId)
        deletebook.delete()
        return HttpResponse("Data Deleted", status=status.HTTP_200_OK)



class Courses(View):
    def get(self, request, *args, **kwargs):
        todos = Course.objects.all()
        return HttpResponse(todos)


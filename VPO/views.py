from django.shortcuts import render
from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.renderers import JSONRenderer

from .models import User
from .models import User_organizer
from .models import User_member
from .models import Organizer_project
from rest_framework.views import Response
from rest_framework.views import APIView
import json
from .serializer import UserSerializer


# Create your views here.


class VpoAPIView(APIView):
    def get(self, request):
        return Response({'title': 'KDKDKKD'})

    def post(self, request):
        post_new = User.objects.create(

            name=request.data['name']
        )

        return Response({'post': model_to_dict(post_new)})


class Register_organizer(APIView):
    def get(self, request):
        return Response({'title': 'KDKDKKD'})

    def post(self, request):
        post_new = User_organizer.objects.create(
            email=request.data['email'],
            password=request.data['password']
        )

        return Response({'post': model_to_dict(post_new), 'type': 'organizer'})


class Register_member(APIView):
    def get(self, request):
        return Response({'post': "skskksk"})

    def post(self, request):
        post_new = User_member.objects.create(
            email=request.data['email'],
            password=request.data['password']
        )

        return Response({'post': model_to_dict(post_new), 'type': 'member'})


class Sing(APIView):


    def get(self, request):
        print(request.data['email']);
        print(request.data['password']);
        try:
            obj = User_member.objects.get(email=request.data['email'], password=request.data['password'])

            return Response({'post': "1"})

        except:
            return Response({'post': "2"})


    def post(self, request):
        print(request.data['email']);
        print(request.data['password']);
        try:
            obj = User_member.objects.get(email=request.data['email'], password=request.data['password'])
            print(obj)
            return Response({'post': "1"})

        except:
            return Response({'post': "2"})



class Project(APIView):
    def post(self, request):
        post_new = Organizer_project.objects.create(
            id_organizer=request.data['id_organizer'],
            json=request.data['json_data'],
        )

        return Response({'post': model_to_dict(post_new), 'type': 'member'})
    # def post(self, request):
    #     post_new = User_member.objects.create(
    #         email=request.data['id_organizer'],
    #         password=request.data['json_data']
    #     )
    #
    #     return Response({'post': model_to_dict(post_new), 'type': 'member'})

# class VpoAPIView(generics.ListAPIView):
#     # print("sasdadsasds")
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

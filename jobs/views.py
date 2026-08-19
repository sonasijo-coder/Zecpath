from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Job, Application
from .serializers import JobSerializer

from accounts.models import Employer

# Create your views here.

# 1. ListApi

class JobListAPIView(APIView):

  def get(self,request):
    jobs = Job.objects.all().order_by('created_at')
    serializer = JobSerializer(jobs , many=True)
    return Response(serializer.data , status=status.HTTP_200_OK)

# 2. CreateApi - Day 5

#class JobCreateAPIView(APIView):

  #def post(self,request):
    #serializer = JobSerializer(data = request.data)
    #if serializer.is_valid():
      # posted_by is a required FK to User - assign logged-in user
      #serializer.save(posted_by=request.user)
      #return Response(serializer.data , status=status.HTTP_201_CREATED)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#. Create Api - Day 6

class JobCreateAPIView(APIView):

   def post(self,request):
     try:
       employer = Employer.objects.get(user=request.user)
     except Employer.DoesNotExist:
       return Response({"error":"Logged-in user is not an employer"}, status=status.HTTP_400_BAD_REQUEST)

     serializer = JobSerializer(data = request.data)
     if serializer.is_valid():
       serializer.save(posted_by = employer)
       return Response(serializer.data , status=status.HTTP_201_CREATED)
     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# 3 .TestApiView

class UserTestAPIView(APIView):

  def get(self, request):
    return Response( 
      {"message": "DRF setup working correctly!", "Status" : "Success"},
      status=status.HTTP_200_OK
      )

  def post(self,request):
    name = request.data.get("name", "Guest")
    return Response(
      {"message":f"Hello , {name}!", "received_data":request.data},
      status=status.HTTP_200_OK
    )


from django.http import JsonResponse
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def doctor_list(request, format=None):

  #get all doctors
  #serializer them
  #return json

  if request.method == 'GET':
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

    # if you want to return just json data and not the html page with json use the code below in the place of Response()
    # return JsonResponse(serializer.data, safe=False)

  if request.method == 'POST':
    serializer = DoctorSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def doctor_detail(request, id, format=None):

  try:
    doctor = Doctor.objects.get(pk=id)
  except Doctor.DoesNotExist:
    return Response(status = status.HTTP_201_CREATED)

  if request.method == 'GET':
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = DoctorSerializer(doctor, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    doctor.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)


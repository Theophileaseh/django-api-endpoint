from django.http import JsonResponse
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def doctor_list(request):

  #get all doctors
  #serializer them
  #return json

  if request.method == 'GET':
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return JsonResponse(serializer.data, safe=False)

  if request.method == 'POST':
    serializer = DoctorSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)
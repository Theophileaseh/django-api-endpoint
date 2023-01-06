from django.http import JsonResponse
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.decorators import api_view

@api_view('GET', 'POST')
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
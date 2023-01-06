from django.http import JsonResponse
from .models import Doctor
from .serializers import DoctorSerializer

def doctor_list(request):

  #get all drinks
  #serializer them
  #return json

  doctors = Doctor.objects.all()
  serializer = DoctorSerializer(drinks, many=True)
  return JsonResponse(serializer.data)
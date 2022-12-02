from rest_framework.views import APIView, Response, Request, status
from .models import Pet
from .serializers import PetSerializer
from django.shortcuts import get_object_or_404
import ipdb


class PetsView(APIView):
    def get(self, request):
        pet = Pet.objects.all()
        pet_serializer = PetSerializer(pet, many=True)


        return Response(pet_serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = PetSerializer(data= request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class PetsDetailsView(APIView):

    def get(self, request, pet_id):
        pet= get_object_or_404(Pet, id = pet_id)
        serializer = PetSerializer(pet)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pet_id):
        pet= get_object_or_404(Pet, id = pet_id)

        serializer = PetSerializer(pet, request.data, partial=True)
        
        serializer.is_valid(raise_exception=True)

        serializer.save()
        
        return Response(serializer.data, status.HTTP_200_OK)

        
    def delete(self, request, pet_id):
        pet= get_object_or_404(Pet, id = pet_id)

        pet.delete()

        return Response(status= status.HTTP_204_NO_CONTENT)

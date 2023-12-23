from django.shortcuts import render
from .serializers import InscritoSerial
from .models import Inscrito
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class inscrito_list_class(APIView):
    def get(self, request):
        inscrito = Inscrito.objects.all()
        serial = InscritoSerial(inscrito, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = InscritoSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class inscrito_detalle_class(APIView):
    def get_object(self, id):
        try:
            return Inscrito.objects.get(pk=id)
        except Inscrito.DoesNotExist:
            return Http404
    
    def get(self, id):
        inscrito = self.get_object(id)
        serial = InscritoSerial(inscrito)
        return Response(serial.data)
    
    def put(self, request, id):
        inscrito = self.get_object(id)
        serial = InscritoSerial(inscrito, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, id):
        inscrito = self.get_object(id)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def inscrito_list(request):
    if request.method == 'GET':
        inscrito = Inscrito.objects.all()
        serial = InscritoSerial(inscrito, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InscritoSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def inscrito_list(request):
    if request.method == 'GET':
        inscrito = Inscrito.objects.all()
        serial = InscritoSerial(inscrito, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InscritoSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def inscrito_detalle(request, id):
    try:
        inscrito = Inscrito.objects.get(pk=id)
    except Inscrito.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InscritoSerial(inscrito)
        return Response(serial.data)
        
    if request.method == 'PUT':
        serial = InscritoSerial(inscrito, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
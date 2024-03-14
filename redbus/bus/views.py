from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import bus_details
from .serializers import busdetailsser
# Create your views here.
class bus(APIView):
    def get(self,r):
        busdetails = bus_details.objects.all()
        serobj = busdetailsser(busdetails,many =True)
        return Response(serobj.data)

    def post(self,r):
        serobj = busdetailsser(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)

        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class busUpdateDelete(APIView):
    def put(self,r,pk):
        busobj = bus_details.objects.get(pk=pk)
        serobj = busdetailsser(busobj,data = r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)

        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)



        return Response(busobj)

    def delete(self,r,pk):
        busobj = bus_details.objects.get(pk=pk)
        busobj.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

from django.shortcuts import render

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from app.models import Course
from app.serializers import CourseSerializer
from app import serializers

# Create your views here.


class CreateCourse(APIView):
    def post(self,request):
        data=request.data
        serializer_instance=CourseSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



class ListCourse(APIView):
    def get(self,request):
        e=Course.objects.all()
        serializer_instance=CourseSerializer(e,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


class UpdateCourse(APIView):
    def put(self,request,id):
        data=request.data
        e=get_object_or_404(Course,id=id)
        serializer_instance=CourseSerializer(instance=e,data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



class PartialUpdateCourse(APIView):
    def put(self,request,id):
        data=request.data
        e=get_object_or_404(Course,id=id)
        serializer_instance=CourseSerializer(instance=e,data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



class DeleteCourse(APIView):
    def delete(self,request,id):
        e = get_object_or_404(Course, id=id)
        serializer_instance = CourseSerializer(instance=e)
        if serializer_instance.is_valid():
            e.delete()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)



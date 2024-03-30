from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def movies(request):

    if request.method == 'POST':
        serialized = MovieSerializer(movies, data=request.data)
        if serialized.is_valid():
            serialized.saved()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
        # return JsonResponse({'movies':serializer.data}, )
    
@api_view(['GET', 'PUT', 'DELETE'])
def movie(request, did):
    movie = get_object_or_404(Movie, id=did)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serialized = MovieSerializer(movies, data=request.data)
        if serialized.is_valid():
            serialized.saved()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
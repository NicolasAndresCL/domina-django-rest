from drf_yasg.utils import swagger_auto_schema

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from movie.models import Movie
from movie.serializers import MovieSerializer, MovieModelSerializer


class MovieAPIView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieModelSerializer(movies, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(request_body=MovieModelSerializer)
    def post(self, request):
        serializer = MovieModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    @swagger_auto_schema(request_body=MovieSerializer)
    def put(self, request, pk=None):
        try:
            movie = Movie.objects.get(id=pk)
        except:
            Response("Not found", status=404)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


# @swagger_auto_schema(method="POST", request_body=MovieModelSerializer)
# @api_view(["GET", "POST"])
# def get_movies(request):

#     if request.method == "GET":

#         movies = Movie.objects.all()
#         serializer = MovieModelSerializer(movies, many=True)
#         return Response(serializer.data, status=200)

#     if request.method == "POST":

#         serializer = MovieModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)

#         return Response(serializer.errors, status=400)

#     return Response("Method not allowed", status=405)


# @swagger_auto_schema(method="PUT", request_body=MovieSerializer)
# @api_view(["PUT"])
# def put_movies(request, pk):
#     try:
#         movie = Movie.objects.get(id=pk)
#     except:
#         Response("Not found", status=404)

#     serializer = MovieSerializer(movie, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=200)
#     return Response(serializer.errors, status=400)

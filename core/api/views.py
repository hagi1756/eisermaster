from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import BlogSerializer
from  core.models import Blog

class BlogListAPIView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    # def get_queryset(self):
    #     return super().get_queryset()


class BlogDetailAPIView(RetrieveAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field ='id'


class BlogCreateAPIView(CreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field ='id'


class BlogDeleteAPIView(DestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field ='id'


class GeneralView(APIView):
    def get(self,request, *args, **kwargs):
        return Response({'message':'Hello World'})
    def post(self,request, *args, **kwargs):
        return Response({'message':'Hello World'})
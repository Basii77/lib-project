from django.shortcuts import render
from book.models import Books
from rest_framework.decorators import api_view
from book.serializers import bookserializer,userserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny



# -------------------------------------------------------------------------
# mixins views

# class booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Books.objects.all()
#     serializer_class=bookserializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#
# class bookdetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Books.objects.all()
#     serializer_class=bookserializer
#     def get(self,request,pk):
#         return self.retrieve(request)
#     def put(self,request,pk):
#         return self.update(request)
#     def delete(self,request,pk):
#         return self.destroy(request)


# ----------------------------------------------------------------------

# Generics class view

# class booklist(generics.ListCreateAPIView): # non primary key
#     queryset=Books.objects.all()
#     serializer_class=bookserializer
#
#
# class bookdetails(generics.RetrieveUpdateDestroyAPIView): # primary key based
#     queryset=Books.objects.all()
#     serializer_class=bookserializer

# ---------------------------------------------------------------------

# view set based

class bookviewset(viewsets.ModelViewSet): # primary key based & non primary key based will work
    queryset=Books.objects.all()
    serializer_class=bookserializer

class registerviewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = User.objects.all()
    serializer_class = userserializer









# ------------------------------------------------------------------------

# Create your views here. function based


# @api_view(['GET','POST'])
# def Booklist(request):
#     if(request.method=="GET"):
#         book=Books.objects.all()
#         b=bookserializer(book,many=True)
#         return Response(b.data)
#     elif(request.method=="POST"):
#         b=bookserializer(data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data,status=status.HTTP_201_CREATED)
#
#     return Response(b.error,status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def book_details(request,pk):
#     try:
#         book=Books.objects.get(pk=pk)
#
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if(request.method=="GET"):
#         b=bookserializer(book)
#         return Response(b.data)
#     elif(request.method=="PUT"):
#         b=bookserializer(book,data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data,status=status.HTTP_201_CREATED)
#         return Response(b.error,status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=="DELETE"):
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

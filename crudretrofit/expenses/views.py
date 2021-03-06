from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer

# Create your views here.

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#    permission_classes = (IsAuthenticated,)

#    def get(self, request, format=None):
#        categories = [category.name for category in Category.objects.all()]
#        print('Usuário do token:', request.data)
#        print('Usuário do token (request.user):', request.user)
#        return Response(categories)
    
#    def post(self, request, format=None):
#        serializer = CategorySerializer(data=request.data)
#        if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data, status=201)
#        return Response(serializer.errors, status=400)

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

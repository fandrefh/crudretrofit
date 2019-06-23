"""crudretrofit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from crudretrofit.expenses import views

from rest_framework_simplejwt import views as views_simplejwt

urlpatterns = [
    path('api/v1/categories/', views.CategoryListCreateView.as_view(), name='categories'),
    path('api/v1/categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='categories_update'),
    path('api/v1/expenses/', views.ExpenseListCreateView.as_view(), name='expenses'),
    path('api/v1/expenses/<int:pk>/', views.ExpenseRetrieveUpdateDestroyView.as_view(), name='expenses_update'),
    path('api/v1/token/', views_simplejwt.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', views_simplejwt.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', views_simplejwt.TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
]

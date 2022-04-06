from django.urls import path
from .import views

app_name = 'calculators'

urlpatterns = [
    path('', views.calculators_list, name = 'list'),
    path('<slug:slug>/', views.calculator_detail, name = "detail"),

]

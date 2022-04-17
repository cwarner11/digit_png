from django.urls import path
from .import views

app_name = 'pages'

urlpatterns = [
    path('', views.pages_list, name = 'list'),
    path('<slug:slug>/', views.pages_detail, name = "detail"),

]

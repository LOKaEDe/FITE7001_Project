from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('prices/', views.prices, name="prices"),
   path('score/', views.Ex_score, name="score"),
   path('report/', views.report, name="report"),
]

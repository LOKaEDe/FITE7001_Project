from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('prices/', views.prices, name="prices"),
   path('score/', views.Ex_score, name="score"),
   path('report/', views.report, name="report"),
   path('exchanges/', views.exchanges, name="exchanges"),
   path('exchanges/<str:exchange_name>', views.exchanges_detail, name="detail"),
   path('email-post/', views.email_post, name="email-post"),
]

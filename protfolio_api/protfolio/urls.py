from django.urls import path
from .views import getUser

urlpatterns = [
    path('protfolio/<str:email>', getUser)
]

from django.urls import path
from . import views


urlpatterns = [
    path("<int:month>", views.monthly_challengeN),
    path("<str:month>", views.monthly_challenge),
]

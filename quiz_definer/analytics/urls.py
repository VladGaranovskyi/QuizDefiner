from django.urls import path
from .views import quiz_analytics

urlpatterns = [
    path('quiz/<str:caption>', quiz_analytics, name="quiz_analytics")
]

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from quizapp.models import Quiz

# quick main page view through lambda function
main_page_view = lambda request: render(request, "main.html", {"quizes": Quiz.objects.all()})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("authapp.urls")),
    path('', main_page_view),
    path('search/', include("search.urls")),
    path('quiz/', include("quizapp.urls")),
    path('analytics/', include("analytics.urls")),
]

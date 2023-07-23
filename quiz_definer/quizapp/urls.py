from .views import CreateQuizView, PassQuizView, QuizResultView, QuizApiView
from django.urls import path

urlpatterns = [
    path('create/', CreateQuizView.as_view(), name="create_quiz"),
    path('page/<str:quiz_caption>', PassQuizView.as_view()),
    path('page/<str:quiz_caption>/<int:result>', QuizResultView.as_view()),
    path('api/', QuizApiView.as_view())
]
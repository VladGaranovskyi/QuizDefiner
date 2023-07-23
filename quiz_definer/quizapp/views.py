from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Quiz
from .managers import QuizManager
from django.utils.html import json_script
from analytics import db_connect
from .serializers import QuizSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateQuizView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "quiz/create_quiz.html")

    def post(self, request):
        # check function needs to be added
        Quiz.objects.create_quiz(request)
        return redirect('/')


class PassQuizView(LoginRequiredMixin, View):
    def get(self, request, quiz_caption):

        # getting object from db
        quiz = Quiz.objects.only("caption", "questions", "result_ranges").get(caption=quiz_caption)

        # receiving models of questions from many to many field
        questions_model = quiz.questions.all()

        # converting to dict
        questions = QuizManager.questions_to_dict(questions_model)
        return render(request, "quiz/quiz_page.html", {"questions": json_script(questions), "caption": quiz.caption})


class QuizResultView(LoginRequiredMixin, View):
    def get(self, request, quiz_caption, result):

        result = int(result)

        # analytics data insertion in MongoDB
        db_connect.insert_dict({"caption": quiz_caption, "result": result})

        # getting quiz object from db
        quiz = Quiz.objects.get(caption=quiz_caption)

        # generating message of the result
        msg = QuizManager.get_result_message(quiz, result)
        return render(request, "quiz/quiz_result.html", {"msg": msg, "quiz": quiz})


class QuizApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        quizes = Quiz.objects.all()
        quiz_serializer = QuizSerializer(quizes, many=True)
        return Response(quiz_serializer.data)





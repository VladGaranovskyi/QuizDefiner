from rest_framework import serializers
from .models import Quiz
from authapp.serializers import UserSerializer


class QuizSerializer(serializers.ModelSerializer):

    # making author serializer to show only his nickname, without password hash and email
    author = UserSerializer()

    class Meta:
        model = Quiz
        depth = 1
        fields = ['caption', 'genre', 'questions', 'author', 'result_ranges']

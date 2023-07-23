from django.db import models
from authapp.models import User
from json import dumps
from .managers import QuizManager


class Question(models.Model):
    question = models.CharField(max_length=150)
    answers = models.TextField(max_length=700)


class ResultRange(models.Model):
    left = models.IntegerField()
    right = models.IntegerField()
    message = models.CharField(max_length=200)


class Quiz(models.Model):
    caption = models.CharField(max_length=70, unique=True, primary_key=True, default="")
    genre = models.CharField(max_length=30, default="General")
    questions = models.ManyToManyField(Question, blank=True, default=None, db_constraint=False)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    result_ranges = models.ManyToManyField(ResultRange, blank=True, default=None, db_constraint=False)

    objects = QuizManager()

    def __str__(self):
        return self.caption

    class Meta:
        indexes = [models.Index(fields=["caption", "genre"])]



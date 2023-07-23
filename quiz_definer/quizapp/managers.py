from django.db import models
from json import dumps, loads
from django.apps import apps


class QuizManager(models.Manager):
    """
    this class can create quiz object from request
    can define result message and prevent wrong results
    can convert question object to dict
    """
    @staticmethod
    def get_result_message(quiz, coefficient):
        ranges = quiz.result_ranges.all()

        # going through ranges and finding the right one with the simple linear search
        for r in ranges:
            if coefficient >= r.left and coefficient <= r.right:
                return r.message

        # if found nothing, getting max and min of ranges and calling recursive function
        max_border = max(tuple(r.right for r in ranges))
        min_border = min(tuple(r.left for r in ranges))
        return QuizManager.get_result_message(quiz, max_border if coefficient > max_border else min_border)


    @staticmethod
    def questions_to_dict(questions):
        return [{"question": question.question, "answers": loads(question.answers)} for question in questions]

    def create_quiz(self, request):

        count_of_questions = int(request.POST["qCount"])
        count_of_ranges = int(request.POST["rCount"])

        questions = []
        ranges = []

        """
        structure of request.POST:
            q(n) : ''
            q(n)a(k)Text: '', q(n)a(k)Value: ''
            
            n is in [1, +infinity)
            k is in [1, 4]
        """
        for i in range(1, count_of_questions + 1):
            questions.append(apps.get_model(app_label="quizapp", model_name="Question")(
                question=request.POST[f"q{i}"],
                answers=dumps([
                    {"text": request.POST[f"q{i}a1Text"], "value": int(request.POST[f"q{i}a1Value"])},
                    {"text": request.POST[f"q{i}a2Text"], "value": int(request.POST[f"q{i}a2Value"])},
                    {"text": request.POST[f"q{i}a3Text"], "value": int(request.POST[f"q{i}a3Value"])},
                    {"text": request.POST[f"q{i}a4Text"], "value": int(request.POST[f"q{i}a4Value"])},
                ])
            ))

        for i in range(1, count_of_ranges + 1):
            ranges.append(apps.get_model(app_label="quizapp", model_name="ResultRange")(
                left=int(request.POST[f"left{i}"]),
                right=int(request.POST[f"right{i}"]),
                message=request.POST[f"message{i}"]
            ))

        # creating instance
        quiz = self.model(author=request.user, caption=request.POST["caption"], genre=request.POST["genre"])

        # saving questions and result ranges
        for q in questions:
            q.save()
            quiz.questions.add(q)

        for r in ranges:
            r.save()
            quiz.result_ranges.add(r)

        # saving instance
        quiz.save()

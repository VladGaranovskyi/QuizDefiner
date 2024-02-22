from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Question, ResultRange, Quiz
from .managers import QuizManager
from django.http import HttpRequest
from unittest.mock import Mock

class QuizManagerTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        User = get_user_model()
        self.user = User.objects.create_user(nickname='test_user', email='test@example.com', password='password')

    def test_get_result_message(self):
        # Create some result ranges
        range1 = ResultRange.objects.create(left=0, right=10, message='Low')
        range2 = ResultRange.objects.create(left=11, right=20, message='Medium')
        range3 = ResultRange.objects.create(left=21, right=30, message='High')

        # Create a quiz with these ranges
        quiz = Quiz.objects.create(caption='Test Quiz', author=self.user)
        quiz.result_ranges.add(range1, range2, range3)

        # Test for coefficient within the first range
        self.assertEqual(QuizManager.get_result_message(quiz, 5), 'Low')

        # Test for coefficient within the second range
        self.assertEqual(QuizManager.get_result_message(quiz, 15), 'Medium')

        # Test for coefficient within the third range
        self.assertEqual(QuizManager.get_result_message(quiz, 25), 'High')

        # Test for coefficient below the minimum range
        self.assertEqual(QuizManager.get_result_message(quiz, -5), 'Low')

        # Test for coefficient above the maximum range
        self.assertEqual(QuizManager.get_result_message(quiz, 35), 'High')

    def test_questions_to_dict(self):
        # Create some questions
        question1 = Question.objects.create(question='Question 1', answers='[{"text": "Answer 1", "value": 1}]')
        question2 = Question.objects.create(question='Question 2', answers='[{"text": "Answer 2", "value": 2}]')

        # Convert questions to dictionary
        questions_dict = QuizManager.questions_to_dict([question1, question2])

        # Test if questions are converted correctly
        self.assertEqual(questions_dict[0]['question'], 'Question 1')
        self.assertEqual(questions_dict[0]['answers'][0]['text'], 'Answer 1')
        self.assertEqual(questions_dict[0]['answers'][0]['value'], 1)
        self.assertEqual(questions_dict[1]['question'], 'Question 2')
        self.assertEqual(questions_dict[1]['answers'][0]['text'], 'Answer 2')
        self.assertEqual(questions_dict[1]['answers'][0]['value'], 2)

    def test_create_quiz(self):
        # Create a mock request object
        request = Mock(spec=HttpRequest)
        request.user = self.user
        request.POST = {
            'caption': 'Test Quiz',
            'genre': 'General',
            'qCount': '2',
            'rCount': '2',
            'q1': 'Question 1',
            'q1a1Text': 'Answer 1',
            'q1a1Value': '1',
            'q2': 'Question 2',
            'q2a1Text': 'Answer 2',
            'q2a1Value': '2',
            'left1': '0',
            'right1': '10',
            'message1': 'Low',
            'left2': '11',
            'right2': '20',
            'message2': 'Medium',
        }

        # Create a quiz using the manager method
        Quiz.objects.create_quiz(request)

        # Test if the quiz is created
        self.assertEqual(Quiz.objects.count(), 1)
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(ResultRange.objects.count(), 2)

        # Test if the quiz is associated with the correct user
        quiz = Quiz.objects.first()
        self.assertEqual(quiz.author, self.user)

        # Test if the questions and result ranges are associated with the quiz
        self.assertEqual(list(quiz.questions.values_list('question', flat=True)), ['Question 1', 'Question 2'])
        self.assertEqual(list(quiz.result_ranges.values_list('message', flat=True)), ['Low', 'Medium'])

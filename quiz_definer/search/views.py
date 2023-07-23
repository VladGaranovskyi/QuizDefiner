from django.shortcuts import render
from quizapp.documents import QuizDocument
from quizapp.models import Quiz


def search(request):

    if request.method == "POST":
        quizes = None

        # getting post data
        genre = request.POST['genre']
        prompt = request.POST['prompt']

        # checking for prompt and genre if they are not none to avoid causing the error
        if genre and prompt:
            quizes = QuizDocument.search().query("term", caption=prompt).query("match", genre=genre)
        elif genre:
            quizes = QuizDocument.search().query("match", genre=genre)
        elif prompt:
            quizes = QuizDocument.search().query("term", caption=prompt)

        # creating list of quizes to help jinja parse it
        quizes_models = [Quiz.objects.get(caption=q.caption) for q in quizes]
        return render(request, "main.html", {"quizes": quizes_models, "prompt": prompt})

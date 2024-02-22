# from django_elasticsearch_dsl import Document
# from django_elasticsearch_dsl.registries import registry
# from .models import Quiz


# # creating document for elasctic search indexing
# @registry.register_document
# class QuizDocument(Document):
#     class Index:
#         name = 'quiz'
#         settings = {'number_of_shards': 1,
#                     'number_of_replicas': 1}

#     class Django:
#         model = Quiz

#         fields = [
#             'caption',
#             'genre'
#         ]

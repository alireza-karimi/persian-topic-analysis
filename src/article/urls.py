from django.urls import path
from .views import GetArticles, PredictArticles

urlpatterns = [
    path('', GetArticles.as_view()),
    path('predict/', PredictArticles.as_view())
]

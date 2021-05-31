from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from article.models import Article
from article.serializers import (
    ArticleSerializer,
    PredictTopicSerializer,
    PredictTopicResultSerializer
)
from article.paginations import ArticlesPagination
from django.conf import settings


class GetArticles(ListAPIView):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer
    pagination_class = ArticlesPagination


class PredictArticles(CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = PredictTopicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        category = str(settings.SVM_PREDICTOR.predict(text))
        Article.objects.create(
            text=text,
            category=category
        )
        return Response(PredictTopicResultSerializer({"category": category}).data)

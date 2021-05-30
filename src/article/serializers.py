from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class PredictTopicSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)


class PredictTopicResultSerializer(serializers.Serializer):
    category = serializers.CharField()

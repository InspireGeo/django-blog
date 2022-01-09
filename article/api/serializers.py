from rest_framework import serializers
from article.models import Article


#### STANDART SERIALIZER
class ArticleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author= serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()
    created_date= serializers.DateTimeField(read_only=True)
    

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

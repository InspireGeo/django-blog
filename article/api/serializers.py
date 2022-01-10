from rest_framework import serializers
from article.models import Article



from datetime import datetime
from datetime import date
from django.utils.timesince import timesince



class ArticleSerializer(serializers.ModelSerializer):

   # time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = '__all__'
        # fields = ['yazar', 'baslik', 'metin']
        # exclude = ['yazar', 'baslik', 'metin']
        read_only_fields = ['id']

   # def get_time_since_pub(self,object):
       # now = datetime.now()
       # pub_date = object.created_date
       # time_delta = timesince(pub_date, now)
       # return time_delta
       




'''



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

    def update(self, instance, validated_data):
        instance.author = validated_data.get('yazar', instance.author)
        instance.title = validated_data.get('baslik', instance.title)
        instance.content = validated_data.get('icerik', instance.content)
        #instance.metin = validated_data.get('metin', instance.metin)
        #instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.created_date = validated_data.get('yayımlanma_tarihi', instance.created_date)
        #instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.save()
        return instance

    def validate(self, data): # object level
        if data['title'] == data['content']:
            raise serializers.ValidationError('Baslik ve açıklama alanları aynı olamaz. Lütfen farklı bir açıklama giriniz.')
        return data

    #def validate_baslik(self, value):
       ## if len(value) < 20:
          #  raise serializers.ValidationError(f'Baslik alani minimum 20 karakter olmalı. siz {len(value)} karakter girdiniz.')
       # return value

'''
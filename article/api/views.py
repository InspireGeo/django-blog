from rest_framework import status
from rest_framework.response import Response 
# from rest_framework.decorators import api_view

from article.models import Article
from article.api.serializers import ArticleSerializer

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


""" 
class GazeteciListCreateAPIView(APIView):
    def get(self, request):
        yazarlar = Gazeteci.objects.all()
        serializer = GazeteciSerializer(yazarlar, many=True, context={'request': request}) 
        return Response(serializer.data)


    def post(self, request):
        serializer = GazeteciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 """


class ArticleListCreateAPIView(APIView):
    def get(self, request):
        articles= Article.objects.filter() 
        serializer =ArticleSerializer(articles, many=True) 
        return Response(serializer.data)


    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):

    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)
        return article_instance

    def get(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article) 
        return Response(serializer.data)       

    def put(self, request, pk):
        article= self.get_object(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

    def delete(self, request, pk):
        article = self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






'''from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from article.models import Article
from article.api.serializers import ArticleDefaultSerializer



@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_api_view(request, pk):
    try:
        article_instance = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(
            {
                'errors': {
                    'code': 404,
                    'message': f'Böyle bir id ({pk}) ile ilgili makale bulunamadı.'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = ArticleDefaultSerializer(article_instance) 
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = ArticleDefaultSerializer(article_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        article_instance.delete()
        return Response(
            {
                'işlem': {
                    'code': 204,
                    'message': f'({pk}) id numaralı makale silinmiştir.'
                }
            },
            status = status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'POST'])
def    article_list_create_api_view(request):
    
    if request.method == 'GET':
        articellar= Article.objects.filter() 
       
        serializer = ArticleDefaultSerializer(articellar, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleDefaultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)'''
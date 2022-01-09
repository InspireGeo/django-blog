
from django.urls import path
from article.api import views as api_views

urlpatterns = [
    path('articellar/',api_views.article_list_create_api_view, name='article-listesi'),
    path('articellar/<int:pk>', api_views.article_detail_api_view, name='article-detay'),
]

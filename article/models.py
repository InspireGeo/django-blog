from django.db import models
from django.db.models.base import Model

import article

# Create your models here.

class Article(models.Model):
    #author = models.CharField(max_length=50,verbose_name="Yazar")
    author= models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="yazar")

    title = models.CharField(max_length=50,verbose_name="baslik")
    content = models.TextField(verbose_name="icerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="oluşturma tarihi")
    article_image = models.FileField(blank=True,null=True,verbose_name="makaleye foto ekle")
    
    def __str__(self):
        return self.title
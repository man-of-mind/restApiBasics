from django.urls import path
import apibasics.views

urlpatterns = [
    path('articles/', apibasics.views.article_list, name="articles"),
    path('article/detail/<int:pk>', apibasics.views.article_detail, name="detail"),
]

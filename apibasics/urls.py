from django.urls import path
import apibasics.views

urlpatterns = [
#    path('articles/', apibasics.views.article_list, name="articles"),
#    path('article/detail/<int:pk>', apibasics.views.article_detail, name="detail"),
    path('articles/', apibasics.views.ArticleApiView.as_view(), name="articles"),
    path('details/<int:id>/', apibasics.views.ArticleDetails.as_view()),
    path('generic/article/', apibasics.views.GenericAPIView.as_view()),
]

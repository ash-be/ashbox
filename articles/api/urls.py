from django.urls import path
from articles.api import views

urlpatterns = [

    # GET, POST
    path('', views.articles, name='articles'),

    # GET, PATCH, DELETE
    path('<int:id>/', views.article_detail, name='article-detail'),

    # PATCH
    path('<int:id>/publish', views.publish_draft, name='publish-draft'),

]
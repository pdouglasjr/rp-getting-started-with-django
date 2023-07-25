from django.urls import path

from blog import views

urlpatterns = [
    path('', views.blog_index, name='blog')
    path('category/<str:category>', views.blog_category, name='blog_category')
]


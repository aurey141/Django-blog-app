from . import views
from django.urls import path

# URL pattern routing for project Blog
urlpatterns = [
  path('', views.PostList.as_view(), name="Home"),
  path('post/<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
]
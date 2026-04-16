from django.urls import path
from .views import PostListView, CategoryPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('category/<int:category_id>/', CategoryPostListView.as_view(), name='category-posts'),
]

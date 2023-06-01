from django.urls import path
from .views import PostCreateView, PostLikeView, PostUnLikeView, GetAllPosts, FilterLikesByDate

urlpatterns = [
    path('create', PostCreateView.as_view(), name='post_create'),
    path('like/<int:id>/', PostLikeView.as_view(), name='post_like'),
    path('unlike/<int:id>/', PostUnLikeView.as_view(), name='post_unlike'),
    path('all', GetAllPosts.as_view(), name='all_posts'),
    path('filter', FilterLikesByDate.as_view(), name='filter_like'),
]

from django.urls import path
from .views import (
    BlogPostListView, BlogPostUserListView, BlogPostDetailView,
    CommentListView, CommentUserListView, CommentDetailView,
    LikeListView, LikeCreateView, LikeDetailView,
    BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView,
    LikeDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('blogs/all/', BlogPostListView.as_view(), name='blogpost-list'),
    path('blogs/user/', BlogPostUserListView.as_view(), name='blogpost-user-list'),
    path('blogs/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('blogs/new/', BlogPostCreateView.as_view(), name='blogpost-create'),
    path('blogs/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost-update'),
    path('blogs/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost-delete'),
    path('blogs/<int:blogID>/comments/', CommentListView.as_view(), name='comment-list'),
    path('blogs/comments/user/', CommentUserListView.as_view(), name='comment-user-list'),
    path('blogs/<int:blogID>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('blogs/<int:blogID>/likes/<int:likeID>/delete/', LikeDeleteView.as_view(), name='like-delete'),
    path('blogs/<int:blogID>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('blogs/<int:blogID>/comments/<int:commentID>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('blogs/<int:blogID>/comments/<int:commentID>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('blogs/<int:blogID>/likes/', LikeListView.as_view(), name='like-list'),
    path('blogs/<int:blogID>/likes/new/', LikeCreateView.as_view(), name='like-create'),
    path('blogs/<int:blogID>/likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),
]

from rest_framework import generics, permissions
from .models import BlogPost, Comment, Like
from .serializers import BlogPostSerializer, CommentSerializer, LikeSerializer

class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-date')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BlogPost.objects.all().order_by('-date')

class BlogPostUserListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user).order_by('-date')

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogPostCreateView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostUpdateView(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)

class BlogPostDeleteView(generics.DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)

class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post__id=self.kwargs['blogID'])

class CommentUserListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(comment_author=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(comment_author=self.request.user)

class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(comment_author=self.request.user)

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(comment_author=self.request.user)

class LikeListView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(post__id=self.kwargs['blogID'])

class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        blog_post = BlogPost.objects.get(pk=self.kwargs['blogID'])
        serializer.save(user_giving=self.request.user, user_receiving=blog_post.author)

class LikeDetailView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(user_giving=self.request.user)

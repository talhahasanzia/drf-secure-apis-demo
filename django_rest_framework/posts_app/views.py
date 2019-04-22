# Create your views here.
import time

from rest_framework.views import APIView

from django_rest_framework.messages import success, failure, empty_success
from posts_app import models
from posts_app.models import Post
from posts_app.serializers import PostSerializer, CommentSerializer


class PostAPI(APIView):
    def get(self, request):
        user = self.request.user

        post_id = self.request.query_params.get('post_id', None)
        try:
            if post_id:
                post = Post.objects.get(pk=post_id)
                serialized = PostSerializer(post)
                return success(200, serialized.data)
            else:
                post = Post.objects.filter(author=user)
                serialized = PostSerializer(post, many=True)
                return success(200, serialized.data)
        except models.Post.DoesNotExist:
            return failure(403, "No post found ")

    def post(self, request):
        try:
            post = PostSerializer(data=request.data)
            if post.is_valid(raise_exception=True):
                post.save(author=self.request.user, created_at=time.time(), )
        except Exception as e:
            return failure(403, str(e))
        else:
            return empty_success(200)


class CommentCreateAPI(APIView):
    def post(self, request, post_id):
        comment = CommentSerializer(data=request.data)
        try:
            if comment.is_valid(raise_exception=True):
                post = Post.objects.get(pk=post_id)
                comment.save(post=post)

        except Exception as e:
            return failure(403, str(e))
        else:
            return empty_success(200)

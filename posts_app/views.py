# Create your views here.
import time

from rest_framework.views import APIView

from oauth_django.messages import success, failure, empty_success
from posts_app.models import Post
from posts_app.serializers import PostSerializer


class PostAPI(APIView):
    def get(self, request):
        user = self.request.user
        user_posts = Post.objects.filter(author=user)
        serialized = PostSerializer(user_posts, many=True)
        return success(200, serialized.data)

    def post(self, request):
        try:
            print(request.data)
            post = PostSerializer(data=request.data)
            if post.is_valid(raise_exception=True):
                post.save(author=self.request.user, created_at=time.time())
        except Exception as e:
            return failure(403, str(e))
        else:
            return empty_success(200)

from rest_framework import serializers

from posts_app.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    author = serializers.CharField(required=False)
    created_at = serializers.CharField(required=False)
    votes = serializers.IntegerField(required=False)

    class Meta:
        model = Post
        fields = ('title', 'description', 'author', 'created_at', 'votes')


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('comment_author', 'comment', 'post')

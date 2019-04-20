from rest_framework import serializers

from posts_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'author', 'created_at', 'votes',)

    title = serializers.CharField()
    description = serializers.CharField()
    author = serializers.CharField(required=False)
    created_at = serializers.CharField(required=False)
    votes = serializers.IntegerField(required=False)

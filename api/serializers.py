from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.EmailField()

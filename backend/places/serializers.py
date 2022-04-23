from rest_framework import serializers 
from places.models import *
from django.contrib.auth import get_user_model
 
 
class PostSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Post
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Attachment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username')
    child_comments = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_child_comments(self, obj):
        print(self)
        print(obj.child_comments)
        if obj.child_comments.exists():
            newChildComments = []
            for item in obj.child_comments:
                newChildComments.append(CommentSerializer(item).data)
            return newChildComments
        else:
            return None
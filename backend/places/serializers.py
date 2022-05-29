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
        if obj.child_comments.exists():
            newChildComments = []
            for item in obj.child_comments:
                newChildComments.append(CommentSerializer(item).data)
            return newChildComments
        else:
            return None
class PostsSerializer(serializers.ModelSerializer):
    attachments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

    def get_attachments(self, obj):
        attachments = Attachment.objects.filter(post_id=obj.id)
        return AttachmentSerializer(attachments, many=True).data

class MainsScreenPostsSerializer(serializers.ModelSerializer):
    attachment = serializers.SerializerMethodField()
    count = serializers.IntegerField()
    class Meta:
        model = Post
        fields = ['id', 'state', 'attachment', 'count']

    def get_attachment(self, obj):
        attachment = Attachment.objects.filter(post_id=obj.id).first()
        return AttachmentSerializer(attachment).data['image'] if AttachmentSerializer(attachment).data['image'] else None
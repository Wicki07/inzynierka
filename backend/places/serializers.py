from rest_framework import serializers 
from places.models import *
 
 
class PostSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Post
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Attachment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = ('id',
                  'user_id',
                  'post_id',
                  'rate',
                  'parent_com',
                )
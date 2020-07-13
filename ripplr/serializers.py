from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import System, Profile
from rest_framework.response import Response
from rest_framework.decorators import action

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'url'
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Profile
        fields = '__all__' 
        
class ProfileSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'      

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'    
        
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer2(required=False)
    groups = GroupSerializer(read_only=False, many=True)
    
    @action(detail=False)
    def groups(self, request):
        ug_qs = Group.objects.filter(user=request.user)
        user_groups = [g.name for g in ug_qs]
        return Response(user_groups)
    
   # groups= UserSerializer('__all__')
   # groups.save()
    class Meta:
        model = User
        fields = '__all__'                
        
class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'url'
        ) 
        

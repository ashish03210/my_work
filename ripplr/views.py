from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, viewsets, mixins
from django.contrib.auth.models import User, Group
from ripplr.serializers import UserSerializer, ProfileSerializer, GroupSerializer
from ripplr.serializers import SystemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from rest_framework.parsers import FileUploadParser
from rest_framework.authentication import TokenAuthentication
from .models import Profile
from ripplr.permissions import RipplrAppModelPermission


# Create your views here.
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, RipplrAppModelPermission]
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('is_active','first_name','id')
    ordering_fields = ('username', 'email')
    search_fields = ('id', 'first_name')
   
    
class SystemViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.raw('SELECT * FROM ripplr_profile WHERE user_id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, RipplrAppModelPermission]

 
    
class GroupViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, RipplrAppModelPermission]
    
    
class ProfilesViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
   



class ProfileUpdateView(UpdateView):
    fields = ['designation', 'salary', 'picture']
    template_name = 'auth/profile_update.html'
    success_url = reverse_lazy('my_profile')

    def get_object(self):
        return self.request.user.profile


class UploadView(APIView):
    parrser_classes = (FileUploadParser,)
    authentication_classes = (TokenAuthentication,)
    parmission_classes =(IsAuthenticated)
    
    
    def post(self, request):
        file = request.date.get('file',None)
        import pdb; pdb.set_trace()
        print(file)
        if file:
            return Response({"message": "File is recieved"}, status=200)
        else:
            return Response({"message": "File is missing"}, status=400)   
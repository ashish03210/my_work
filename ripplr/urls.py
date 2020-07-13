from django.urls import path
from . import views
from rest_framework import routers
from ripplr.views import *

router=routers.DefaultRouter()
router.register(r'users', views.UserViewSet),
router.register(r'systems', views.SystemViewSet),
router.register(r'profiles', views.ProfilesViewSet),
router.register(r'groups', views.GroupViewSet),

# place holder forn all Url path
urlpatterns = [
#    path('', views.authenticate, name="base"),
    path('uplood/', UploadView.as_view(), name="file_uplod"),
    
    
]    
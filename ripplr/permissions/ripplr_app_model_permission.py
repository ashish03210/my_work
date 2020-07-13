from rest_framework.permissions import DjangoModelPermissions

import copy

#Permission checks will typically use the authentication information in the To use custom model permissions, 
# override DjangoModelPermissions and set the  Permissions given for HR Manager
# A dictionary overring need deepcopy.
class RipplrAppModelPermission(DjangoModelPermissions):
    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)# we need deepcopy when you inherit a dictionary type 
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s'] #For API views to check for groups and permissions, we can use
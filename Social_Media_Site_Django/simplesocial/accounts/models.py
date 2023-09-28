from django.db import models
from django.contrib import auth
from django.utils import timezone
# SuperUserInformation
# User: Redi
# Email: tagarediii@gmail.com
# Password: admin

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

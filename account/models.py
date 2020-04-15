from django.db import models
from django.contrib import auth
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)




    #
    # address = models.CharField(max_length=150, blank=False)
    # phone_number = models.IntegerField(blank=False)

from django.db import models
class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=40) ## Naive method, will imrpove this when doing authentication of user

    def __str__(self):
        return self.email


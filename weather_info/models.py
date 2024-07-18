from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50,default=None)
    ip_address = models.GenericIPAddressField()
    weather_requests = models.CharField(max_length=50,default=None)

class UserQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weather_request')
    weather_requests = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.user.username} - {self.query}"

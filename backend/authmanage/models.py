from email.policy import default
from django.db import models
# from django.contrib.auth.models import User

# class User(models.Model):
    
#     username = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
#     password = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
#     email = models.CharField(max_length=1500)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     position = models.BooleanField(default=False)
#     def __str__(self):
#         return self.text
#     class Meta:
#         ordering = ('timestamp', )
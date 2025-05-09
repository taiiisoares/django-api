from django.db import models

class User(models.Model):

    user_id = models.AutoField(primary_key=True)
    user_nickname = models.CharField(max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'Id: {self.user_id} | Nickname: {self.user_nickname} | Email: {self.user_email}'
from django.db import models

from django.contrib.auth.models import User
# For profile images
from PIL import Image


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpeg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img=Image.open(self.image.path)

        if img.height > 300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Project_add(models.Model):
    pid = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=700)
    link = models.CharField(max_length=200)
    stack = models.CharField(max_length=300)
    date = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.pid = str(str(self.name[0:3])+'_'+str(self.date).split(' ')[0].split('-')[2])
        super(Project_add, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# For OTP


class OTPModel(models.Model):
    user = models.EmailField(max_length=127)
    timestamp = models.DateTimeField(auto_now_add=True)
    otp = models.IntegerField()

    class Meta:
        verbose_name = 'OTP'

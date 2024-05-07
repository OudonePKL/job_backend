from django.db import models
from users.models import UserModel

class Resume(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="user")
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    major = models.CharField(max_length=100)
    skill = models.TextField()
    image = models.FileField(verbose_name="image", upload_to="resume")
    resume_image = models.FileField(verbose_name="Resume image", upload_to="resume")
    is_recommend = models.BooleanField(default=False)

    def __str__(self):
        return self.name
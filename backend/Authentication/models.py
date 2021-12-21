from django.db import models
from django.contrib.auth import get_user_model

class UserActivate(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    activate_code = models.CharField(max_length=64)
    
    def __str__(self):
        return self.activate_code

    class Meta:
        verbose_name = "UserActivate"
        verbose_name_plural = "UserActivations"
# from django.db import models
from users.models import CustomUser

# class Project(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_projects')
#     assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_projects')
from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_projects')

    class Meta:
        db_table = 'project'
        verbose_name = ('project')
        verbose_name_plural = ('project')

    def __str__(self):
        return self.name

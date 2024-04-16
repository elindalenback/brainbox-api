from django.db import models
from django.contrib.auth.models import User

# Note Model
class Note(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('tags.Tag', related_name='notes')
    notebook = models.ForeignKey('notebooks.Notebook', on_delete=models.SET_NULL, null=True, blank=True)
    deleted = models.BooleanField(default=False)  # Soft delete flag - for future backup and possible restoration
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()
    
    def __str__(self):
        return self.title
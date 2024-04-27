from django.db import models
from django.contrib.auth.models import User
from notes.models import Note


class Like(models.Model):
    """
    Like model, related to 'owner' and 'note'.
    'owner' is a User instance and 'note' is a Note instance.
    'unique_together' makes sure a user can't like the same note twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(
        Note, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'note']

    def __str__(self):
        return f'{self.owner} {self.note}'

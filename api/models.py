from django.db import models

class Institute(models.Model):
    q1 = models.TextField()
    q2A = models.TextField(null=True, blank=True)
    q2B = models.TextField(null=True, blank=True)
    q2C = models.TextField(null=True, blank=True)
    q3 = models.TextField(null=True, blank=True)
    q4A = models.TextField(null=True, blank=True)
    q4B = models.TextField(null=True, blank=True)
    q4C = models.TextField(null=True, blank=True)
    q4D = models.TextField(null=True, blank=True)
    q4E = models.TextField(null=True, blank=True)
    q4F = models.TextField(null=True, blank=True)
    q4G = models.TextField(null=True, blank=True)
    q5A = models.TextField(null=True, blank=True)
    q5B = models.TextField(null=True, blank=True)
    q5C = models.TextField(null=True, blank=True)
    q6 = models.TextField(null=True, blank=True)
    qE1 = models.TextField(null=True, blank=True)
    qE2 = models.TextField(null=True, blank=True)
    qE3 = models.TextField(null=True, blank=True)
    qE4 = models.TextField(null=True, blank=True)
    qE5 = models.TextField(null=True, blank=True)
    qE6 = models.TextField(null=True, blank=True)
    qE7 = models.TextField(null=True, blank=True)
    qE8 = models.TextField(null=True, blank=True)
    qE9 = models.TextField(null=True, blank=True)
    qE10 = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["created_at"])]
        ordering = ['-created_at']

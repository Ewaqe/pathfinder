from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Skill(TimeStampMixin):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Topic(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return self.name

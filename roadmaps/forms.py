from .models import Skill
from django.forms import ModelForm


class SkillForm(ModelForm):

    class Meta:
        model = Skill
        fields = ['name']
from django.forms import ModelForm
from .models import Comment, LegendaryKangaroo

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = '__all__'

class LegendaryKangarooForm(ModelForm):
  class Meta:
    model = LegendaryKangaroo
    fields = '__all__'
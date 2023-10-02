from django.forms import ModelForm
from .models import Comment, LegendaryKangaroo
from django.contrib.auth.models import User

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = "__all__"

class LegendaryKangarooForm(ModelForm):
  class Meta:
    model = LegendaryKangaroo
    fields = "__all__"

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = [
      "username",
      "email"
    ]
from django.contrib import admin
from .models import Comment, LegendaryKangaroo, KangarooType

admin.site.register(Comment)
admin.site.register(LegendaryKangaroo)
admin.site.register(KangarooType)

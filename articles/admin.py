from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'timestamp', 'updated','publish']  # fields to be used to display the article
    search_fields=['content'] # search artilces by matching corresponding content

admin.site.register(Article,ArticleAdmin)

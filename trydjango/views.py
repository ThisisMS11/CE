"""
To render HTML Pages    
"""
from django.http  import HttpResponse
from articles.models import Article

article_obj = Article.objects.get(id=1)
HTML_STRING =f"<h1>{article_obj.title} + {article_obj.content}</h1>";

def home_view(request):
    return HttpResponse(HTML_STRING)
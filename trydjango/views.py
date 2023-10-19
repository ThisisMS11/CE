"""
To render HTML Pages    
"""
from django.http  import HttpResponse
from articles.models import Article
from django.template.loader  import render_to_string #,get_template


# getting data from the  sqlite in this form 
article_obj = Article.objects.get(id=2)
article_list = Article.objects.all()

# the context to be passed on to the template has to be a dictionary

myList = [100,200,300,400,500]
context ={
    "article_list":article_list,
    "title": article_obj.title,
    "content": article_obj.content,
    "myList":myList
}

# Django Templates

# using get_template 
# tmpl = get_template('home-view.html')
# tmpl_string = tmpl.render(context= context)
# tmpl_string2 = tmpl.render(context= context)

# using render_to_string
HTML_STRING = render_to_string('home-view.html', context=context)

# this way you can access the arguements , parameters passed in the url
def home_view(request, id=None,*args,**kwargs):
    print(args,kwargs)
    print('id : ', id);  
    return HttpResponse(HTML_STRING)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Article

#what are django forms 
from .forms import ArticleForm
from django import forms

def article_search_view(request):
    # print(dir(request))  : To get all the attributes of the class
    print(request.GET)
    query_dic = request.GET  #this is going to be a dictionary
    query = query_dic.get('q')

    try:
        query = int(query_dic.get('q'))
    except:
        query = None

    article_obj=None

    if query is not None:
        article_obj = Article.objects.get(id= query)
    # print(query)

    context={
        "object":article_obj
    }
    return render(request,'articles/search.html',context=context)


# create Article
# @csrf_exempt

# only authenticated users should be able to use create a new article so use login_required decorator.

# if the user is not authenticated then the user will be redirected to a 404 page not found page (default)
# @login_required
# version1
# def article_create_view(request):
#     form = ArticleForm()
#     context ={
#         "form":form
#     }
#     if request.method=="POST":
#         form = ArticleForm(request.POST or None)
#         context['form'] = form
#         # content_dic = request.POST

#         # csrf token is also coming along with content_dic which helps django verify the authenticity of the user.
#         # context ={
#         #     "title" :
#         #     "content":content_dic.get('content')
#         # }
#         # print(context)
#         # title= content_dic.get('title')
#         # content = content _dic.get('content')
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get('content')
#             object = Article.objects.create(title=title,content=content)
#             context['isCreated'] = True
#             context['object'] = object

#     return render(request,'articles/create.html',context=context)

# version2 (preferred way of doing it : less redundant code)
@login_required
def article_create_view(request):
    form = ArticleForm()
    context ={
        "form":form
    }
    if request.method=="POST":
        form = ArticleForm(request.POST or None)
        context['form'] = form
        
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get('content')
            object = Article.objects.create(title=title,content=content)
            context['isCreated'] = True
            context['object'] = object
    return render(request,'articles/create.html',context=context)


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        # grab the article from the db using the id
        article_obj = Article.objects.get(id=id)
    context={
        "object":article_obj
    }
    # render the template
    return render(request,"articles/detail.html",context=context)
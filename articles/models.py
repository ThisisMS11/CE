from django.db import models
from django.db.models.signals import pre_save,post_save
from django.utils import timezone
from .utils import slugify_instance_title


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True, null=True)
    content = models.TextField(default='default content')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # null=True: This option allows the field to have a NULL database value. In other words, if null=True is set for a field, it means that in tphe database, this field can contain a NULL value, which signifies the absence of a value.

    # blank=True: This option is related to form validation. When blank=True is set for a field, it means that the field is not required when submitting data through a form
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True,default=timezone.now)

    # overiding the save method  
    def save(self,*args,**kwargs):
        # only when we are defining the slug by ourselves we have to do this.
        
        # if self.slug is None :
        #     self.slug = slugify(self.title)'
                    # or
        #     slugify_instance_title(self,save=False)

        super().save(*args,**kwargs)


# pre save things 
def article_pre_save(sender,instance,*args,**kwargs):
    print('pre_save')
    # print(sender,instance)
    # print(args,kwargs)

    if instance.slug is None :
            slugify_instance_title(instance,save=False)

pre_save.connect(article_pre_save,sender=Article)


# post save things
def article_post_save(sender,instance,created,*args,**kwargs):
    print('post_save')
    # print(args,kwargs)
    if created :
        slugify_instance_title(instance,save=True)

post_save.connect(article_post_save,sender=Article)
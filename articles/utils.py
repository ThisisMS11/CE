import random
from django.utils.text import slugify


# https://docs.djangoproject.com/en/4.2/ref/signals/
# sender :  The model class.
# instance :The actual instance being saved.

def slugify_instance_title(instance,save=False,new_slug = None):

    # for handling initial params.
    if new_slug is not None :
        slug = new_slug
    else:
        slug = slugify(instance.title)

    # accessing the class Model from instance
    Klass = instance.__class__

    qs = Klass.objects.filter(slug=slug).exclude(id= instance.id)

    # if similar slugs already exists then we will just save our new slug in this way so that it gets differentiated from the rest though this is not enough for now.
    
    if qs.exists():
        # randomly appending some number for uniqueness
        rand_int = random.randint(300_000,500_000)

        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance,save=save,new_slug=slug)

    instance.slug = slug
    if save :
        instance.save()
    return instance

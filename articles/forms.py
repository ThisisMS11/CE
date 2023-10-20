from django import forms
from .models import Article
# Model form : Model form in django simplifies the process of creating html forms by creating forms based on your database Models.For example, if you have a model with fields for a user's name, email, and age, the model form will create fields for these attributes. 
# https://chat.openai.com/share/4eec9e38-02a1-44c8-8eb7-cc24a2eb03bd

class ArticleForm(forms.ModelForm):
    class Meta :
        model = Article
        # specify the fields which you want to include in your form.
        fields = ['title','content']

    def clean(self):
        data = self.cleaned_data
        # to determine does there already exist any Article with this title or not 
        title = data.get('title')
        qs = Article.objects.all().filter(title__icontains=title)

        if qs.exists():
            self.add_error('title',f"{title} has already been taken try another one")
        return data

# here we manually have to define what fields are to be present in our forms like here these are title and content.

class ArticleFormOld(forms.Form):
    title= forms.CharField()
    content= forms.CharField()

    # these  methods are automatically called when the is_valid method is called for the django forms as these are predefined methods used to valid the form fields in django forms. 

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print("cleaned_data : ", cleaned_data)
    #     title = cleaned_data.get('title')

    #     Example Error :
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError("This title has already been taken . ")
        
    #     print("title : ",title)
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data : ',cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title.lower().strip()=="the office":
            # adding this error to title field specifically.
            self.add_error('title','This title is taken')

        if "office" in content or "office" in title:
            # adding this error to content field specifically .
            self.add_error('content','office is not allowed in content')
            raise forms.ValidationError("office is not allowed")
        
        return cleaned_data
    
    #  the temp method is not automatically called during the form validation process because it's not part of Django's form handling. You would need to call it explicitly in your code if you want it to execute.
    # def temp(self):
    #     print("This one is also called without any specific reason ")
    #     return 
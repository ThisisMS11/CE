from django import forms
class ArticleForm(forms.Form):
    title= forms.CharField()
    content= forms.CharField()

    # these  methods are automatically called when the is_valid method is called for the django forms as these are predefined methods used to valid the form fields in django forms. 

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print("cleaned_data : ", cleaned_data)
    #     title = cleaned_data.get('title')

    #     # avoid this title
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
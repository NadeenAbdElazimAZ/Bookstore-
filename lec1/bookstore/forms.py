from django import forms
from bookstore.models import book,Author



class bookForm(forms.Form):
    title = forms.CharField(label='title' , max_length=100,
            help_text="Enter book title", widget=forms.TextInput(attrs={'class': 'form-control'}))

    code = forms.IntegerField( help_text="Enter book's code", label="code",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_of_pages = forms.IntegerField( help_text="Enter Number of bages ", label="no_of_pages",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField( help_text="Enter the price ", label="price",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label='author' , max_length=100,
            help_text="Enter the author", widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image' )


    def clean_title(self):
        title=self.cleaned_data['title']

        if len(title) < 2:
                raise forms.ValidationError("Name must be at least 2 charachter ")
        return title
    

class bookModelForm(forms.ModelForm):
     class Meta:
          model=book
          fields = ['title','code','no_of_pages','price','author','image']

     def clean_title(self):
        title=self.cleaned_data['title']

        if len(title) < 2:
                raise forms.ValidationError("Name must be at least 2 charachter ")
        return title
     



    
class AuthorForm(forms.ModelForm):
     class Meta:
          model=Author
          fields = ['id','name','image','bdate']

     def clean_title(self):
        name=self.cleaned_data['name']

        if len(name) < 2:
                raise forms.ValidationError("Name must be at least 2 charachter ")
        return name
     
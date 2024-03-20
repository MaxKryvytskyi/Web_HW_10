from django import forms
from .models import Quote, Tag, Author

class AuthorForm(forms.ModelForm):
    
    fullname = forms.CharField(max_length=50, required=True, widget=forms.TextInput())
    born_date = forms.CharField(max_length=50, required=False, widget=forms.TextInput())
    born_location = forms.CharField(max_length=80, required=False, widget=forms.TextInput())
    description = forms.CharField(max_length=8000, required=False, widget=forms.TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

# class TagForm(forms.ModelForm):
#     name = forms.CharField(max_length=40, null=False, unique=True)
    # class Meta:
    #     model = Tag
    #     fields = ['name']

class QuoteForm(forms.ModelForm):

    quote = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
    goodreads_page = forms.URLField(max_length=200, required=False)

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author', 'goodreads_page']

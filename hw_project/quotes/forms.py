from django.forms import ModelForm, CharField, TextInput, ModelMultipleChoiceField, URLField, ModelChoiceField, Textarea, CheckboxSelectMultiple
from .models import Quote, Tag, Author

class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, required=True, widget=TextInput())
    born_date = CharField(max_length=50, required=False, widget=TextInput())
    born_location = CharField(max_length=80, required=False, widget=TextInput())
    description = CharField(max_length=8000, required=False, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

# class Tag(models.Model):
#     name = models.CharField(max_length=40, null=False, unique=True)

class QuoteForm(ModelForm):
    # quote = models.TextField()
    # tags = models.ManyToManyField(Tag)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    # goodreads_page = models.URLField(max_length=200, blank=True, null=True)
    quote = CharField(widget=Textarea(attrs={'rows': 3}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    author = ModelChoiceField(queryset=Author.objects.all(), required=False)
    goodreads_page = URLField(max_length=200, required=False)

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author', 'goodreads_page']

from django.forms import ModelForm, CharField, TextInput
from .models import Quote, Tag, Author

class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, required=True, widget=TextInput())
    born_date = CharField(max_length=50, required=True, widget=TextInput())
    born_location = CharField(max_length=80, required=True, widget=TextInput())
    description = CharField(max_length=8000, required=True, widget=TextInput())
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

# class Tag(models.Model):
#     name = models.CharField(max_length=40, null=False, unique=True)

# class Quote(models.Model):
#     quote = models.TextField()
#     tags = models.ManyToManyField(Tag)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
#     goodreads_page = models.URLField(max_length=200, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
# Міграція з mongoDB в posgresql
import os 
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author # posgresql

from ..Load_mongoDB.connect_db import connect # mongoDB
from ..Load_mongoDB.models import Authors, Quotes # mongoDB

authors = Authors.objects()

for author in authors:
    Author.objects.get_or_create(
            fullname = author.fullname,
            born_date = author.born_date,
            born_location = author.born_location,
            description = author.description)
            

quotes = Quotes.objects()

for quote in quotes:
    tags = []
    for tag in quote.tags:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote.quote)))
    if not exist_quote:
        author = Authors.objects.filter(id=quote.author.id).first()
        a = Author.objects.get(fullname=author.fullname)
        q = Quote.objects.create(
            quote=quote.quote,
            goodreads_page = quote.goodreads_page,
            author=a
        )
        for tag in tags:
            q.tags.add(tag)

from bson import ObjectId
from django import template
from ..utils import connect, Authors, Quotes
from quotes.models import Tag
from django.db.models import Count 
register = template.Library()

def get_author(id_):
    author = Authors.objects(id=ObjectId(id_.id)).first()
    return author.fullname

def get_top_ten_tags(quotes):
    # select tag_id, count(*), qt.name
    # FROM public.quotes_quote_tags
    # join public.quotes_tag as qt on qt.id = tag_id 
    # GROUP BY tag_id, qt.name;

    # Запрос на топ 10 тегов
    top_tags = Tag.objects.annotate(quote_count=Count('quote')).order_by('-quote_count')[:10]
    return top_tags

def get_author_details(author):
    return 

register.filter("tags", get_top_ten_tags)
register.filter("author", get_author)
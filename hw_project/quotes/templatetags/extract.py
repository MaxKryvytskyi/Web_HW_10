from bson import ObjectId
from django import template
from ..utils import connect, Authors
# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

register = template.Library()

def get_author(id_):
    # logging.debug("_"* 30)
    # logging.debug(f"{id_.id}")
    # logging.debug("_"* 30)
    author = Authors.objects(id=ObjectId(id_.id)).first()
    # logging.debug(f"{author.fullname}")
    return author.fullname

def get_top_ten_tags(quotes):
    pass

register.filter("quotes", get_top_ten_tags)
register.filter("author", get_author)
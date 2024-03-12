from django.shortcuts import render
from django.core.paginator import Paginator
from .utils import connect, Quotes, Authors
from quotes.models import Tag, Quote, Author



def main(request, page=1):
    quotes = Quotes.objects()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})

def author(request, author_id):
    # из-за 2 баз даних 
    try:
        author_info = Authors.objects.get(id=author_id) # mongoDB
    except Exception as er:
        author_info = Author.objects.get(id=author_id) # posgreSQL
    return render(request, "quotes/author.html", context={"author": author_info})

def tag_search(request, tag):
    # select qt.name, qqt.quote_id 
    # from public.quotes_tag qt 
    # join public.quotes_quote_tags qqt on qqt.tag_id = qt.id 
    # join public.quotes_quote qq on qq.id = qqt.quote_id 
    # WHERE qt.name = 'love';
    # --Запрос на поиск цитат за тегом
    
    quotes_id = Tag.objects.filter(name=tag).values('name', 'quote__id')
    quotes = []
    for item in quotes_id:
        quote = Quote.objects.get(id=item['quote__id'])
        data = Quote.tags.through.objects.filter(quote_id=quote.id).values('tag_id')
        tags = []
        for tag_id in data:
            tag_name = Tag.objects.filter(id=tag_id["tag_id"]).values('name')
            tag_name = list(tag_name.values_list('name', flat=True))
            tags.append(*tag_name)

        quotes.append({"id" : quote.id,
                       "quote" : quote.quote,
                       "tags" : tags,
                       "author" : { "fullname" : quote.author.fullname, "id" : quote.author.id},
                       "goodreads_page" : quote.goodreads_page})  
    return render(request, "quotes/tag_search.html", context={"quotes": quotes})

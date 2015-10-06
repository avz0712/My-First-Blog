# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from Blog.models import Article


# Create your views here.

def home(request):
    # return HttpResponse('Hello world.')
    articles = Article.objects.all()
    context = {'articles': articles}
    print(context)
    return render(request, 'Blog/home.html', context)


def about(request):
    return render_to_response('Blog/about.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'Blog/article.html', {'article': article})

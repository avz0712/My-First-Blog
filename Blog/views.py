# -*- coding: utf-8 -*-

from django.http.response import HttpResponse, Http404
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from Blog.models import Article, Comments
from Blog.forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator

__author__ = 'Anrew Zaharovskyi'

# Create your views here.
PAGE_COUNT = 2


def home(request, page_number=1):
    # return HttpResponse('Hello world.')
    articles = Article.objects.all()
    current_page = Paginator(articles, PAGE_COUNT)

    if auth.get_user(request).is_anonymous():
        f_name = auth.get_user(request)
    else:
        f_name = auth.get_user(request).first_name

    context = {'articles': current_page.page(page_number),
               'username': auth.get_user(request).username,
               'first_name': f_name
               }
    return render(request, 'Blog/home.html', context)


def show_article(request, article_id):
    args = {}
    args.update(csrf(request))
    args['article'] = get_object_or_404(Article, id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['comment_form'] = CommentForm
    args['username'] = auth.get_user(request).username
    return render_to_response('Blog/article.html', args)


def about(request):
    return render_to_response('Blog/about.html')


def add_like(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, "added like")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def add_comment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(30)
            request.session['pause'] = True
    return redirect('/articles/%s/' % article_id)

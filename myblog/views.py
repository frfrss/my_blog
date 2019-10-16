from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Article,Comment
from .forms import CommentForm
from django.shortcuts import redirect
import markdown
import re
from django.http.request import HttpRequest

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'myblog/index.html', context)


def article_comment(request, article_id):
    article = get_object_or_404(Article,pk=article_id)
    article.content = markdown.markdown(article.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = article.comment_set.all()

    context = {'article':article,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'myblog/detail.html', context=context)


def vote(request,article_id):
    form = CommentForm()
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment_list = article.comment_set.all()
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('http://127.0.0.1:8000/myblog/'+str(article_id)+'/')

    else:
        article = get_object_or_404(Article, pk=article_id)
        article.content = re.sub('',r'<p>|</p>',str(article.content))
        comment_list = article.comment_set.all()
        context = {'article': article,
                   'form': form,
                   'comment_list': comment_list
                   }
        return render(request, 'myblog/detail.html', context=context)

    # return redirect(article)






# Create your views here.

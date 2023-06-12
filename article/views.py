from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm



def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm()
    
    articles = Article.objects.all()
    context ={'form': form, 'articles': articles}
    return render(request, 'index.html', context)

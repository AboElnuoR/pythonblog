from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render
from django.template import RequestContext
from .models import *
from blog.forms import UserForm
from .forms import ArticleForm, ArticleForm2, CommentForm, CommentForm2
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage


def index(request):
    all_posts = Article.objects.all()
    data = {'posts': all_posts}
    return render(request, 'blog/index.html', data)


def latest_5(request):
    posts_5 = Article.objects.filter(is_published=True).order_by('-publish_date')[0:5]
    data = {'posts': posts_5}
    return render(request, 'blog/latest_posts.html', data)


def single(request, post_id):
    single = Article.objects.get(pk=post_id)
    data = {'posts': single}
    return render(request, 'blog/single.html', data)


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)

            if 'user_image' in request.FILES:
                user.user_image = request.FILES['user_image']
            user.save()

            email = EmailMessage('Python blog', 'thank you for registering!', 'php.lover17@gmail.com',
                                 [user.email])
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request,
                  'blog/register.html',
                  {'user_form': user_form, 'registered': registered})

@csrf_protect
def login(request):
    if request.COOKIES.get("sessionid", None):
        print "exist"
        return HttpResponseRedirect('loggedin')
    else:
        c = {}
        c.update(request)
        return render(request, 'blog/signin.html', c)


def signin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if not request.POST.get('remember_me'):
        request.session.set_expiry(0)

    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect('loggedin')
    else:
        return HttpResponseRedirect('invalid')


def loggedin(request):
    print request.user.id
    form = ArticleForm()
    return render(request, 'blog/loggedin.html', {"Name": request.user.username, 'form': form})


def invalid(request):
    return render(request, 'blog/invalid.html')


def logout_view(request):
    logout(request)
    return render(request, 'blog/signin.html')


def add_article(request, user_id):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        title = request.POST.get('title')
        subject = request.POST.get('content')
        image = request.POST.get('image')
        date = request.POST.get('publish_date')
        new_article = Article(title=title, atricle_content=subject, image=image, publish_date=date,
                              user_id=request.user)
        new_article.save()

        return HttpResponse("Article added successfully")
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {"Name": request.user.username, 'form': form})


def edit_article(request, art_id):
    article = get_object_or_404(Article, pk=art_id)
    if article.user_id != request.user:
        return HttpResponse("Not allowed to edit this article")
    else:
        form = ArticleForm2(request.POST, instance=article)
        if request.POST:
            if form.is_valid():
                form.save()
                return HttpResponse("Article edited successfully")

    return render(request, 'blog/edit_article.html', {'form': form})


def add_comment(request, comm_id):
    article = Article.objects.get(pk=comm_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        subject = request.POST.get('content')
        new_comment = Comment(comment_content=subject, article_id=article, user_id=request.user)
        new_comment.save()

        return HttpResponse("Comment added successfully")
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'article': article})


def edit_comment(request, post_id, comm_id):
    comment = Comment.objects.get(pk=comm_id)
    if comment.user_id != request.user:
        return HttpResponse("Not allowed to edit this comment")
    else:
        form = CommentForm2(request.POST, instance=comment)
        if request.POST and form.is_valid():
                form.save()
                return HttpResponse("comment edited successfully")

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

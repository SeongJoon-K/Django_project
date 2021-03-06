from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm


def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts': posts})


# 즐로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# create가 실행된다는 것은 create가 어떤 요청을 받았기 때문에 실행되는 것이다.


def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# django form을 이용해서 입력값을 받는 함수,
# GET, (=입력값을 받을 수 있는 html을 갖다줘야한다.)
# POST 요청 (=입력한 내용을 DB에 저장하는 기능을 수행. form에서 입력한 내용을 처리)


def formcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():  # request POST에 담겨 있는 데이터가 유효하다면?
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = BlogForm()  # 입력을 받을 수 있는 HTML을 갖다주기
    return render(request, 'form_create.html', {'form': form})


def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():  # request POST에 담겨 있는 데이터가 유효하다면?
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()  # 입력을 받을 수 있는 HTML을 갖다주기
    return render(request, 'form_create.html', {'form': form})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail': blog_detail, 'comment_form': comment_form})


def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)

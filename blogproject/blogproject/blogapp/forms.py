from django import forms
from .models import Blog, Comment


class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()  # form 으로 부터 character 형식을 타이틀을 입력받을거에요
    # form으로 부터 character 형식을 body 값을 입력받을거에요
    body = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['title', 'body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        # fields = ['title', 'body']

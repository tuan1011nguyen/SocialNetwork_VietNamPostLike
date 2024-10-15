# forms.py
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image','content']
        widgets = {
            'content': forms.Textarea(attrs={'id': 'markdown-editor'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content_cmt']  # Thay đổi 'cmt' thành 'content_cmt'
        widgets = {
            'content_cmt': forms.Textarea(),
        }

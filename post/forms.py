from django import forms
from .models import Post

# This form handels cresting a new Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'title' , 'body']
 
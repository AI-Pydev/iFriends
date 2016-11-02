from django import forms
from .models import Blog, Person, Post

sList = [('S', 'Hill'),('M','Peak'), ('L', 'Climber')]
class EmailForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'size':'50'}))
    sender = forms.EmailField(max_length=30, widget=forms.TextInput(attrs={'size':'30'}))
    date = forms.DateTimeField()
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':'6','cols':'75'}))



class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'text', 'date',)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('name', 'gender', 'birthday', 'email', 'favouriteURL', 'desc', 'friends', 'blogs')





class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

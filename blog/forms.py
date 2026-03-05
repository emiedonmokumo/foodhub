from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.CharField(max_length=255, required=False)
    content = forms.CharField(widget=forms.Textarea, required=False)
    featured_image = forms.CharField(max_length=512, required=False)
    published_date = forms.DateTimeField(required=False)

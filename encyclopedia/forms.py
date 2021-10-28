from django.db import models
from django.forms import ModelForm


class WikiPage(models.Model):
    Title = models.CharField(max_length=256)
    Content = models.TextField(max_length=256)


class WikiPageForm(ModelForm):
    class Meta:
        model = WikiPage
        fields = ["Title", "Content"]


class EditWikiPageForm(ModelForm):
    class Meta:
        model = WikiPage
        fields = ["Content"]

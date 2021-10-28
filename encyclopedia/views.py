import random

from django import forms
from django.http import HttpResponseBadRequest
from django.shortcuts import render, HttpResponse, redirect

from encyclopedia import util, forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def open_entry(request, title):
    html = util.get_html_content(title)
    if html:
        return render(request, "encyclopedia/entry.html", {
            "title": title, "html": html
        })
    else:
        return HttpResponse("This web page does not exist yet.")


def search(request):
    if request.method == 'POST':
        query = request.POST['q']
        partial_results = util.get_partial_results(query)
        html = util.get_html_content(query)
        if html:
            return render(request, "encyclopedia/entry.html", {
                "title": query, "html": html
            })
        else:
            return render(request, "encyclopedia/search_results.html", {
                "search_results": partial_results, "query": query
            })


def create_new_page(request):
    if request.method == "POST":
        form = forms.WikiPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["Title"]
            text = form.cleaned_data["Content"]
            if title not in util.list_entries():
                util.save_entry(title, text)
                html = util.get_html_content(title)
                return render(request, "encyclopedia/entry.html", {
                    "title": title, "html": html
                })
            return HttpResponse("This web page already exists.")
        else:
            return HttpResponseBadRequest("Form is not valid.")
    return render(request, "encyclopedia/create.html", {
        "form": forms.WikiPageForm()
    })


def edit_page(request, title):
    if request.method == "GET":
        content = util.get_entry(title)
        page = forms.WikiPage(Title=title, Content=content)
        form = forms.EditWikiPageForm(instance=page)
        return render(request, "encyclopedia/edit.html", {
            "form": form,
            "title": title
        })
    elif request.method == "POST":
        form = forms.EditWikiPageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["Content"]
            util.save_entry(title, text)
            return redirect(f"/wiki/{title}")
        else:
            return HttpResponseBadRequest("Form is not valid.")


def random_page(request):
    title_list = util.list_entries()
    random_page = random.choice(title_list)
    return redirect(f"/wiki/{random_page}")

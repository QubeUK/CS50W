from random import choice
from django.shortcuts import render, reverse, HttpResponseRedirect
from django import forms
from . import util


class NewWikiForm(forms.Form):
    """Django form class"""
    title = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter Title"}),
        max_length=30,
    )
    content = forms.CharField(
        label="", widget=forms.Textarea(attrs={"placeholder": "Enter Markdown Here"})
    )


class EditWikiForm(forms.Form):
    """Django form class"""
    title = forms.CharField(label="", widget=forms.TextInput(), max_length=30)
    content = forms.CharField(label="", widget=forms.Textarea())


def index(request):
    """Creates list of entires for index.html"""
    if "articles" not in request.session:
        request.session["articles"] = []
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def new_page(request):
    """Displays form and gets data for new wiki entry"""
    if request.method == "POST":
        form = NewWikiForm(request.POST)
        if form.is_valid():
            article = form.cleaned_data
            util.save_entry(article["title"], article["content"])
            return HttpResponseRedirect(reverse("wiki:index"))
        return render(request, "wiki/create.html", {"form": form})
    return render(request, "encyclopedia/create.html", {"form": NewWikiForm()})


def edit(request):  # Need to fix edit from random page
    """Edit an article"""
    if request.method == "POST":
        form = EditWikiForm(request.POST)        
        if form.is_valid():
            article = form.cleaned_data            
            util.save_entry(article["title"], article["content"])
            return HttpResponseRedirect(reverse("wiki:index"))
    form = EditWikiForm()
    form["title"].initial = (request.META["HTTP_REFERER"]).rsplit("/")[-2]
    form["content"].initial = util.get_entry(form["title"].initial)
    return render(request, "encyclopedia/edit.html", {"title": "Page Editor", "form": form})


def display(request, article=None):
    """Displays a requested article"""
    if article is None:
        article = choice(util.list_entries())
    html, title = util.page_info(article)
    return render(request, "encyclopedia/display.html", {"html": html, "title": title})


def search(request):
    """Displays a searched for article"""
    result = []
    query = request.GET["query"]
    if query.casefold() in map(str.casefold, util.list_entries()):
        html, title = util.page_info(query)
        return render(request, "encyclopedia/display.html", {"html": html, "title": title})
    for entry in util.list_entries():
        if query.casefold() in entry.casefold():
            result.append(entry)
    return render(request, "encyclopedia/search.html",{"title": "Search Results", "result": result},)

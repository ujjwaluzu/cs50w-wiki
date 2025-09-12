from django.shortcuts import render
from django import forms
import markdown
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect
from random import choice

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, name):
    entrie = util.get_entry(name)
    if not entrie:
        return render(request, "encyclopedia/errorpage.html",{
            "message": "This page cannot be found"
        })
    html_content = markdown.markdown(entrie)
    return render(request, "encyclopedia/content.html", {
        "title": name,
        "content": html_content
    })
class NewPageform(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class': 'form-control w-75 mb-2'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control w-75'}), label="Description",)

    
def newpage(request):
    if request.method == "POST":
        form = NewPageform(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
        
        if util.get_entry(title):
            return render(request, "encyclopedia/errorpage.html", {
                "message": "This page already exists"
            })
        else:
            util.save_entry(title, description)

            return HttpResponseRedirect(reverse("wiki", args=[title]))


    return render(request, "encyclopedia/newpage.html", {
        "form": NewPageform()
    })

def randompage(request):
    name = choice(util.list_entries())
    return HttpResponseRedirect(reverse("wiki", args=[name]))


def edit(request, name):
    entry_content = util.get_entry(name)
    if not entry_content:
        return render(request, "encyclopedia/errorpage.html", {
            "message": f"The page '{name}' does not exist."
        })
    if request.method == "POST":
        form = NewPageform(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            util.save_entry(title, description)
            return HttpResponseRedirect(reverse("wiki", args=[name]))
    else:
        form = NewPageform(initial={
            "title": name,
            "description": entry_content
                })


    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "title": name
    })

def search(request):
    query = request.GET.get("q").strip()
    entries = util.list_entries()
    if query.lower() in (entry.lower() for entry in entries):
        return HttpResponseRedirect(reverse("wiki", args=[query]))
    results = []
    for entry in entries:
        if query.lower() in entry.lower():
            results.append(entry)
    
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })
from django.shortcuts import render
from django import forms
import markdown
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect

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
        "content": html_content
    })
class NewPageform(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")

    
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
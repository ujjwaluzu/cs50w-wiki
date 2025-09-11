from django.shortcuts import render
import markdown
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, name):
    entrie = util.get_entry(name)
    if not entrie:
        return render(request, "encyclopedia/errorpage.html")
    html_content = markdown.markdown(entrie)
    return render(request, "encyclopedia/content.html", {
        "content": html_content
    })

def newpage(request):
    return render(request, "encyclopedia/newpage.html")
from django.shortcuts import render
import spacy
from newspaper import Article


# Create your views here.

def home(request):
    return render(request, "home.html")

def article(request):
    return render(request, "article.html", {})


def articledownload(request):

    url = request.POST.get('getarticle')
    nlp = spacy.load("en_core_web_sm")
    article = Article(url)
    article.download()
    article.parse()
    doc = article.text

    print(doc)

    doctitle = article.title

    print(doctitle)

    docimage =article.top_image

    print(docimage)

    article.nlp()
    docsummary = article.summary

    print(docsummary)

    
    return render(request, 'article.html', {'text':doc, 'title':doctitle, 'image':docimage, 'summary': docsummary})
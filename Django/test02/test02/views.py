from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    # context={"name":"xsnd"}
    return render(request,"index.html")
def search(request):
    request.encoding('utf-8')
    query=request.GET['q']

    if query:
        message='cxnr'+query
    else:
        message='nssscv'
    return  HttpResponse(message)
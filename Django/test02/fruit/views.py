from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def main(request):
    context={"name":"xsnd"}
    return render(request,"index.html",context)
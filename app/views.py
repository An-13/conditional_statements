from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':200,'b':300,'c':400}
    return render(request,'conditional.html',d)
from django.shortcuts import render
def input(request):
    return render(request, 'input.html')
def table(request):
    a=int(request.GET['t1'])
    b=int(request.GET['t2'])
    c=range(1,b+1)
    d={'e':a,'f':c}
    return render(request, 'display.html',d)

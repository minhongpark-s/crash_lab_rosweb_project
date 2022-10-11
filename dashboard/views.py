from django.shortcuts import render

def dashboard(request):
    return render(
                request,
                'dashboard/index.html',
                 )
# Create your views here.
def roslibjs(request):
    return render(
                request,
                'dashboard/roslibindex.html',
                 )
def roslibjsmain(request):
    return render(
                request,
                'dashboard/roslibjsmain.html',
                 )
                 

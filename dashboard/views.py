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

def roslibjsSP(request):
    return render(
                request,
                'dashboard/roslibjsSubPub.html',
                 )

def serviceConnectionTest(request):
    return render(
                request,
                'dashboard/serviceConnectionTest.html',
                 )
                 

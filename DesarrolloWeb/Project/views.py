from django.shortcuts import render
from django.contrib import messages
from Project.models import Users

# Create your views here.
def Login(request):
    return render(request, "Login.html")

def Index(request):
    return render(request, "Index.html")


def loginUser(request):
    if request.method=='POST':
        try:
            User= Users.objects.get(username=request.POST['username'], password=request.POST['password'])
            print("User: ", User)
            request.session['password']=User.username
            return render(request, 'index.html')
        except Users.DoesNotExist as e:
            messages.success(request, 'no existe')
    return render(request, 'login.html')
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Todo

def signup(request):    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2 :
            return render(request,"signup.html",{'error':'password did not match!Try again'})
        
        if User.objects.filter(username=username).exists():
            return render(request,"signup.html",{'error':'User already exists!'})
        
        User.objects.create_user(
            username=username,
            email=email,
            password=pass1,
        )
        
        
        return redirect('login')
    
    return render(request,"signup.html")
    

def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todo')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, "login.html")



# Show Todo Page
def todo_page(request):
    
    if request.method == "POST":
        title = request.POST.get('task_title') # Match the 'name' attribute in HTML
        if title:
            Todo.objects.create(title=title, user=request.user)
        return redirect('todo')

    # Fetch tasks for the logged-in user only
    res = Todo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})


# Delete Task
def delete_task(request, id):
    # our model uses `sno` as the auto‑created primary key, so use pk lookup
    task = Todo.objects.get(pk=id)
    task.delete()
    return redirect('todo')


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')



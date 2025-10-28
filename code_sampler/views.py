from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from django.http import HttpResponse
from .models import tasks
from django.db.models import Q
from .form import task_from , new_user_form
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    all_tasks = tasks.objects.all().order_by('-task_date')  # Fetch all tasks, ordered by date

   
    paginator = Paginator(all_tasks, 8)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'all_task': page_obj})  # Use 'home.html'


#create
@login_required
def create_task(request):
    if request.method == 'POST':
        form = task_from(request.POST , request.FILES)
        if form.is_valid():
            saved_task = form.save(commit=False)
            saved_task.user = request.user
            saved_task.save()
        return redirect('home')
    else:
        form = task_from()
        para = {
            'form' : form
        }
    return render(request , 'create.html' , para)

#update
@login_required
def edit(request , id):
    task = get_object_or_404(tasks , pk = id , user = request.user)
    if request.method == 'POST':
        form = task_from(request.POST , request.FILES  , instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('home')
    else:
        form = task_from(instance=task)
        para = {
            'form' : form
        }
    return render(request , 'create.html' , para)


# delete 
@login_required
def delete_task(request , id):
    get_task = get_object_or_404(tasks , pk = id)
    get_task.delete()
    return redirect('home')

# for getting the code
def get_code(request , id):
    get_task = get_list_or_404(tasks, pk=id)
    para = {
                'all_task': get_task
            }
    return render(request, 'detail.html', para)

#for search the task
def search(request):
    if request.method == "POST":
        name = request.POST.get('task_name')
        if name != "":
            get_tasks = tasks.objects.filter(Q(task_name__icontains = name))
            para = {
                'all_task': get_tasks
            }
        else: return redirect('home')
           
    return render(request, 'search.html', para)


# filttered task
def only_user_task(request):
    all_task = tasks.objects.filter(user=request.user).order_by('-task_date')
    para = {
        'all_task' : all_task
    }
    return render(request , 'list.html' , para) 

# for register new user
def user_reg(request):
    if request.method == 'POST':
        form = new_user_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return redirect('home')
    else:
        form = new_user_form()
    para =  { 'form' : form}
    return render(request , 'registration/register.html' , para)
    



#contact form
def contact(request):
    return render(request , 'contact.html')
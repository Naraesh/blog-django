from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import authorpost


def profile(request):
    return render(request,'profile.html')
    

def content(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        pos_title = request.POST.get('post_title')
        content = request.POST.get('post_content')
        date = request.POST.get('date')
        url = request.POST.get('user profile link')

        obj=authorpost()
        obj.name=username
        obj.post_title=pos_title
        obj.post_content=content
        obj.date_published=date
        obj.user_profile_link=url
        obj.save()
        return redirect('profile')
    else:
        return HttpResponse("<script> Failed</script>")

def edit(request, id):  
    usr = authorpost.objects.get(id=id)  
    return render(request,'edit.html', {'user':usr})  

def destroy(request,id):
    authorpost.objects.get(id=id).delete()
    return render(request,'myfeeds.html')

def update(request, id): 
    if(request.method=="POST"):
        use = authorpost.objects.get(id=id)  
        use.name = request.POST.get('uname')
        use.pos_title = request.POST.get('post_title')
        use.date_published = request.POST.get('date')
        use.post_content=request.POST.get('post_content')
        use.user_profile_link=request.POST.get('profile_link')
        use.save()
        return redirect('/') 
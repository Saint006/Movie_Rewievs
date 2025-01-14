from django.shortcuts import render
from django.shortcuts import redirect
from . models import Movieinfo
# Create your views here.

from . forms import MovieForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




@login_required(login_url='login')
def create(request):
    
    frm=MovieForm()
   #censor=CensorInfo()
    if request.POST:
        frm=MovieForm(request.POST,request.FILES)
        #censor=CensorInfo(rating=request.POST['rating'],certified_by=request.POST['certified_by'])
        if frm.is_valid:
            movie = frm.save(commit=False)
            movie.created_by = request.user
            movie.save()
            #censor.save()
            #frm=MovieForm()
            #if hasattr(request.user, 'list'):
                #print(request.user)
                #request.user.list.add(movie)

            return redirect('list')
        else:
            print(frm.errors)
            frm=MovieForm()
            print(frm.errors)



    return render(request,'create.html',{'frm':frm})


@login_required(login_url='login')
def list(request):
    recent_visits=request.session.get('recent_visits',[])
    co=request.session.get('count',0)
    co=int(co)
    co=co+1
    request.session['count']=co
    recent_movie_set=Movieinfo.objects.filter(pk__in=recent_visits) 
    search = request.GET.get('search')
    if search:
        movie_list=Movieinfo.objects.filter(created_by=request.user,title__icontains=search)
    else:
        movie_list=Movieinfo.objects.filter(created_by=request.user) 
    print(request.user)
    #ls=Movieinfo.objects.get(pk=pk)

    response = render(request,'list.html',{'recent_movies':recent_movie_set,'movies':movie_list,'visits':co})
    
    return response

@login_required(login_url='login')
def edit(request,pk):
    instance_edited = Movieinfo.objects.get(pk=pk)
    frm=MovieForm(instance=instance_edited)
    if request.POST:
        frm=MovieForm(request.POST,request.FILES,instance=instance_edited)
        if frm.is_valid():  
            instance_edited.save()
            frm=MovieForm()
            return redirect('list')
    else:
        request.session['recent_visits']=[pk]+request.session.get('recent_visits',[])
        frm=MovieForm()
        frm = MovieForm(instance=instance_edited)
    print(Movieinfo.objects.get(pk=pk).title)
        

    
    return render(request,'create.html',{'frm':frm})

@login_required(login_url='login')
def delete(request,pk):
    instance = Movieinfo.objects.get(pk=pk)
    instance.delete()
    movie_list=Movieinfo.objects.all()
    return render(request,'list.html',{'movies':movie_list})
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
# from .models import Userinfo
from django.http import JsonResponse

from mistershoppie.models import Users, normusers



def user_login(request):

    if request.session.has_key('username'):

        return redirect('/')
    else:

        if(request.method == 'POST'):

            username = request.POST['username']
            password = request.POST['password']
            if(User.objects.filter(username=username)):
                username = User.objects.get(username=username)
                user = authenticate(username=username, password=password)
                if user is not None:
                    request.session['id'] = user.id
                    request.session['username'] = user.username
                    # cartValue = int(Cart.objects.filter(userId_id = user.id).count())
                    return JsonResponse( 
                        {'success':True},
                        safe=False
                    )
                else:
                    return JsonResponse(
                        {'success':False}, 
                        safe=False
                    )
            else:
                return JsonResponse(
                        {'success':False},
                        safe=False
                ) 
        else:
            return render(request, 'login.html')






    user = request.session.get('username')
    if request.method == "POST":
        username  = request.POST['username']
        password  = request.POST['password']
        
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            request.session['id'] = user.id
            request.session['username'] = user.username

            return JsonResponse(
                {'success':True},
                safe=False
            )
        else:
            return JsonResponse(
                {'success':False},
                safe=False
            )
    elif(user):
        return redirect('/display')
    else:
        return render(request,"login.html",{'user':user})


def display(request):
    user = request.session.get('username')   
    if(user):
        
        # data = Userinfo.objects.all()
        return render(request,"demi.html",)
    else:
        return redirect("/")
def signup(request):
        user=request.session.get('username')
        if request.method == "POST":
            first_name  = request.POST['first_name']
            last_name   = request.POST['last_name']
            username    = request.POST['username']
            email_id    = request.POST['email']
            password_1  = request.POST['password1']
            password_2  = request.POST['password2']
            print("hello 1")

            if (password_1 == password_2):
                if User.objects.filter(username=username):
                    messages.info(request,'Username taken')
                    print("hello 2")

                    return redirect('/signup')
                elif User.objects.filter(email=email_id):
                   messages.info(request,'Email taken')
                   print("hello 3")

                   return redirect('/signup')
                else:
                   users = User.objects.create_user(username=username,password=password_1,email=email_id,first_name=first_name,last_name=last_name)
                   users.save()
                   print("hello 4")

                   return redirect('/')
               
            else:
                messages.info(request,'password not matching')
                print("hello 5")
                return redirect(signup)
        elif(user):
            print("hello 6")
            return redirect(display)
        else:
            print("hello 7")
            return render(request,'register.html',{'user':user})

def logout(request):
    try:
        request.session.flush()
        
    except:
        pass
    return redirect("/")
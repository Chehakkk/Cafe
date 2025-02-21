from django.shortcuts import render,redirect
from .models import cafes,jain,sweet,place,bar,Wishlist,visitor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
# import razorpay
from datetime import datetime
from django.core.mail import send_mail
# Create your views here.
def home(request):
     context={}
     if request.user.is_authenticated:
        username = request.user.username
        context = {'username': username}
        
     Cafes=cafes.objects.all()
     context['Cafes']=Cafes
     Jain=jain.objects.all()
     context['Jain']=Jain
     return render(request,'index.html',context)

def viewdetail(request,cid):
    context={}
    Cafes=cafes.objects.get(id=cid)
    context['Cafes'] = Cafes
    return render(request,"info.html",context)
def jinfo(request,cid):
    context={}
    Jain=jain.objects.get(id=cid)
    context['Jain']=Jain
    return render(request,'jain.html',context)



def registration (request):
    context={}
    if(request.method=='POST'):
        uname = request.POST['uname']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']
        if (uname==''or upass==''or ucpass==''):
            context['error']="please fill all the fields"  
            return render(request,"register.html",context)
        elif (upass!=ucpass):
            context['error']="password should be same "
            return render(request,"register.html")
        else:
            user_obj=User.objects.create(password=upass,username=uname,email=uname)
            user_obj.set_password(upass)
            user_obj.save()
            context['success']="User registered successfully"
            return render(request,"register.html",context)
    else:
        return render(request,"register.html")

def user_login(request):
    context={}
    if(request.method=='POST'):
        uname=request.POST['uname']
        password=request.POST['upass']
        if(uname=='' or password==''):
            context['error']="please fill all the fields"
        u = authenticate(username=uname,password=password)
        if u is not None:
            login(request,u)
            return redirect('/')
        else:
            context['error']= "invalid username or password"
            return render (request,"login.html",context)
    else:
        return render(request,"login.html",context) 
    
def user_logout(request):
    logout(request)
    return redirect("/login") 

# Views for specific Cusine
def dessert(request):
    context={}
    desserts=sweet.objects.all()
    context['desserts']=desserts
    return render(request,'dessert.html',context)

def pinfo(request):
    context={}
    Place=place.objects.all()
    context['Place']=Place
    return render(request,'place.html',context)

def club(request):
    context={}
    Club=bar.objects.all()
    context['Club']=Club
    return render(request,'club.html',context)



def catfilter(request,cid):
    Cafes=cafes.objects.filter(category=cid)
    Jain=jain.objects.filter(category=cid)
    context={}
    context['Cafes'] = Cafes
    context['Jain']=Jain
    
    return render(request,"index.html",context)

# View for dessert category
def catfilterd(request,cid):
    desserts=sweet.objects.filter(category=cid)
    context={}
    context['desserts']=desserts
    return render(request,'dessert.html',context)

# View for place  category
def catfilterp(request,cid):
     Place=place.objects.filter(category=cid)
     context={}
     context['Place']=Place
     return render(request,'place.html',context)

# View for Restaurant and bars  category
def catfilterb(request,cid):
     Club=bar.objects.filter(category=cid)
     context={}
     context['Club']=Club
     return render(request,'club.html',context)

def addTowish(request,cid):
    if(request.user.is_authenticated):
        uid=request.user.id
        u=User.objects.get(id=uid)
        c=cafes.objects.get(id=cid)
        # j=jain.objects.get(id=jid)
        # d=sweet.objects.get(id=did)
        # p=place.objects.get(id=pid)
        # r=bar.objects.get(id=rid)
        c=Wishlist.objects.create(uid=u,cid=c)
        c.save()
        return redirect("/")
    else:
        return redirect("/")


    
  # View for to view wishcart   

def viewwish(request):
    context={}
    user=request.user.id
    c=Wishlist.objects.filter(uid=user)
    np=len(c)
    context['Cafes']=c
    context['desserts']=c
    context['Place']=c
    context['Club']=c
    return render(request,'wishlist.html',context)  






# def addtowish(request, cid):
    if request.user.is_authenticated:
        uid = request.user.id
        user = User.objects.get(id=uid)

        # Assuming you want to create Wishlist entries for cafes, sweets, places, and bars
        if cafes.objects.filter(id=cid).exists():
            cafe = cafes.objects.get(id=cid)
            wishlist_entry = Wishlist.objects.create(uid=user, cafe=cafe)
            wishlist_entry.save()

        elif sweet.objects.filter(id=cid).exists():
            sweet_item = sweet.objects.get(id=cid)
            wishlist_entry = Wishlist.objects.create(uid=user, sweet=sweet_item)
            wishlist_entry.save()

        elif place.objects.filter(id=cid).exists():
            place_item = place.objects.get(id=cid)
            wishlist_entry = Wishlist.objects.create(uid=user, place=place_item)
            wishlist_entry.save()

        elif bar.objects.filter(id=cid).exists():
            bar_item = bar.objects.get(id=cid)
            wishlist_entry = Wishlist.objects.create(uid=user, bar=bar_item)
            wishlist_entry.save()

        else:
            # Handle the case when the type of place is not recognized
            return redirect("/")

        wishlist_entry.save()
        return redirect("/")
    # else:
        # Add code or comments for the else block
        # pass
def reservation(request):
    order=Wishlist.objects.filter(uid=request.user.id)
    client = razorpay.Client(auth=("rzp_test_zW7NtKv2qBRdJm", "zQsEYklfN5d8PTC72nVC4N7T"))

    data = { "amount": 200, "currency": "INR", "receipt":"user"}
    payment = client.order.create(data=data)
    print(payment)
    context={}
    context['payment']=payment
    if(request.method=='POST'):
        uname=request.POST['uname']
        unum=request.POST['unum']
        uphone=request.POST['uphone']
        udate=request.POST['udate']
        uemail=request.POST['uemail']
        selected_date = datetime.strptime(udate, '%Y-%m-%d').date()
        current_date = datetime.now().date()
        if (uname=='' or unum=='' or uphone=='' or udate=='' or uemail==''):
            context['error']="Please fill all the information"
            return render(request,'reservation.html',context)
        elif(selected_date < current_date):
            context['error'] = "Please select a future date"
            return render(request, 'reservation.html', context)
        else:
             user_obj=visitor.objects.create(email=uemail,name=uname,contact=uphone,visitors=unum,date=udate)
             user_obj.save()
             context['success']="Visit soon we're Waiting"
             print("sucess")
             return render(request,"reservation.html",context)
    else:
        return render(request,'reservation.html')    
    
def sendusermail(request):
    msg="Reservation Done Succesfully ...So see you there on time ! "
    send_mail(
    "Cafeteria Reservation ",
    msg,
    "chehakkankariya@gmail.com",
    ["chehakkankariya@gmail.com"],
    fail_silently=False,
    )       
    return redirect("/")                                  
    
    

def remove_res(request):
     if request.user.is_authenticated:
      user=request.user
      remove=Wishlist.objects.filter(uid=user)
     for i in remove:
         i.delete()
         return redirect("/")
    
# def visit(request):
#     return render(request,'booking.html')    

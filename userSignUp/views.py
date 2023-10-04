from django.shortcuts import render, redirect
from .models import User_DB,admin_add_auction_items,Bid
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def homePage(request):
    auction_items = admin_add_auction_items.objects.all()
    
    return render(request, 'home.html', {'auction_items': auction_items})

def signUp(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        age = request.POST["age"]

        # Create a new user and save it to the database
        user_details = User_DB(name=name, password=password, age=age)
        user_details.save()


    return render(request, 'signupForm.html')

def signIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User_DB.objects.get(name=username, password=password)
        except User_DB.DoesNotExist:
            user = None

        if user is not None and user.tokens > 0:
            name = user.name
            user.tokens -= 1
            user.save()
            password = user.password
            auction_items = admin_add_auction_items.objects.all()
    
            return render(request, 'home.html', {'name': name, 'password': password,'available_tokens':user.tokens,
            'auction_items': auction_items})

    error_message = "Invalid credentials. Please try again."
    return render(request, 'signinForm.html', {'error_message': error_message})


def updateProfile(request):
    if request.method == "POST":
        new_name = request.POST.get("newName")
        new_password = request.POST.get("newPassword")
        
        user_profile = User_DB.objects.get(id=request.user.id)

        user_profile.name = new_name
        user_profile.password = new_password
        user_profile.save()
        
        auction_items = admin_add_auction_items.objects.all()

        return render(request, 'home.html',{'name': new_name, 'password': new_password,'auction_items': auction_items})

    return render(request, 'signinForm.html')

def place_bid(request):
    if request.method == 'POST':
        bid_value = request.POST.get('bid')
        item_id = request.POST.get('item_id')
        
        user = User_DB.objects.get(id=1)
        
        auction_item = admin_add_auction_items.objects.get(id=item_id)
        
        highest_bid = Bid.objects.filter(auction_item=auction_item).order_by('-bid_amount').first()
        
        if not highest_bid or int(bid_value) > highest_bid.bid_amount:
            bid = Bid(user=user, auction_item=auction_item, bid_amount=bid_value)
            bid.save()
            
        else:
            pass
        
        user_profile = User_DB.objects.get(id=user.id)
        
        auction_items = admin_add_auction_items.objects.all()
        
        return render(request, 'home.html', {
            'name': user_profile.name,
            'password': user_profile.password,
            'available_tokens': user_profile.tokens,
            'auction_items': auction_items,
            'highest_bid':highest_bid
        })

    return redirect('signinForm.html')  

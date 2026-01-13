from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from decimal import Decimal
from django.contrib import messages

from .models import User, Listing, Category, Bid, Watchlist, Comment


def listing(request, listing_id):
    listing_obj = Listing.objects.get(id=listing_id)

    is_watching = False
    if request.user.is_authenticated:
        is_watching = Watchlist.objects.filter(
            user=request.user,
            listing=listing_obj
        ).exists()
    winner = None
    if not listing_obj.isActive:
        highest = listing_obj.bids.order_by("-amount").first()
        if highest:
            winner = highest.user

    return render(request, "auctions/listing.html", {
        "listing": listing_obj,
        "watching": is_watching,
        "winner": winner,

    })

def watch_list(request):
    listings = Listing.objects.filter(watched__user=request.user)
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })


def toggle_watchlist(request, listing_id):
    listing_obj = Listing.objects.get(id=listing_id)
    if request.method == "POST":
        watch = Watchlist.objects.filter(user=request.user, listing=listing_obj)
        if watch.exists():
           watch.delete()
        else:
            Watchlist.objects.create(user=request.user, listing=listing_obj)
    return HttpResponseRedirect(reverse("listing", args=[listing_obj.id]))


def place_bid(request, listing_id):
    listing_bid = Listing.objects.get(Listing, id=listing_id)
    bid_amount = Decimal(request.POST["bid"])
    current = listing.current_price()
    if bid_amount <= current:
        messages.error(request, "Bid must be higher than current price.")
    else:
        Bid.objects.create(
            listing=listing,
            user=request.user,
            amount=bid_amount,
        )
        messages.success(request, "Bid placed successfully!")
    return HttpResponseRedirect("listing", listing_id=listing.id)

def close_auction(request, listing_id):
    listing = Listing.objects.get(Listing, id=listing.id)
    if request.user == listing.owner:
        listing.active = False
        listing.save()
    return HttpResponseRedirect("listing", listing_id=listing.id)


def add_comment(request, listing_id):
    listing = Listing.objects.get(Listing, id=listing_id)
    text = request.POST["comment"]
    Comment.objects.create(
        listing=listing,
        user=request.user,
        text=text,
    )
    return HttpResponseRedirect("listing", listing_id=listing.id)


def index(request):
    active_listings = Listing.objects.filter(isActive=True)
    all_categories = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": active_listings,
        "categories": all_categories
    })


def display_categories(request):
    if request.method == "POST":
        category_form = request.POST['category']
        category = Category.objects.get(category_nm=category_form)
        active_listings = Listing.objects.filter(isActive=True, category=category)
        all_categories = Category.objects.all()
        return render(request, "auctions/index.html", {
            "listings": active_listings,
            "categories": all_categories,
    })



def create_listing(request):
     if request.method == "GET":
         get_categories = Category.objects.all()
         return render(request, "auctions/create.html", {
             "categories": get_categories
         })
     else:
         # Get the data from the form
         title = request.POST["title"]
         description = request.POST["description"]
         price = request.POST["price"]
         image_url = request.POST["image url"]
         category = request.POST["category"]
         user_in = request.user
         category_data = Category.objects.get(category_nm=category)

         # Create a new listing object
         user_listing = Listing(
             title=title,
             description=description,
             image_url=image_url,
             price=float(price),
             category=category_data,
             owner=user_in
         )
         # Inset the object in our database
         user_listing.save()
         # Redirect to index page
         return HttpResponseRedirect(reverse(index))



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")




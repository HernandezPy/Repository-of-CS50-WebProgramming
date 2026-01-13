from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category_nm = models.CharField(max_length=80)

    def __str__(self):
        return self.category_nm


class Listing(models.Model):
    title = models.CharField(max_length=30)
    created_listing = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=1200)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watch_list = models.ManyToManyField(User, blank=True, related_name="watchlist")

    def __str__(self):
        return self.title

    def current_price(self):
        highest = self.bids.order_by("-amount").first()
        return highest.amount if highest else self.starting_bid

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_by")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commented")
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watch")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watched")



class Create(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image_url = models.CharField(max_length=1000)


# customer360/views.py

from django.shortcuts import render, get_object_or_404, redirect
from datetime import date, timedelta
from django.db.models import Count
from .models import Customer, Interaction

# Define index view to display all customers
def index(request):
    customers = Customer.objects.all()  # Fetch all customers
    context = {"customers": customers}  # Context to pass to the template
    return render(request, "index.html", context=context)

# Define view to create a new customer
def create_customer(request):
    if request.method == "POST":
        # Retrieve data from the form
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "")
        social_media = request.POST.get("social_media", "")  # Optional field for social media

        # Create a new Customer object
        customer = Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            social_media=social_media,
        )
        customer.save()  # Save the new customer to the database

        msg = "Successfully Saved a Customer"  # Success message
        return render(request, "add.html", context={"msg": msg})  # Render the add.html template with the success message
    return render(request, "add.html")  # Render the add.html template for GET requests

# Define summary view to show interaction data
def summary(request):
    thirty_days_ago = date.today() - timedelta(days=30)  # Calculate the date 30 days ago
    interactions = Interaction.objects.filter(interaction_date__gte=thirty_days_ago)  # Fetch interactions from the last 30 days

    count = len(interactions)  # Count the number of interactions
    interactions = interactions.values("channel", "direction").annotate(count=Count('channel'))  # Group interactions by channel and direction
    context = {
        "interactions": interactions,
        "count": count,
    }
    return render(request, "summary.html", context=context)  # Render the summary.html template with interaction data

# Define interaction view to handle customer interactions
def interact(request, cid):
    channels = Interaction.CHANNEL_CHOICES  # Fetch available channels
    directions = Interaction.DIRECTION_CHOICES  # Fetch available directions
    context = {"channels": channels, "directions": directions}

    if request.method == "POST":
        # Fetch the selected customer
        customer = get_object_or_404(Customer, id=cid)
        channel = request.POST.get("channel", "")
        direction = request.POST.get("direction", "")
        summary = request.POST.get("summary", "")

        # Create a new Interaction object
        interaction = Interaction.objects.create(
            customer=customer,
            channel=channel,
            direction=direction,
            summary=summary
        )
        interaction.save()  # Save the interaction to the database
        context["msg"] = "Interaction Success"  # Success message
        return render(request, "interact.html", context=context)  # Render the interact.html template with the success message

    return render(request, "interact.html", context=context)  # Render the interact.html template for GET requests

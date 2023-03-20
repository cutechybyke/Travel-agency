from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):
  
  # dest1 = Destination()
  # dest1.offer = True
  # dest1.name = 'Mumbai'
  # dest1.desc = 'Our city is the best'
  # dest1.img = 'destination_1.jpg'
  # dest1.price = 750
  
  # dest2 = Destination()
  # dest2.name = 'Lagos'
  # dest2.desc = 'Our city is the One'
  # dest2.img = 'destination_2.jpg'
  # dest2.price = 850
  # dest2.offer = False
  
  # dest3 = Destination()
  # dest3.name = 'Owerre'
  # dest3.desc = 'Our city is the Greatest'
  # dest3.img = 'destination_3.jpg'
  # dest3.price = 800
  # dest3.offer = False
  
  # dest4 = Destination()
  # dest4.name = 'Awka'
  # dest4.desc = 'Our city is intentional'
  # dest4.img = 'destination_4.jpg'
  # dest4.price = 770
  # dest4.offer = False
  
  # dest5 = Destination()
  # dest5.name = 'Port-Harcourt'
  # dest5.desc = 'Our city is the Gorgeous'
  # dest5.img = 'destination_5.jpg'
  # dest5.price = 940
  # dest5.offer = True
  
  # dest6 = Destination()
  # dest6.name = 'Avu'
  # dest6.desc = 'Our city is Amazing'
  # dest6.img = 'destination_6.jpg'
  # dest6.price = 850
  # dest6.offer = False
  
  # dests = [dest1, dest2, dest3, dest4, dest5, dest6]
  dests = Destination.objects.all()
  
  return render(request, 'index.html', {'dests': dests});
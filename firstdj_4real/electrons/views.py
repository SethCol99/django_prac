from django.shortcuts import render

# Create your views here.
  
def fortune(request):
  return render(request, 'electrons/lil_rundown.html')
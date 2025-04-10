from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import PersonalGoldSource
from .forms import PersonalGoldSourceForm

def index(request):
    return render(request, 'index.html')

def pgs_new(request, pk=None):
    if pk:
        profile = get_object_or_404(PersonalGoldSource, pk=pk)
    else:
        profile = None

    if request.method == 'POST':
        form = PersonalGoldSourceForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = PersonalGoldSourceForm(instance=profile)

    return render(request, 'pgs_new.html', {'form': form})

def pgs_all(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        # Filter PGS Records by Name or Email (case-insensitive)
        profiles = PersonalGoldSource.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )
    else:
        # Show all PGS Records if no search query is provided
        profiles = PersonalGoldSource.objects.all()

    return render(request, 'pgs_all.html', {'profiles': profiles})


def pgs_delete(request, pk):
    # Get the profile by primary key (pk)
    profile = get_object_or_404(PersonalGoldSource, pk=pk)

    # Delete the profile
    profile.delete()

    # Add a success message (optional)
    messages.success(request, f"Personnel Gold Source record for '{profile.name}' has been deleted successfully.")

    # Redirect back to the list page
    return redirect('pgs_all')

#API to be used for PowerAutomate
def profiles_api(request):
    """
    API endpoint to fetch all profiles or filter them by name/email.
    """
    query = request.GET.get('q', '')  # Get the search query from the request
    if query:
        profiles = PersonalGoldSource.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )
    else:
        profiles = PersonalGoldSource.objects.all()

    # Serialize the data into a list of dictionaries
    profiles_data = list(profiles.values('id', 'name', 'email', 'employeeid', 'status'))
    return JsonResponse(profiles_data, safe=False)
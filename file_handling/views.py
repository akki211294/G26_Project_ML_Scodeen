from django.shortcuts import render, redirect
from .models import YourModel
from .forms import YourModelForm
from django.db.models.signals import post_save
from django.shortcuts import render

def your_model_upload(request):
    upload_success = False

    if request.method == 'POST':
        form = YourModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            # Set the upload_success variable to True
            upload_success = True

            # Redirect to a success page or handle as needed
            return redirect('success')  
    else:
        form = YourModelForm()

    return render(request, 'upload.html', {'form': form, 'upload_success': upload_success})

def success_view(request):
    return render(request, 'success.html')

def your_model_upload_redirect(request):
    return redirect('upload')



# Create your views here.
from django.shortcuts import render, redirect
from .models import UploadedImage
from .utils import detect_forgery  # We'll create this utility function later
import os

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        image_instance = UploadedImage(image=uploaded_image)
        image_instance.save()

        # Detect forgery
        image_path = image_instance.image.path
        is_forged, info = detect_forgery(image_path)

        return render(request, 'result.html', {
            'uploaded_image': image_instance,
            'is_forged': is_forged,
            'info': info,
        })
    return render(request, 'upload.html')
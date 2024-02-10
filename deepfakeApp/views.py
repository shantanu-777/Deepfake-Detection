# views.py

from django.shortcuts import render
from django.http import HttpResponse
from your_deepfake_detection_module import detect_deepfake

def index(request):
    result = None

    if request.method == 'POST':
        video_file = request.FILES.get('video')
        image_file = request.FILES.get('image')

        if video_file and image_file:
            # Call your deepfake detection function
            result = detect_deepfake(video_file, image_file)

    return render(request, 'index.html', {'result': result})

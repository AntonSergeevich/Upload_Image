from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ImageSerializer

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'upload/upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'upload/image_list.html', {'images': images})


@api_view(['POST'])
def upload_image_api(request):
    if request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
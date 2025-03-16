from django.shortcuts import render
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from  .models import *

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        face_image_data = request.POST.get('face_image')
        print(f'face_image_data: {face_image_data}')
        face_image_data=face_image_data.split(',')[1]
        
        face_image = ContentFile(base64.b64decode(face_image_data), name=f'{username}_.jpg')
        print(f'face_image: {face_image}')
        
        try:

            user = User.objects.create(username=username)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
        
        UserImage.objects.create(user=user, face_image=face_image)
        
        return JsonResponse({'success': True , 'message': 'Face registered successfully'})
        
    return render(request, 'register.html')
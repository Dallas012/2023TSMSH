from django.shortcuts import render
from . import models
from . import convert
from config import settings
# Create your views here.

def uploadFile(request):
    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['file']
        
        pdf = models.FileUpload(
            title = title,
            file = file
        )
        pdf.save()
        if 'Convert' in request.POST:
            file_name = str(request.FILES['file'])
            convert.requests_call(file_name)
            jsonFile = getJson(file_name)
            return render(request, 'Core/upload-file.html', context=
                          {
                              'Convert' : jsonFile
                          })
        
    
    return render(request, "Core/upload-file.html")  

def getJson(file_name):
    file_name = file_name.split('.')[0]
    file_path = settings.MEDIA_ROOT + '\\Result\\' + file_name + '.json'
    jsonFile = open(file_path, 'r', encoding='UTF-8')
    return jsonFile
    
    
# def convertFile(request):
#     if request.method == 'POST':
#         title = request.POST[]
# def showJson(request):
    
#     json = None
#     return render(request, "Core/showJson.html", context = {
#         'files' : json
#     })
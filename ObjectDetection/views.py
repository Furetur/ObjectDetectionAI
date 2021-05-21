from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from ObjectDetection.convert_images import decode_cv_image, encode_image_uri
from ObjectDetection.model.model import Model

model = Model()


class UploadImageForm(forms.Form):
    file = forms.FileField()


def index(request):
    if request.method == "GET":
        return render(request, "index.html", {"file_form": UploadImageForm()})
    elif request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = decode_cv_image(request.FILES["file"].read())
            new_img = model.process(img)
            return render(request, "result.html", {"input": encode_image_uri(img), "output": encode_image_uri(new_img)})
        else:
            return HttpResponse("Form invalid. Try again")

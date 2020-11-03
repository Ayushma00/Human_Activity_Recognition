from django.shortcuts import render
from django.http import HttpResponse
import pickle as pkl
import cv2
import numpy as np
import os
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
from keras.models import load_model
model=load_model(os.path.join(BASE_DIR,"test2.h5"))
with open(os.path.join(BASE_DIR,"OHE.pkl"),'rb') as f:
     ohe1 = pkl.load(f)
text=""
def index(request):
    return render(request, "main/index.html",{"text":text})

image_copy=np.zeros((80,80))
def get_frame(vidcap,seconds):

    global image_copy
    vidcap.set(cv2.CAP_PROP_POS_MSEC,seconds*1000)
    hasFrames,image = vidcap.read()
    px=80
    py=80
    if hasFrames:
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image1 = cv2.resize(np.uint8(gray),(px,py), interpolation = cv2.INTER_AREA)
        image_array = np.reshape(np.array(image1),(px,py))
        image_copy=image_array
    else:
        image_array=image_copy
    return hasFrames,image_array.astype("int")

def predict1(request):
    global text
    if request.method=="POST":
        blob=request.body
        f = open(os.path.join(BASE_DIR,"file.MP4"), 'wb')
        f.write(blob)
        f.close()
        lister=vidarray(os.path.join(BASE_DIR,"file.MP4"))
        X1=np.array(lister)
        X1=X1.reshape(-1,40,80,80,1)
        X1=X1/255
        pred=model.predict(X1)
        text1=ohe1.inverse_transform(np.round(pred))
        text=text1[0][0]
        return HttpResponse("good")

def vidarray(input):
    video_cap=cv2.VideoCapture(input)
    sec = 0
    sec1=0
    frameRate = 0.3
    count=1
    list2=[]
    success,_ = get_frame(video_cap,sec)
    while success:
        list1=[]
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        sec1 = sec1 + frameRate
        sec1 = round(sec1, 2)
        if sec<=12:
            success,img =get_frame(video_cap,sec1)
            list1.append(img)
            list2.append(list1)
            if success==0:
                sec1=0
                success=1
        else:
            success=0
    return list2

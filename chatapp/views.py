
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Conversation,suggestions
from django.db.models import Q
from chatapp.replyScript import (assistant,talkToMe)
from django.core import serializers
from django.shortcuts import  get_object_or_404
from rest_framework.views import APIView
#from .serializers import convoserializers
from rest_framework.response import Response
import json

# class convoList(APIView):
#     def get(self,request):
#         convo=Conversation.objects.all()
#         serializers=convoserializers(convo,many=True)
#         return Response(serializers.data)
#     def post(self,request):
#         convo=request.data
#         serializer=Conversation.objects.filter(medicine=convo)
#         return Response(serializer)

def images(request):
    imagedata=open("","rb").read()
    return HttpResponse(imagedata,content="image/png")
def Home(request):
    return render(request, "chatapp/Vaidya123.html")
def Index(request):
    return render(request,'chatapp/index.html')
def new(request):
    return render(request,'chatapp/Vaidya9876.html')

@csrf_exempt
def Post(request):
    if request.method == "POST":
        query = request.POST.get('msgbox', None)
        sugg=suggestions.objects.all()
        reply=sugg.filter(Q(input__icontains=query))
        #for m in reply:
        #    st=m
        try:
            st=reply[0]
            speak=talkToMe(str(st.output))
            return JsonResponse({'response':str(st.output),'sug1':str(st.sug1),'sug2':str(st.sug2),'sug3':str(st.sug3),'sug4':str(st.sug4),'query':query})
        except:
            speak=talkToMe("Sorry, I don't understand")
            return JsonResponse({'response':"Sorry, I don't understand",'query':query})

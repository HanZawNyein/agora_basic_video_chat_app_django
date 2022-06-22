import json
import os

from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
from .models import RoomMember
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
# Create your views here.
def lobby(request):
    return render(request, 'base/lobby.html')


def room(request):
    return render(request, 'base/room.html')


def getToken(request):
    appId = os.getenv("APPID")
    channelName = request.GET.get('channel')
    appCertificate = os.getenv("APP_CERTIFICATE")
    expirationTimeSeconds = 3600 * 24
    currentTimeStam = time.time()
    privilegeExpiredTs = currentTimeStam + expirationTimeSeconds
    role = 1
    uid = random.randint(1, 230)
    token = RtcTokenBuilder.buildTokenWithAccount(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token': token,'app_id':appId, 'uid': uid}, safe=False)

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member,create = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    return JsonResponse({"name":data['name']},safe=False)

def getMember(request):
    uid=request.GET.get('UID')
    room_name=request.GET.get('room_name')
    member= RoomMember.objects.get(
        uid=uid,
        room_name=room_name
    )
    name=member.name
    return JsonResponse({'name':member.name},safe=False)

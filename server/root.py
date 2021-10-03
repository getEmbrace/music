
import time
import json

import myHttp
import wyy

Wyy = wyy.Wyy()

path = "D:/HTML/vue/vueProject/music/server/dist"
IP = "192.168.0.100"
PORT = 8081

def index(params):

    with open(path + '/index.html', 'r') as f:
        data = f.read()
        
    response = myHttp.response({
        'body': data,
        'headers': {
            'Content-Type': 'text/html'
        }
    })
    return response

def getMusicList(params):
    bodys = json.loads(params.get('bodys'))
    songName = bodys.get('songName', '偏爱')
    data = []
    songDist = json.loads(Wyy.searchByName(songName)).get('result').get('songs')
    if(songDist):
        for i in songDist:
            #除去vip歌曲
            songUrl = Wyy.getSongUrl(i.get('id'))
            if(songUrl != "vip"):
                data.append({
                    "name": i.get('name'),
                    "id": i.get('id'),
                    "ar": i.get('ar')[0].get('name')
                })
    
    
    response = myHttp.response({
        'body': bytes(str(data), 'utf-8'),
        'headers': {
            'Content-Type': 'text/json'
        }
    })
    return response

def getSongPic(params):
    bodys = json.loads(params.get('bodys'))
    songId = bodys.get('songId', 1436709403)
    songPic = Wyy.getSongPic(songId)
    data = {
        "songPic": songPic
    }
    response = myHttp.response({
        'body': bytes(str(data), 'utf-8'),
        'headers': {
            'Content-Type': 'text/json'
        }
    })
    return response

def getSongWord(params):
    bodys = json.loads(params.get('bodys'))
    songId = bodys.get('songId', 1436709403)
    songWord = Wyy.getSongWord(songId)

    response = myHttp.response({
        'body': bytes(json.loads(songWord).get('lrc').get('lyric'), 'utf-8'),
        'headers': {
            'Content-Type': 'text/txt'
        }
    })
    return response

def getSongUrl(params):
    bodys = json.loads(params.get('bodys'))
    songId = bodys.get('songId', 1436709403)
    songUrl = Wyy.getSongUrl(songId)
    data = {
        "songUrl": songUrl
    }
    response = myHttp.response({
        'body': bytes(str(data), 'utf-8'),
        'headers': {
            'Content-Type': 'text/json'
        }
    })
    return response

routers = {
    '/': index,
    '/getMusicList': getMusicList,
    '/getSongPic': getSongPic,
    '/getSongWord': getSongWord,
    '/getSongUrl': getSongUrl,
}

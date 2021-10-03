from os import name
import requests
import re
import random
import math
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import json


class Wyy:
    def __init__(self) -> None:
        pass

    def getEncText(self, a, b):
        cryptor = AES.new(str(b).encode('utf-8'), AES.MODE_CBC,
                          '0102030405060708'.encode('utf-8'))
        encText = cryptor.encrypt(pad(str(a).encode('utf-8'), 16, 'pkcs7'))
        return str(base64.b64encode(encText), 'utf-8')

    def getEncSecKey(self, a, b, c):
        encSecKey = "73f984f9464e0675e2bb34ea7fc6f0f748f631aa950afbefb6f9705803775691f725d7a96d8b5f2544bea1a18d9b07fe8e2e13e576c4cdd5e80ba31c6b89798c90d6dd4b52469038036c06a3c391210ea048fcb294e28614928397fc03468e514cd6ffb296e027f599366796738e801a41a45f244e3a55e5243e288d2649ede3"
        return encSecKey

    def getParams(self, a):
        b = "010001"
        c = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        d = "0CoJUm6Qyw8W8jud"
        # 获取16位随机值iStr_0
        iStr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        iStr_0 = ''
        for i in range(16):
            random16 = math.floor(random.random() * len(iStr))
            iStr_0 += iStr[random16]
        iStr_0 = "xPiPrN5GPgl5uNoy"
        encText = self.getEncText(a, d)
        encText = self.getEncText(encText, iStr_0)
        encSecKey = self.getEncSecKey(iStr_0, b, c)
        return [encText, encSecKey]

    def searchByName(self, name):
        url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
        header = {
            "Origin": "https://music.163.com",
            "Referer": "https://music.163.com/search/",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
        }
        a = "{\"hlpretag\":\"<span class=\\\"s-fc7\\\">\",\"hlposttag\":\"</span>\",\"s\":\"" + name + "\",\"type\":\"1\",\"offset\":\"0\",\"total\":\"true\",\"limit\":\"10\",\"csrf_token\":\"\"}"
        data = self.getParams(a)
        params = {
            "params": data[0],
            "encSecKey": data[1]
        }
        res = requests.post(url, headers=header, params=params)
        res.encoding = res.apparent_encoding
        return res.text

    def getSongPic(self, songId):
        #获取图片
        url = "https://music.163.com/song?id={}".format(songId)
        header = {
            "Host": "music.163.com",
            "Referer": "https://music.163.com/",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
        }
        res = requests.get(url, headers=header)
        res.encoding = res.apparent_encoding
        image = re.search(r'"images": \["(.*?)"\],', res.text[0: 4000]).groups()[0]
        return image

    def getSongWord(self, songId):
        #获取歌词
        url = "https://music.163.com/weapi/song/lyric?csrf_token="
        header = {
            "Host": "music.163.com",
            "Origin": "https://music.163.com",
            "Referer": "https://music.163.com/song?id={}".format(songId),
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
        }
        a = "{\"id\":\"" + str(songId) + "\",\"lv\":-1,\"tv\":-1,\"csrf_token\":\"\"}"
        data = self.getParams(a)
        params = {
            "params": data[0],
            "encSecKey": data[1]
        }
        res = requests.post(url, headers=header, params=params)
        res.encoding = res.apparent_encoding
        songWord = res.text
        return songWord
    
    def getSongUrl(self, songId):
        #获取歌曲mp3
        url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
        header = {
            "Host": "music.163.com",
            "Origin": "https://music.163.com",
            "Referer": "https://music.163.com/",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
        }
        a = "{\"ids\":\"[" + str(songId) + "]\",\"level\":\"standard\",\"encodeType\":\"aac\",\"csrf_token\":\"\"}"
        data = self.getParams(a)
        params = {
            "params": data[0],
            "encSecKey": data[1]
        }
        res = requests.post(url, headers=header, params=params)
        res.encoding = res.apparent_encoding
        try:
            songUrl = re.search(r'"url":"(.*?)"', res.text).groups()[0]
        except:
            songUrl = 'vip'
        return songUrl
    
if __name__ == "__main__":
    wyy = Wyy()
    songList = wyy.searchByName("偏爱")
    print(songList)
    # songInfo = wyy.getSongRecourse(5238992)
    # print(songInfo)
    # getData()
    # getParams()

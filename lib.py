from googletrans import Translator
import os
import requests

def cn2en(source):
	translator = Translator(service_urls=['translate.google.cn'])
	text = translator.translate(source,src='zh-cn',dest='en').text
	return text

def en2cn(source):
	translator = Translator(service_urls=['translate.google.cn'])
	text = translator.translate(source,src='en',dest='zh-cn').text
	return text

def makeGrass(text,times=10):
	for i in range(times):
		print(str(int(i/times*100))+"%")
		text=en2cn(cn2en(text))
	return text

def getAudio(text):
	url="https://tts.baidu.com/text2audio?tex="+text+"&cuid=baike&lan=ZH&ctp=1&pdt=301&vol=9&rate=32&per=2&&spd=3"
	# url="http://tts.baidu.com/text2audio?lan=zh&pid=100&ie=UTF-8&text="+text+"&spd=3"
	r=requests.get(url=url,stream=True)
	f = open("audio.mp3", "wb")
	for chunk in r.iter_content():
		if chunk:
			f.write(chunk)
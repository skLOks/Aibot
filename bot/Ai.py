import pyaudio
import wave
import sys
from time import sleep
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
import speech_recognition as sr
import webbrowser as wb
import random



cmd = {
	'name': ["ай", "хошино", "аюш", "аечка", "хош", "хоши"],
	'cmd': ["включи", "открой", "сделай", "выполни"]
}

def enumname(str1):
	for i in cmd['name']:
		if fuzz.ratio(str1, i) >= 50:
			str1 = i
	return str1

def enum(key, com):
	sl = com.split(" ")
	for i in range(len(cmd[key])):
		for g in sl:
			if comparison(cmd[key][i], g.lower())  == 1:
				return 1
	else:
		return 0

def delstr(com, key):
	e = com.split()
	for i in range(len(e)):
		if enum(key, e[i].lower()) == 1:
			com = com.replace(e[i], '')
			if com[0] == ' ':
				com = com.replace(" ", '', 1)
			return com
	else:
		return com

def comparison(str1, str2):
	try:
		assert fuzz.ratio(str1, str2) >= 70
		return 1
	except:
		return 0

def delsimv(com):
	simv = "!-#~`@$%^&*()_=+/.,\"?''{}№;:|\\"
	for i in simv:
		com = com.replace(i, '')
	return com

def randsound():
	r = random.randint(1, 3)
	if r == 1:
		return "sounds/хорошо.wav"
	elif r == 2:
		return "sounds/хорошо2.wav"
	elif r == 3:
		return "sounds/я поняла.wav"

def play(file):
	CHUNK = 1024
	wf = wave.open(file, 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True)
	data = wf.readframes(CHUNK)
	while len(data) > 0:
	    stream.write(data)
	    data = wf.readframes(CHUNK)
	stream.stop_stream()
	stream.close()
	p.terminate()

def rec(time):
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		print("Говорите...")
		audio = r.listen(source, time, time)
	try:
		text = r.recognize_google(audio, language="ru")
		print("Вы сказали: " + text)
		return text
	except sr.UnknownValueError:
		print("Извините, не удалось распознать речь.")
	except sr.RequestError as e:
		print("Ошибка сервиса распознавания речи; {0}".format(e))
	

def processing(stroka, key):
	stroka = delsimv(stroka)
	stroka = delstr(stroka, key)
	return stroka

def sleepf():
	while True:
		try:
			request = rec(1)
			for i in cmd['name']:
				if fuzz.ratio(request, i) >= 50:
					request = i
					print(request)
					break
			
			if enum('name', request) == 1:
				play("sounds/ага.wav")
				main()
				break
		except:
			print("Странная ошибка")

def main():
	while True:
		try:
			inp = input()
			# inp = rec(3)
			request = inp
			request = processing(request, 'name')
			request = processing(request, 'cmd')
			print(request)

			if comparison(request.lower(), "youtube") == 1:
				play(randsound())
				wb.open("https://www.youtube.com")
			if comparison(request.lower(), "привет") == 1:
				play("sounds/я Ай.wav")
			if comparison(request.lower(), "как говорит роналду") == 1:
				play("sii.wav")
			if comparison(request.lower(), "стоп"):
				play("sounds/да пока.wav")
				break
			if comparison(request.lower(), "музыка") == 1:
				play(randsound())
				os.startfile('"C:/Users/huawei matebook d14/AppData/Local/Programs/YandexMusic/YM.exe"')
			if comparison(request.lower(), "моя любимая музыка") == 1:
				play(randsound())
				wb.open("https://music.yandex.ru/users/r3mbog/playlists")
			if comparison(request.lower(), "ошибка") == 1:
				a = 4 / 0

			if comparison(request.lower(), "Днс") == 1:
				wb.open("https://www.dns-shop.ru")

		except:
			sleep(0.5)
			play("sounds/да пока.wav")
			sleepf()
			break

if __name__	== '__main__':
	main()
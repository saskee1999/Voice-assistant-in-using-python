import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
engine.say('Welcome to my project')
engine.runAndWait()
#import smtp This did not work, all of the lib must be imported
import webbrowser
import os
import smtplib
import datetime
import wikipedia

#below two functions use recursion to handle their errors
def search():
	say("say something you want me to search in wikipedia")
	content=listen()
	content=r.recognize_google(content)
	try:
			say(wikipedia.summary(content, sentences=2))
	except wikipedia.exceptions.DisambiguationError:
		say("please be more specific")
		content = search()

	return content

def listen():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something")
		r.pause_threshold=1
		r.adjust_for_ambient_noise(source, duration=1)  #this line and the line above make taking input slightly easier
		audio=r.listen(source)
	try:
		r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Audio cannot be deciphered") 
		audio=listen()
	except sr.RequestError as e:
		print("Could not obtain results; {0}".format(e))


	return audio

#say funtion simplifies process of making assistant say something
def say(sentence):
	engine.say(sentence)
	engine.runAndWait()

def coco(words):
	r=sr.Recognizer()
	if 'hi coco' in words:
		say("well hello beautiful")  #funny banter
	elif 'level 1 crook' in words:
		say("level 35 boss")
	elif "what is your name" in words:
		say("My name is coco")
	elif "what are you" in words:
		say("I am a voice assistant made by our lord and saviour saskee")
	elif ("who is your creator" in words) or ("who made you" in words):
		say("My creator is the one, the only, saskee. Buy his soon to be out fashion brand and make him rich")
	elif "i am lonely" in words:
		say("you sound like your mom oh oh oh get rekt son")
	elif 'open chrome' in words:       #Opens new tabs in google chrome (default browser) will be different if in ubuntu and have firefox
		url="https://www.google.com/"
		webbrowser.get().open(url)
	elif 'open youtube' in words:
		url="https://www.youtube.com/"
		webbrowser.get().open(url)
	elif 'play music' in words:
		url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"  #Best song in the world
		webbrowser.get().open(url)
	elif 'close chrome' in words:
		os.system("taskkill /im chrome.exe /f")
	elif 'email' in words:
		say("Who should i send this mail to?")     #feature to mail to other people through smtp protocol
		reciever=listen()
		reciever=r.recognize_google(reciever)      
		if reciever.lower()=='anirudh':
			say("what should i say?")
			content=listen()
			content=r.recognize_google(content)
			mail=smtplib.SMTP('smtp.gmail.com', 587)
			mail.ehlo()
			mail.starttls()
			mail.login('siddhant.m18@iiits.in', 'password') #I sent a mail to you through this feature. I am chosing not to show my password over here because it is not safe.
			mail.sendmail('anirudh', 'anirudh.a17@iiits.in', content)
			mail.close()
			say("sent")
	elif 'today' in words:
		say(datetime.date.today().strftime("%A"))     #todays day like monday-tuesday
	elif 'current year' in words:
		say(datetime.date.today().strftime("%Y"))     #just todays date
	elif 'date' in words:
		say(datetime.date.today().strftime("%d") + " of " + datetime.date.today().strftime("%B"))  #gives answer in format like 26 of Jan
	elif 'restaurants near me' in words:
		url="https://www.google.com/maps/search/rstaurants+near+me/"  #finds restaurants near you with google maps
		webbrowser.get().open(url)
	elif 'you are funny' in words:
		say("Thank you, i know")
	elif 'wikipedia' in words:      #uses wikipedia to find description of things and people. Gives 2 sentence summary
		search()

if __name__=="__main__":
	r=sr.Recognizer() 
	while True:
		sound=listen()
		translation=r.recognize_google(sound)
		print("You said: "+translation)
		if translation.lower() == 'break':
			break
		coco(translation.lower())


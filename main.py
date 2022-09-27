from secrets import choice
import speech_recognition as speech 
import pyttsx3 as engine 
import wikipedia as wiki 
import webbrowser as browse 
import serial 
import os 
import time 
 
# a function to speak 
Speak = engine.init() 
 
 
# speak and print function 
def speak(text): 
print(text) 
Speak.say(text) 
Speak.runAndWait() 
 
 
# function for greeting and from here the program starts 
def greetings(): 
current_time = time.localtime() 
current_time = int(time.strftime("%H", current_time)) 
if current_time > 6 or current_time < 12: 
speak("Good Morning.") 
elif current_time >= 12 or current_time < 18: 
speak("Good Afternoon") 
else: 
speak("Good Evening") 
 
speak("Can I Help You?") 
 
 
# function for converting voice to text 
def VoiceToSpeech(): 
with speech.Microphone() as Voice: 
print("Listening") 
# Listening to the Voice 
audio = speech.Recognizer().listen(Voice) 
print("Recognizing") 
try: 
# recognizing the voice to text 
text = speech.Recognizer().recognize_google(audio, language='en-in') 
print("you said:", text) 
return str(text).lower() 
except Exception as e: 
print(e) 
return "try again" 
 
 
# function to open google chrome 
def chrome(): 
speak("opening google chrome") 
browse.open("https://www.google.com/") 
 
 
# function to search in google chrome 
def search(text): 
speak("Searching for " + text) 
browse.open("https://www.google.com/search?q=" + text) 
 
 
# function to open youtube 
def youtube(text): 
speak("Opening youtube for " + text) 
browse.open("https://www.youtube.com/search?q=" + text) 
 
 
# function to open music 
def music(): 
speak("Which Music Do you want to play?") 
song = VoiceToSpeech() 
path = "C:\\Users\\Sample Music" # path for the music directory 
all_songs = os.listdir(path) # getting list of songs in directory 
try: 
for songs in all_songs: 
if song in songs.lower(): # match the song you needed and plays it 
os.startfile(os.path.join(path, songs)) 
break 
else: 
speak("Music Not Found") 
except Exception as e: 
print(e) 
 
 
# function to open wiki pedia 
def wiki_pedia(text): 
speak("Searching on Wiki pedia") 
wiki_result = wiki.summary(text, sentences=1) 
speak(wiki_result) 
 
 
# function to save a note 
def note(): 
speak("what do you want to save in note?") 
note_text = VoiceToSpeech() 
note_name = str(round(time.monotonic())) + ".txt" 
with open(note_name, 'w') as file: 
file.write(note_text) 
print("File Saved Successfully") 
speak("Do you want to open note?") 
print("Yes or No...!") 
command = VoiceToSpeech() 
if command == "yes": 
os.startfile(note_name) 
 
 
# function to open facebook 
def facebook(text): 
speak("Opening Facebook") 
browse.open("https://www.facebook.com/search/top/?q=" + text) 
 
 
# function to open instagram 
def instagram(text): 
speak("Opening Instagram") 
browse.open("https://www.instagram.com/" + text) 
 

 
greetings() 
while True: 
choice = VoiceToSpeech() 
if "open google" in choice: 
chrome() 
elif "what" in choice: 
search(choice) 
elif "wikipedia" in choice: 
choice = choice.replace("wikipedia", "") 
wiki_pedia(choice) 
elif "youtube" in choice: 
choice = choice.replace("youtube", "") 
youtube(choice) 
elif "music" in choice: 
choice = choice.replace("music", "") 
music() 
elif "write note" in choice: 
choice = choice.replace("write note", "") 
note() 
elif "facebook" in choice: 
choice = choice.replace("facebook", "") 
facebook(choice) 
elif "instagram" in choice: 
choice = choice.replace("instagram", "") 
instagram(choice) 
elif "controls" in choice: 
arduino() 
elif "bye" in choice: 
print("Bye")
break
else:
    speak(choice)
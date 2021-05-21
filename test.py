# Python program to translate
# speech to text and text to speech
from chatterbot import ChatBot
bot=ChatBot('chotu')
from chatterbot.trainers import ChatterBotCorpusTrainer
bot.set_trainer(ChatterBotCorpusTrainer)

# un-comment this if you are running this for the first time
# bot.train('chatterbot.corpus.english')

import speech_recognition as sr
import pyttsx3 
  
  
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
      
      
  
while(1):    
    r = sr.Recognizer() 
      
    try:
          
        with sr.Microphone() as source2:
              
            r.adjust_for_ambient_noise(source2, duration=0.1)
              
            audio2 = r.listen(source2)
              
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            if MyText=='bye' or MyText=='goodbye':
                SpeakText("Nice talking to you .. bye bye")
            
                break
            
            reply=bot.get_response(MyText)
            print("You: {}".format(MyText))

            print("bot: {}".format(reply))
            SpeakText(str(reply))
            
              
          
    except:
        print("unknown error occured")
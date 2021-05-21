from tkinter import *
from chatterbot import ChatBot
import speech_recognition as sr
import pyttsx3 
bot=ChatBot('chotu')
from chatterbot.trainers import ChatterBotCorpusTrainer
# un-comment this if you are running this for the first time
# bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train('chatterbot.corpus.english')

engine = pyttsx3.init()

def SpeakText(command):
    engine.say(command) 
    engine.runAndWait()
    
def bottalk():
    r = sr.Recognizer() 

    try:
        
        with sr.Microphone() as source:
            
            r.adjust_for_ambient_noise(source, duration=0.1)
            
            audio = r.listen(source)
            
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            if MyText=='bye' or MyText=='goodbye':
                SpeakText("Nice talking to you .. bye bye")
            
                root.destroy()
                return 0
            T.insert(END, "you :{} \n".format(MyText))
                
            reply=bot.get_response(MyText)
            print("You: {}".format(MyText))
            T.insert(END, "bot :{}\n".format(reply))


            print("bot: {}".format(reply))
            SpeakText(str(reply))
            T.see(END)

            
            
        
    except:
        T.insert(END, "bot : sorry .. try again\n")
        SpeakText("Sorry please try again")
    

root = Tk()
  
root.geometry("500x400")
  
# T = Text(root, height = 5, width = 52)
  
from tkinter import scrolledtext
l = Label(root, text = "TalkBot")
l.config(font =("Courier", 14))
  
T = scrolledtext.ScrolledText(root, 
                                    wrap = WORD, 
                                    width = 40, 
                                    height = 10, 
                                    font = ("Times New Roman",
                                            15))
  
b1 = Button(root, text = "click here ",command=bottalk )
  
b2 = Button(root, text = "Exit",
            command = root.destroy) 
  
l.pack()
T.pack()
b1.pack()
b2.pack()
  
  
mainloop()
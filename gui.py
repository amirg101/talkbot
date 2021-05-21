from tkinter import *
from chatterbot import ChatBot
import speech_recognition as sr
import pyttsx3 
bot=ChatBot('chotu')
from chatterbot.trainers import ChatterBotCorpusTrainer
# un-comment these lines if you are running the script for the first time
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
from PIL import Image, ImageTk
root.geometry("600x500")
  
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

photo=PhotoImage(file="mic1.png")


b1 = Button(root, text="Speak",font=("Times New Roman",20),image=photo,command=bottalk,height=50, width=170,compound=LEFT )
  
b2 = Button(root, text = "Exit",font=("Times New Roman",17),
            command = root.destroy)
  
l.pack(pady=25)
T.pack()
b1.pack(pady=20)
b2.pack()
  
  
mainloop()
# from PIL import Image
# image = Image.open('mic.png')
# new_image = image.resize((50, 50))
# new_image.save('mic1.png')

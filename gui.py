from tkinter import *
'''
Library : chatterbot
class: chatbot
'''
from chatterbot import ChatBot
import speech_recognition as sr
import pyttsx3 
'''
Load the data & load the algorithm => load the library
-Load the alogrithm /Trainer
    ChatterBotCorpusTrainer
        Library:chatterbot
        module:trainers
        class:ChatterBotCorpusTrainer
'''
bot=ChatBot('chotu')
from chatterbot.trainers import ChatterBotCorpusTrainer
'''
set the trainer ;
class:ChatBot
    function:set_trainer(Name_of_the_trainer)
    
and train the chatbot on the corpus data
    class :ChatBot
    function:train
'''
# un-comment these lines if you are running the script for the first time
# bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train('chatterbot.corpus.english')

engine = pyttsx3.init()

# Function to convert text to speech
def SpeakText(command):
    engine.say(command) 
    engine.runAndWait()
    
def bottalk():
    
    # Initialize the recognizer 
    r = sr.Recognizer() 
    # Exception handling to handle
    # exceptions at the runtime
    try:
        '''
        interaction part
            chatbot should prompt for a message from user(i/p msg)
            if the msg is 'bye' =>Terminate msging /bot action
            if msg is somethin else=>get proper response

        Class : ChatBot
        function : get_response(MESSAGE)
        '''
        with sr.Microphone() as source:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.1)
            #listens for the user's input
            audio = r.listen(source)
            # Using google to recognize audio
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            # stop the script if user says 'bye' or 'goodbye'
            if MyText=='bye' or MyText=='goodbye':
                # SpeakText("string") to convert text("string") to speech
                SpeakText("Nice talking to you .. bye bye")
                # close the tkinter window
                root.destroy()
                return 0
            T.insert(END, "you :{} \n".format(MyText))
            #get reply from the bot
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

# 'speak' button which when pressed will listen to the user and get reply from the bot
b1 = Button(root, text="Speak",font=("Times New Roman",20),image=photo,command=bottalk,height=50, width=170,compound=LEFT )
#exit button to close the tkinter window
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

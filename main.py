import pyjokes
import pyttsx3
import speech_recognition as sr
# import datetime
import wikipedia
import webbrowser
import time
import pywhatkit as pw
from translate import Translator
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Ross is listening.....!")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Ross is Recognizing......!")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Thank You ")

def txspeech(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(x)
    engine.runAndWait()
txspeech("Loading your personal voice assistant , ross")
txspeech("So, How can i help you")

if __name__=='__main__':
    # if "start running" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if ("who are you") in data1:
                name = "i am ross, your personal voice assistant"
                txspeech(name)
            elif "abhi" in data1:
                pw.search("who is abhi success")
                txspeech("Abhi Success , Founder and CEO , Ne-Ent Tech Developer")
            # elif "right now" in data1:
            #     time = datetime.datetime.now().strftime("%I%M%p")
            #     txspeech(time)
            elif "founder" in data1:
                foun = "team alpha developers creats me"
                txspeech(foun)
            elif "search" in data1:
                txspeech("Entering , into the mode of search console")
                txspeech("Kindly wait")
                while True:
                    abgh = wikipedia.summary(sptext(), sentences=2)
                    txspeech(abgh)
                    time.sleep(4)
                    if "exit" in abgh:
                        txspeech("Successfully , Exited from search console mode")
                        txspeech("Please, wait")
                        txspeech("Entering, into the Normal mode")
                        break
            elif "time" in data1:
                pw.search("time right now")
            elif "youtube" in data1:
                yout = "opening youtube"
                txspeech(yout)
                webbrowser.open("www.youtube.com/")
            elif "joke" in data1:
                jokess = pyjokes.get_jokes(language="en", category="neutral")
                print(jokess)
                txspeech(jokess)
            elif "favourite song" in data1:
                fav = "i know my team favourite song , wait i am opening"
                fav1 = "playing dandelions by ruth b on youtube"
                txspeech(fav)
                txspeech(fav1)
                webbrowser.open("https://youtu.be/fXbfBUNJ9mY")
            elif "made" in data1:
                ma = "abhi success, created me for helping you all people"
                txspeech(ma)
            elif "gmail" in data1:
                gma = "opening gmail"
                txspeech(gma)
                webbrowser.open("https://mail.google.com/mail/")
            elif "birth date" in data1:
                bd =  "hahahaha, i was created on march 2023, now calculate my present age ,i know you are genius in mathematics"
                txspeech(bd)
            elif "song for me" in data1:
                sfm = "well, i don't know your favourite song but still i am trying"
                sfm1 = "i can open music player for you , here you can play your favourite song"
                sfm2 = "opening player"
                txspeech(sfm)
                txspeech(sfm1)
                txspeech(sfm2)
                webbrowser.open("www.gaana.com/")
            elif "girlfriend" in data1:
                gf = "well i like alexa ,more over siri and google assistant"
                txspeech(gf)
            elif "eat" in data1:
                e = "well, i eat 100 of mb, and some part of your phone battery , hahahaha"
                txspeech(e)
            elif "date" in data1:
                d = "well, don't tell anyone , its alexa"
                txspeech(d)
            elif "calendar" in data1:
                cd = "opening calender on google"
                txspeech(cd)
                webbrowser.open("https://www.google.com/calendar")
            elif "alarm" in data1:
                al = "opening alarm on google"
                txspeech(al)
                webbrowser.open("https://support.google.com/clock/answer/2840926?hl=en")
            elif "youtube" in data1:
                txspeech("opening youtube")
                webbrowser.open("https://www.youtube.com/")
            elif "alpha" in data1:
                pk="team alpha developers consists of following members"
                pk1 ="Abhi Success , Pranav Mehta , piyush kumar , Fahim ul haq , harshit soni"
                pk2 = "we believe , that we can transform the technology"
                txspeech(pk)
                txspeech(pk1)
                txspeech(pk2)
            elif "english" in data1:
                txspeech("Successfully opened , kindly write your query")
                translator = Translator(to_lang="Hindi")
                translation = translator.translate(input("Enter the text in english to translate : "))
                print(translation)
            elif "between two" in data1:
                txspeech("Successfully opened , kindly write your query")
                translator1 = Translator(from_lang="german",to_lang="spanish")
                translation1 = translator1.translate(input("Enter the text in Germen to translate : "))
                print(translation1)

            elif "stop" in data1:
                txspeech("Thank you , for using ross personal voice assistant")
                break
            time.sleep(6)
    # else:
    #     print("Sorry, i couldn't get your voice")
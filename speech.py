import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser
import wikipedia

engine = pyttsx3.init()
a=engine.getProperty('voices')
b=engine.getProperty('rate')
c=engine.getProperty('volume')

g_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',g_id)
engine.setProperty('rate',100)

def convert(s):  
    new = ""  
    for x in s: 
        new += x  
        new +=" "  
    return new 

while(1):
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        audio = r.listen(source,phrase_time_limit=5,timeout=3)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        k="Hello"
        k= r.recognize_google(audio,language='en-IN')
        print("Recognizing....")
        k=k.lower()
        if(k=="how are you"):
            k="i am fine thankyou"
        elif(k=="what is your name"or k=="who are you"):
            k="my name is zaira,i am an actor"
        elif(k=="what do you like"):
            k="i like cooking"
        elif(k=="where do you live"):
            k="with you,in you,on the earth"
        elif(k=="who created you"or k=="who is your creator"):
            k="Ojas created me" 
        elif(k=="hello"):
            k="hello nice to see you"
        elif(k=="are you engaged"):
            k="yes"       
        elif(k=="who is your boyfriend"):
            k="Motu akash samant"     
        elif(k=="shutdown" or k== "end"):
            break 
        else:
            query=list(k.split()) 
            print(query)
            if "google" in query:
                webbrowser.open_new('www.facebook.com')
            elif "facebook" in query :
                webbrowser.open_new('www.facebook.com') 
            elif "gmail" in query:
                webbrowser.open_new('www.gmail.com')
            elif "search" in query:
                p=query.index("search")
                query=query[p+1:len(query)]
                string=convert(query)
                webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % string)
            elif "wikipedia" in query:
                print("hello")
                p=query.index("wikipedia")
                query=query[p+1:len(query)]
                string=convert(query)
                k=wikipedia.search("Barack")
                k=wikipedia.summary(string, sentences=1)


            #print(query)
    except sr.UnknownValueError:
        k="Could not understand audio"
    except sr.RequestError as e:
        k="Could not request results from Google Speech Recognition service; {0}".format(e)

    print(k)
    engine.say(k)
    engine.runAndWait()




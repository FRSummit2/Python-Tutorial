import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    # engine.say('What can I do for you')
    # engine.say('Hey swaytom, you are not permitted here')
    engine.runAndWait()

def talk_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                talk(command)
                # command = command.replace('hey', '')
                print (command)
    except:
        pass
    return command

def run_alexa():
    # talk('Arif')
    # talk('sir')
    # talk('chole')
    # talk('gese')
    talk('Atik kono kaz kore naa')
    # talk('Arif sir akta')
    # rate = engine.getProperty('rate')  # getting details of current speaking rate
    # print (rate)  # printing current voice rate
    # engine.setProperty('rate', 125)
    # talk('My current speaking rate is ' + str(rate))
    # command = talk_command()
    # print(command)
    # talk(command)
    # if 'play' in command:
    #     talk('playing')
    #     print('playing')

run_alexa()



# Installed Libraries
# ----------------------------------
# pip install SpeechRecognition
# pip install pyttsx3
# pip install PyAudio
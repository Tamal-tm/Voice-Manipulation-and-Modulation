# pip install googletrans==3.1.0a0 or pip install deep-translator
# pip install SpeechRecognition
# pip install PyAudio

from deep_translator import GoogleTranslator # Text converter
import speech_recognition as sr # Voice recoginition through source
import gtts # Text to Speech
import playsound # Plays the sound. 

# input_lang="hi" | Instead of language="hi"
# output_lang="en" | Instead of language="en"

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now...")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language="hi")
    print("You said (Hindi):", text)

translation = GoogleTranslator(source='hi', target='en').translate(text)
print("Translation (English):", translation)

converted_audio = gtts.gTTS(translation, lang="en")
converted_audio.save("Voice_translate.mp3")
playsound.playsound("Voice_translate.mp3")

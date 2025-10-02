import gtts
import playsound

text=input("Enter something here: ")

sound=gtts.gTTS(text, lang="en") # fr for french, hi for hindi. 

sound.save("Text_to_Speech.mp3")
playsound.playsound("Text_to_Speech.mp3")

# pip install gtts
# pip install playsound==1.2.2

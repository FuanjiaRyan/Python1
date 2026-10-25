from gtts import gTTS

text = "Willis is a poo poo boy, Aminkeng is a pee pee boy  and Maicon is a fat buttocks boy"
tts = gTTS(text=text, lang='en')

tts.save("output.mp3")

print("Audio file saved as output.mp3")
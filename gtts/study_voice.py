from gtts import gTTS

print("================================")
print("        STUDYVOICE")
print("   Turn your notes into audio")
print("================================")

text = input("\nPaste your study notes here:\n\n")

if text.strip():
    tts = gTTS(text=text, lang="en")
    tts.save("study_lesson.mp3")

    print("\nAudio generated successfully!")
    print("Saved as: study_lesson.mp3")
else:
    print("\nPlease enter some text.")
from pypdf import PdfReader
from gtts import gTTS

print("================================")
print("        STUDYVOICE")
print("   PDF TO AUDIO")
print("================================")

pdf_path = input("\nEnter the PDF file path: ")

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

if not text.strip():
    print("\nNo readable text was found in the PDF.")
    exit()

print("\nPDF text extracted successfully!")

# Split the text into smaller chunks
chunk_size = 4000

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

print(f"\nText split into {len(chunks)} parts.")

# Generate audio for each chunk
for i, chunk in enumerate(chunks):

    print(f"\nGenerating audio part {i + 1} of {len(chunks)}...")

    tts = gTTS(text=chunk, lang="en")

    filename = f"study_lesson_{i + 1}.mp3"

    tts.save(filename)

    print(f"Saved: {filename}")

print("\n================================")
print("Audio generation completed!")
print("================================")
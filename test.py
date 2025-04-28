from google import genai

client = genai.Client(api_key="AIzaSyAALehML5GdQAU6ed-ADJ82qOGBidt1wT4")

myfile = client.files.upload(file="/home/linuxer77/Downloads/vid.mp4")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)

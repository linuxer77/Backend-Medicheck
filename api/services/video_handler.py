from google import genai
from google.genai import types
import time
from pathlib import Path

class VideoHandler():
    client = genai.Client(api_key="AIzaSyAALehML5GdQAU6ed-ADJ82qOGBidt1wT4")
    current_dir = Path(__file__).resolve()
    parent_dir = current_dir.parents[2]

    def Response(self, videoName):
        #         video_file_name = f"/home/linuxer77/Programs/Hackathon-Project/Disease-bullshit/media/videos/{videoName}"
        # video_bytes = open(video_file_name, 'rb').read()
        myfile = self.client.files.upload(file=f"{self.parent_dir}/media/videos/{videoName}")

        time.sleep(2)
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=[myfile, "Summarize this video."]
        )

        return response.text
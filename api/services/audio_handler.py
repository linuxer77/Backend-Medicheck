from google import genai

class AudioHandler:
    client = genai.Client(api_key="AIzaSyAALehML5GdQAU6ed-ADJ82qOGBidt1wT4")

    def llmResponse(self, audio_file_name):
        myfile = self.client.files.upload(file=f"/home/linuxer77/Programs/Hackathon-Project/Disease-bullshit/media/audio_files/{audio_file_name}")

        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=['''Analyze the provided audio clip, and list potential corresponding diseases or significant abnormalities based on the user symptons.
                **Output Instructions:**
                - List potential conditions ONLY.
                - Separate each potential condition with a comma OR with spaces each.
                - Do NOT include any introductory text, greeting, explanation, confidence score, disclaimer (like "I am not a medical professional" or "This is not a diagnosis"), or concluding remarks.
                - If no significant abnormalities are detected based on visual patterns, output only the phrase: "No significant abnormalities detected based on visual patterns"

                **Your output must contain *only* the list of potential conditions or the single phrase indicating no abnormalities found.**''', myfile]
        )

        return response.text
from google.genai import types
from google import genai


class PossibleDisease:
    client = genai.Client(api_key="AIzaSyAALehML5GdQAU6ed-ADJ82qOGBidt1wT4")
    def getDisease(self, imgName):
        with open(f'/home/linuxer77/Programs/Hackathon-Project/Disease-bullshit/media/uploads/{imgName}', 'rb') as f:
            self.img_bytes = f.read()

        response = self.client.models.generate_content(
            model='gemini-2.5-flash-preview-04-17',
            contents=[
                types.Part.from_bytes(
                data=self.img_bytes,
                mime_type='image/jpeg',
                ),
                '''Analyze the provided chest X-ray image. Based SOLELY on the visual patterns you detect, list potential corresponding diseases or significant abnormalities.
                **Output Instructions:**
                - List potential conditions ONLY.
                - Separate each potential condition with a comma OR with spaces each.
                - Do NOT include any introductory text, greeting, explanation, confidence score, disclaimer (like "I am not a medical professional" or "This is not a diagnosis"), or concluding remarks.
                - If no significant abnormalities are detected based on visual patterns, output only the phrase: "No significant abnormalities detected based on visual patterns"
                For example: responding only with text  "Gastroenteritis, Influenza, Food poisoning" for a certain condition.
                For each, each disease:
                1 Common name (avoid jargon)
                2. Estimated likelihood as a percentage (must sum to 100 %)
                3. One-sentence “why it might fit”
                **Your output must contain *only* the list of potential conditions or the single phrase indicating no abnormalities found.
                **'''
                ]
        )

        return response.text


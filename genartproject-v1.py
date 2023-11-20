import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '<redacted>'


genes = [
    {"ID": 1, "Votes": None, "Style": "Op Art", "Theme": "Underwater Realm", "Setting": "Desolate Wasteland", "ArtType": "Abstract", "HexColorCode": "#800080", "CreativeMedium": None, "Perspective": "Three-Point Perspective"},
    {"ID": 2, "Votes": None, "Style": "Realism", "Theme": "Cyber Dreams", "Setting": "Futuristic Metropolis", "ArtType": "Figurative", "HexColorCode": "#008B8B", "CreativeMedium": "Acrylics", "Perspective": "Reverse Angle"},
    {"ID": 3, "Votes": None, "Style": "Fauvism", "Theme": "Historical Intrigue", "Setting": None, "ArtType": "Figurative", "HexColorCode": "#000000", "CreativeMedium": "Collage Art", "Perspective": "Linear Perspective"},
]

prompts = []


for row in genes:

  # Constructing the prompt for each row

  prompt = f"Create an image of {row.get('ArtType', 'Unknown')} art. Create it in the {row.get('Style', 'Unknown')} style, using the medium of {row.get('CreativeMedium', 'Unknown')}, centered around a theme of {row.get('Theme', 'Unknown')}. The background color should be {row.get('HexColorCode', 'Unknown')}. Create the image from the perspective of {row.get('Perspective', 'Unknown')}.  If relevant for the artType, set the setting as {row['Setting']}."

  prompts.append(prompt)
# end of loop

# row = next(item for item in genes if item["ID"] == 10)

# PROMPT = f"Create an image of {row['ArtType']} art, using the values from row id=10 as variables in the prompt. Create it in the {row['Style']} style, using the medium of {row['CreativeMedium']}, centered around a theme of {row['Theme']}. The background color should be {row['HexColorCode']}. Create the image from the perspective of {row['Perspective']}. If relevant for the artType, set the setting as {row['Setting']}."


for index, row in enumerate(genes):
    PROMPT = prompts[index]

    response = openai.Image.create(
        model="dall-e-3",
        prompt=PROMPT,
        n=1,
        size="1024x1024",
    )
    print(PROMPT)
    print(response["data"][0]["url"])
# end of loop

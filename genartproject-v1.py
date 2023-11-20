import os
import openai

# represent traits of the art as genes
# change the genes into a prompt
# send the propmpt to DALLE to render
# do this for every member of the population

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '<redacted>'

# create a dictionary structure with all the members of the population

genes = [
    {"ID": 1, "Votes": None, "Style": "Op Art", "Theme": "Underwater Realm", "Setting": "Desolate Wasteland", "ArtType": "Abstract", "HexColorCode": "#800080", "CreativeMedium": None, "Perspective": "Three-Point Perspective"},
    {"ID": 2, "Votes": None, "Style": "Realism", "Theme": "Cyber Dreams", "Setting": "Futuristic Metropolis", "ArtType": "Figurative", "HexColorCode": "#008B8B", "CreativeMedium": "Acrylics", "Perspective": "Reverse Angle"},
    {"ID": 3, "Votes": None, "Style": "Fauvism", "Theme": "Historical Intrigue", "Setting": None, "ArtType": "Figurative", "HexColorCode": "#000000", "CreativeMedium": "Collage Art", "Perspective": "Linear Perspective"},
]

# create a dictionary for the prompts

prompts = []

# convert the genes into a prompt for each member of the population

for row in genes:

  # Constructing the prompt for each row

  prompt = f"Create an image of {row.get('ArtType', 'Unknown')} art. Create it in the {row.get('Style', 'Unknown')} style, using the medium of {row.get('CreativeMedium', 'Unknown')}, centered around a theme of {row.get('Theme', 'Unknown')}. The background color should be {row.get('HexColorCode', 'Unknown')}. Create the image from the perspective of {row.get('Perspective', 'Unknown')}.  If relevant for the artType, set the setting as {row['Setting']}."

  prompts.append(prompt)
# end of loop


# go through each member of the population and send the prompt to DALLE
# print the prompt
# print the URL of the resulting render

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

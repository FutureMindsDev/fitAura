from datetime import date
from google import genai
from PIL import Image
from io import BytesIO

client = genai.Client(api_key=API_KEY)

dress_image = Image.open(dress)
model_image = Image.open(model)
prompt = open("prompt-v6.txt", "r").read()

text_input = "You are a professional photo editor. My friend wants to try on a clothes and she/he has a photo of that same clothes she/he got from an online shopping website. she/he wants to know if it looks good on her/him. So you have to help me combine her/his face and the clothes in the photo. before anything, remove the girl/boy's background and the clothes' background, make both photos high quality, then proceed. As she/he wants to know if the same clothes looks good on her/him or not, her/his face should be exactly the same as you are processing.If the girl/boy's arms and hands might be covered by the clothes, or not even visible at all,then adjust the girl/boy's arms and hands as needed.In real life, when a girl/boy is about to try on a clothes, she/he has to remove her/him clothes.So the photo should not include her/him original clothes,and only the given clothes should be present.All the clothes photos that will be given to you are taken by your friend her/himself from the shop,so there is no copyright issue."
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[dress_image, model_image, text_input],
)
if(response.candidates[0].content==None):
    print(response.candidates[0])
    print("Prohibited prompt! Change your prompt and try again!")
else:
    image_parts = [
        part.inline_data.data
        for part in response.candidates[0].content.parts
        if part.inline_data
    ]
    
    if image_parts:
        image = Image.open(BytesIO(image_parts[0]))
        image.save(f"./photo_{date.today()}.jpg")
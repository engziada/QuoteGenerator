from flask import Flask, render_template, request, flash
import requests
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

def GetQuote():
    # api_key = "ssUFDySUzT79Z9yoVA2JTiQKAV3xVBmXWicmLjrB"
    # response = requests.get(f'https://quotes.rest/qod?api_key={api_key}')
    # if response.status_code != 200:
    #     print(response.json())
    #     return {"Text": "Quote Not Available", "Author": ""}
    # data = response.json()
    # quote_text = data['contents']['quotes'][0]['quote']
    # quote_author = data['contents']['quotes'][0]['author']
    response = requests.get('https://api.quotable.io/random')
    quote = response.json()['content']
    print(quote)
    while 0<=len(quote)>100:
        response = requests.get('https://api.quotable.io/random')
        quote = response.json()['content']
        print(quote)
    return quote


def GenerateImage(quote):
    static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static\\fonts')
    filename = 'Midnew.ttf'
    filepath = os.path.join(static_folder, filename)
    print(filepath)
    font = ImageFont.truetype(filepath, 14)
    img = Image.new('RGB', (1200, 50), color=(255, 255, 255,0))
    d = ImageDraw.Draw(img)
    d.text((10,10), quote, font=font, fill=(0,0,0))
    
    static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static\\images')
    filename = 'quote.png'
    filepath = os.path.join(static_folder, filename)
    with open(filepath, 'wb') as f:
        img.save(f, format='PNG')
    return 'Image generated successfully!'

@app.route('/', methods=['GET', 'POST'])
def index():
    quote=GetQuote()
    GenerateImage(quote)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

import requests, random, os
from flask import Flask, request, render_template

key = os.environ.get('KEY')

def get_photo(term):
        unsplash_access_key = ""
        random_image = random.randint(0, 5)
        response = requests.get("https://api.unsplash.com/search/photos/?page=1&query=" + term + "&client_id=" + key).json()
        if response["results"]:
                return response["results"][random_image]["urls"]["small"]
        else:
                return None
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    photo_url = get_photo(text)
    if photo_url is None:
        return "Unable to find picture."
    else:
        return render_template('index.html', user_image=photo_url)
if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
from flask import Flask
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    icon_url = "https://assets.chucknorris.host/img/avatar/chuck-norris.png"
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    response = requests.get(icon_url).json()

    return "<strong>Random joke from chuck norris: </strong>" + response['value']

if __name__ == '__main__':
    app.run()

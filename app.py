from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mock_place')
def mock_place_response():
    PLACE_JSON = {
                    "candidates": [
                        {
                            "place_id": "ChIJFY7Y3xPwukARQ1bI5stEUYY"

                        }
                    ],
                    "status": "OK"
                }
    return PLACE_JSON

@app.route('/mock_place_details')
def mock_place_details_response():
    with open('/Users/claudiumilea/PycharmProjects/flask_test/place_details.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    app.run()

import flask
from flask import request, Flask, jsonify
import logging
from flask_cors import CORS
import os
import json


app = Flask(__name__)
CORS(app)
app = Flask(__name__)

@app.post("/samplewh")
def sample_wh():
  data = request.get_json()
  print(f"data {data}")
  output = {
    'sessionInfo': {
      'parameters': {
        'userAuthenticated': 'y',
        }
      },
    "fulfillment_response": {
      "messages": [
        {
          "text": {
            "text": ["test"]
            }
        },
        {
          "payload": {
            "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    { "text": "Option 1" },
                                    { "text": "Option 2" },
                                    { "text": "Option 3" }
                                ]
                            }
                        ]
                    ]

          }

        }
      ]
    }
  }
  response_json = json.dumps(output)
  return response_json
  # return flask.jsonify({"results": "output"})

@app.post("/nomatch")
def nomatch():
  # TODO: Aqui se implementa la lógica de la llamada a un motro de GenAI como Gemini
  # En caso de que GenAI determine que hay una probabilidad alta de que sea un intent existente
  # en Dialogflow se devolvería en el fullfillment del webhook.
  # Los intents tienen que tener route groups para poder ser llamados desde cualquier parte del flujo
  # Al estar en el sys no match está disponible en cualquier parte del flujo
  # Tanto el texto como los chips abajo estan hard codeados pero serían rellenados por la respuesta
  # de genai

  # TODO: También se puede forzar una transicion usando tarjet page/flow
  # https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/WebhookResponse


  data = request.get_json()
  print(f"data {data}")
  output = {
    'sessionInfo': {
      'parameters': {
        'userAuthenticated': 'y',
        }
      },
    "fulfillment_response": {
      "messages": [
        {
          "text": {
            "text": ["I understand that you  want to compare accounts. Click on the button if that is the case or type a new search."]
            }
        },
        {
          "payload": {
            "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    { "text": "I want to compare accounts" }

                                ]
                            }
                        ]
                    ]

          }

        }
      ]
    }
  }
  response_json = json.dumps(output)
  return response_json
  # return flask.jsonify({"results": "output"})

@app.post("/transition")
def transition():
  # TODO: Aqui se implementa la lógica de la llamada a un motro de GenAI como Gemini
  # En caso de que GenAI determine que hay una probabilidad alta de que sea un intent existente
  # en Dialogflow se devolvería en el fullfillment del webhook.
  # Los intents tienen que tener route groups para poder ser llamados desde cualquier parte del flujo
  # Al estar en el sys no match está disponible en cualquier parte del flujo
  # Tanto el texto como los chips abajo estan hard codeados pero serían rellenados por la respuesta
  # de genai

  # TODO: También se puede forzar una transicion usando tarjet page/flow
  # https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/WebhookResponse


  data = request.get_json()
  print(f"data {data}")
  output = {
    'sessionInfo': {
      'parameters': {
        'userAuthenticated': 'y',
        }
      },
    "targetFlow": "projects/hospitality-demo-361210/locations/global/agents/368a4676-716f-4bdc-95ba-ddd37099e110/flows/5b01c640-b802-4df6-a2cd-5041512f45e0",
    "fulfillment_response": {
      "messages": [
        {
          "text": {
            "text": ["I understand that you  want to compare credit cards. Click on the button if that is the case or type a new search."]
            }
        },
        {
          "payload": {
            "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    { "text": "I want to compare credit cards" }

                                ]
                            }
                        ]
                    ]

          }

        }
      ]
    }
  }
  response_json = json.dumps(output)
  return response_json
  # return flask.jsonify({"results": "output"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

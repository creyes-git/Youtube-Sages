import requests
import os
from dotenv import load_dotenv


load_dotenv()


voices_man = {"Mateo" : "79743797-2087-422f-8dc7-86f9efca85f1",
              "Francisco" : "34dbb662-8e98-413c-a1ef-1a3407675fe7",
              "Rigoberto" : "846fa30b-6e1a-49b9-b7df-6be47092a09a"}

voices_woman = {"Gabriela" : "01d23d18-2956-44b0-8888-e89d234b17b4",
                "Chaparrita" : "5c5ad5e7-1020-476b-8b91-fdcbe9cc313c",
                "Conchita" : "2deb3edf-b9d8-4d06-8db9-5742fb8a3cb2"}


def cartesia_text_to_speech(text : str, speed : float):

    response = requests.post(url = "https://api.cartesia.ai/tts/bytes",
                             headers = {
                                        "X-API-Key": os.getenv("CARTESIA_API_KEY"),
                                        "Cartesia-Version": "2024-06-10",
                                        "Content-Type": "application/json"
                                       },
                             json = {
                                     "model_id": "sonic",
                                     "transcript": text,
                                     "voice": {
                                               "mode": "id",
                                               "id": "79743797-2087-422f-8dc7-86f9efca85f1",
                                               "__experimental_controls": {
                                                                           "speed": speed,
                                                                           "emotion": []
                                                                          }
                                              },
                                     "output_format": {
                                                       "container": "mp3",
                                                       "bit_rate": 128000,
                                                       "sample_rate": 44100
                                                      },
                                     "language": "es"
                                    })


    return response
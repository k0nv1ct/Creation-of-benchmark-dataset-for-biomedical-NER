import json
import pandas as pd
import re
import requests
from google.oauth2 import service_account
import google.auth.transport.requests


def get_entities(row):
  # Add the token to the headers
  # Path to your service account key file
    KEY_FILE = '/content/numeric-ion-393603-0d0575605119.json'

    # Load the credentials from the service account key file
    creds = service_account.Credentials.from_service_account_file(
        KEY_FILE,
        scopes=['https://www.googleapis.com/auth/cloud-platform']
        )

    # Create an HTTP authorized client using the credentials
    auth_request = google.auth.transport.requests.Request()
    creds.refresh(auth_request)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer {}'.format(creds.token)
    }
    text = row
    # Replace 'your_text' with the text you want to analyze
    data = {
        'documentContent': text
    }
        # Specify the API endpoint URL
    your_project_id = 'numeric-ion-393603'
    your_location_id = 'us-central1'
    url = f"https://healthcare.googleapis.com/v1beta1/projects/{your_project_id}/locations/{your_location_id}/services/nlp:analyzeEntities"


    # Make a POST request to the API endpoint
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Get JSON response
    response_json = response.json()

    return response_json

def flatten_json(x):
  flattened_text = ''

  # Assuming you have already extracted the relevant data in the following lists
  mention_ids = []  # List to store mention IDs
  entity_types = []  # List to store entity types
  texts = []  # List to store texts

  for entity in x['entityMentions']:
      id = f"[id - {entity['mentionId']}]"
      entity_type = f"[entity-type = {entity['type']}]"
      text = f"[text = {entity['text']['content']}]"
      flat = entity_type+' '+text+ ' '
      flattened_text+=flat

      mention_ids.append(entity['mentionId'])
      entity_types.append(entity['type'])
      texts.append(entity['text']['content'])

  data = {
      'id': mention_ids,
      'entity_type': entity_types,
      'text': texts
  }

  # Create a DataFrame using the dictionary
  df = pd.DataFrame(data)

  linked_entity_id = []
  for entity in x['entityMentions']:
    if 'linkedEntities' in entity:
      id = entity['mentionId']
      text = entity['text']['content']
      linked_id = entity['linkedEntities']
      for ids in linked_id:
        linked_entity_id.append([id,text,ids['entityId']])

  linked_entities = []
  for ids in linked_entity_id:
    id = ids[0]
    entity_id = ids[2]
    text = ids[1]
    for entities in x['entities']:
      if entities['entityId'] == entity_id:
        term = entities['preferredTerm']
        linked_entities.append([id,text,term,entity_id])

  related_entities = []
  for relations in x['relationships']:
    related_entities.append([relations['subjectId'],relations['objectId']])

  relationship = []
  for ids in related_entities:
      id1 = ids[0]
      id2 = ids[1]
      text1 = None  # Initialize text1
      text2 = None  # Initialize text2
      for entity in x['entityMentions']:
          if entity['mentionId'] == str(id1):
              text1 = entity['text']['content']
          if entity['mentionId'] == str(id2):
              text2 = entity['text']['content']

      relationship.append([id1, text1, "related to", id2, text2])

  return flattened_text, df, linked_entities, relationship


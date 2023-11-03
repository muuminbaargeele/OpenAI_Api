import requests , uuid, json
# Add your subscription key and endpoint
subscription_key = "a062ff7dd68d47aabcff0de395fa44b0"
endpoint = "https://api.cognitive.microsofttranslator.com/"
 # Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "southafricanorth"
path = '/translate'
constructed_url = endpoint + path
params = {
    'api-version': '3.0',
    'from': 'so',
    'to': ['en']
}

constructed_url = endpoint + path

headers ={
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId' : str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
     'text': "Annaga hadda waxaa ku faxasan nahay inaan bandhiggaan ka soo qaygalno. Maxaa yeelay waa aynu ka faa'ideysanaynaa barnaamijkaan sida ugu macqulsan ugunna hufan."
 }]
request = requests.post( constructed_url, params=params, headers=headers, json=body)
response = request.json()
print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))




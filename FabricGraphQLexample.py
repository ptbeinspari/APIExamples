from azure.identity import InteractiveBrowserCredential
import requests
import json

# Acquire a token
import requests

# Retrieve these from keyvault
tenant_id = ''
client_id = ''
client_secret = ''
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
scope = 'https://api.fabric.microsoft.com/.default'  # Replace with your API scope

# Request body for token retrieval
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope
}

# Make the POST request to get the token
token_response = requests.post(token_url, data=token_data)
token_response.raise_for_status()  # Raise an error for bad status codes

# Extract the token from the response
token = token_response.json().get('access_token')

# Prepare headers
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

endpoint = 'https://3ed3b329e48d4c0694d7986c44f15346.z3e.graphql.fabric.microsoft.com/v1/workspaces/3ed3b329-e48d-4c06-94d7-986c44f15346/graphqlapis/d89558fd-05c1-4090-9b75-fa00b5977479/graphql'
query = """
    query {
  publicholidays 
  {
     items
     {
        countryOrRegion
        holidayName
        normalizeHolidayName
        isPaidTimeOff
        isPaidTimeOff
        countryRegionCode

     },
     endCursor
  }
} 
  
"""

variables = {

  }
  

# Issue GraphQL request
try:
    response = requests.post(endpoint, json={'query': query, 'variables': variables}, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data, indent=4))
except Exception as error:
    print(f"Query failed with error: {error}")

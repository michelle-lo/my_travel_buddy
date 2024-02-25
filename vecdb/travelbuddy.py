from astrapy.db import AstraDB

# Initialize the client
db = AstraDB(
  token="AstraCS:tznbrcmGHUAYZxRKOOzuYmnp:f503ff286d1beafb39d8f66105716bdf00804de59a787b94ce1649c988b9f3bf",
  api_endpoint="https://b3001bed-ac83-49d5-adfa-ff1c9faa8160-us-east-2.apps.astra.datastax.com")

print(f"Connected to Astra DB: {db.get_collections()}")
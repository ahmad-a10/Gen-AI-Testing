from openai import OpenAI

API_KEY = open("secret.txt").read()


client = OpenAI(
api_key=API_KEY
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);

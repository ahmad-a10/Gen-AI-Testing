from openai import OpenAI

API_KEY = open("secret.txt").read()


client = OpenAI(
api_key=API_KEY
)

prompt = input("enter your prompt: ")
response = client.responses.create(
  model="gpt-3.5-turbo",
  input=prompt,
  store=True,
)

print(response.output_text);

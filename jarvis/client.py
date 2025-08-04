from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ] 
)

print(completion.choices[0].message.content)
from openai import OpenAI

API_KEY = "private api key is inserted here"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

messages = [
    {"role": "user", "content": "Explain Saudi Arabia in 10 words"},
]

response = client.chat.completions.create(
    model="google/gemini-2.5-flash-lite",
    messages=messages,
    temperature=0.7,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stream=False,
)

first_reply = response.choices[0].message.content
print("### First Reply:\n", first_reply)

messages.append({"role": "assistant", "content": first_reply})

messages.append({"role": "user", "content": "What is the capital ?"}) 

second_response = client.chat.completions.create(
model="google/gemini-2.5-flash-lite",
messages=messages,
temperature=0.7,
max_tokens=150,
top_p=0.9,
frequency_penalty=0.0,
presence_penalty=0.0,
stream=False,
)

print("\n### Second Reply:\n", second_response.choices[0].message.content)

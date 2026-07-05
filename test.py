from openai import OpenAI

API_KEY = "private api key is inserted here"


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

messages = [
    {"role": "system", "content": "You are a helpful assistant in mathematics."},
    {"role": "user", "content": "List all prime numbers from 1 to 20."},
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

print(response.choices[0].message.content)

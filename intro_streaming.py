import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def chunk_handler(chunk):
    print(chunk, end='', flush=True)

def get_streaming_response(prompt, streaming_callback):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=2000,
        temperature=0.0,
        stream=True
    )

    for chunk in chat_completion:
        if chunk.choices[0].delta.content is not None:
            streaming_callback(chunk.choices[0].delta.content)

prompt = "Tell me a story about two puppies and two kittens who became best friends:"

get_streaming_response(prompt, chunk_handler)
print("\n")
# AI-Streaming-Text-Generator

This repository demonstrates how to use OpenAI's GPT-3.5-turbo model to generate text responses in real-time through **streaming**. The program streams AI-generated responses chunk by chunk as they are produced, providing immediate feedback instead of waiting for the entire response to be processed.

## Features

- **Real-time Streaming**: Get instant responses as text is generated.
- **Customizable Prompts**: Input your own prompts to generate AI responses.
- **Temperature Control**: Fine-tune the creativity of the response with adjustable temperature settings (set to `0.0` in this case for deterministic responses).
- **Chunk Handling**: Each chunk of the AI response is handled separately and streamed in real time for a smooth user experience.

## How Streaming Works

Instead of receiving the entire AI-generated text at once, **streaming** sends smaller parts (chunks) of the response as they are processed. This allows for faster initial feedback and can make long responses more interactive. In this program, the `stream=True` flag is used to enable streaming mode in OpenAI's API.

### Example:
If you prompt the model with:
```
Tell me a story about two puppies and two kittens who became best friends:
```
The response will begin to stream in as the model processes the story, chunk by chunk.

## Code Overview

### Environment Setup
The program loads the API key from environment variables using the `.env` file. Ensure you have a `.env` file with your OpenAI API key set up:
```
OPENAI_API_KEY=your-api-key-here
```

### Main Functionality
- **`get_streaming_response()`**: Sends the prompt to OpenAI's GPT-3.5-turbo model and streams the response in chunks.
- **`chunk_handler()`**: Handles each chunk of text as it arrives and prints it to the console.
- The example prompt: `"Tell me a story about two puppies and two kittens who became best friends."` is passed to the model, and the output is streamed as it is generated.

### Code Example
```python
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
```

## How to Run

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install openai python-dotenv
   ```
3. Set up a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
4. Run the program:
   ```bash
   python intro_streaming.py
   ```

You will see the response start printing in real-time as it is generated.

## Conclusion

This repository highlights the power of **streaming** in generating dynamic, real-time responses from OpenAI's GPT-3.5-turbo model. By streaming output in chunks, you can get immediate feedback, which is especially useful for long-form content or interactive applications.

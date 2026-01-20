import os
from dotenv import load_dotenv
from google import genai
from httpx import Response
import argparse
from google.genai import types

def main():

    # Load API key from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY NOT FOUND")
    
    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()
    # Now we can access `args.user_prompt` and `args.verbose`

    # Prepare the user prompt
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Generate content using the Gemini model
    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

    if not response.usage_metadata:
        raise RuntimeError("No usage metadata found in response")

    if args.verbose:        
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")    
    
    print(response.text)


if __name__ == "__main__":
    main()

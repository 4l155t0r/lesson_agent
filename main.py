import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

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
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt,),
        )

    if not response.usage_metadata:
        raise RuntimeError("No usage metadata found in response")

    if args.verbose:        
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")    

    function_results = []
    if response.function_calls:
        for function_call in response.function_calls:
            #print(f"Calling function: {function_call.name}({function_call.args})")
            function_call_result = call_function(function_call, verbose=args.verbose)
            if not function_call_result.parts:
                raise Exception("No parts found in function response")
            if not function_call_result.parts[0].function_response:
                raise Exception("No function response found in function response part") 
            if not function_call_result.parts[0].function_response.response:
                raise Exception("No response (content) found in function response part's function response")
            else:
                function_results.append(function_call_result.parts[0].function_response.response)
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()

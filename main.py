from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Initialize the OpenAI client
client = OpenAI()

def get_completion(prompt, model="gpt-5.2", temperature=0.7, max_output_tokens=500):
    """
    Helper function to get completions from OpenAI

    Parameters:
    - prompt: The input prompt
    - model: Model to use (default: gpt-5-mini)
    - temperature: Controls randomness (0=deterministic, 1=creative)
    - max_output_tokens: Maximum length of response
    """
    response = client.responses.create(
        model=model,
        input=[{"role": "user", "content": prompt}],
        # temperature=temperature,
        max_output_tokens=max_output_tokens
    )
    return response.output_text

# Test the setup
print(get_completion("Hello I am Aditya, How are you?"))
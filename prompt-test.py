
import jsonlines 
from openai import OpenAI

## Set up your OpenAI API key
client = OpenAI(
      api_key = 'your_openai_api_key'  # Replace 'your_openai_api_key' with your actual API key
)

# Define the prompt and model parameters

# prompt = "Can you recommend some educational toys for 5-year-olds?"
prompt = "Do you sell cars?"
# model = "gpt-3.5-turbo"
model = "your_model"  # Replace 'your_model' with your actual Model name
stop = ["\n", "Assistant:"]  # Specify stopping sequences

# Define a function to test the prompt with different temperature settings
def test_prompt(prompt, model, temperature):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Mellow is a friendly and helpful chatbot for retails clothing store for men and women."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=100,
        stop=stop
    )
    return response.choices[0].message.content


# Test the prompt with different temperature settings
temperature_settings = [0.1, 0.5, 0.9]

for temp in temperature_settings:
    print(f"\nTesting with temperature={temp}:")
    result = test_prompt(prompt, model, temp)
    print(result)

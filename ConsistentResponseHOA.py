import openai
import jsonlines

# Load your JSONL dataset
dataset_path = 'your_dataset.jsonl'  # Replace 'your_dataset.jsonl' with your actual dataset path
data = []
with jsonlines.open(dataset_path) as reader:
    for line in reader:
        data.append(line)

# Prepare your data in the format required by OpenAI
training_data = []
for item in data:
    prompt = item['messages'][1]['content']
    answer = item['messages'][2]['content']
    training_data.append({"prompt": prompt, "completion": answer})

# Set up your OpenAI API key
openai.api_key = 'your_openai_api_key'  # Replace 'your_openai_api_key' with your actual API key

# Fine-tune the GPT model
model = openai.FineTune.create(
    model="text-davinci-003",  # You can choose a different model if you prefer
    dataset=training_data,
    stop=["\n", "Assistant:"],  # Stop completion at newline or when Assistant starts speaking
    is_draft=True  # Set to True for testing; set to False when you're ready to deploy
)

# Retrieve the trained model ID
model_id = model['model']['id']

print("Model trained successfully! Model ID:", model_id)

def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response['choices'][0]['text']

# Test prompt-based queries
prompt = "Question: What types of clothing do you sell?"
print("Response:", get_response(prompt))

# Add more prompt-based queries to test

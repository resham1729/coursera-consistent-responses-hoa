import jsonlines 
from openai import OpenAI

# Set up your OpenAI API key
client = OpenAI(
      api_key = 'your_openai_api_key'  # Replace 'your_openai_api_key' with your actual API key
)

# Load your JSONL dataset
dataset_path = './Data/dataset1.jsonl'  # Replace 'your_dataset.jsonl' with your actual dataset path
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


client.files.create(
  file=open("./Data/dataset1.jsonl", "rb"),
  purpose="fine-tune"
)

# Create a fine-tuned model
client.fine_tuning.jobs.create(
  training_file=client.files.retrieve("file-RVD1Adlzyx9cuspClUOk6uVR"), 
  model="gpt-3.5-turbo"
)


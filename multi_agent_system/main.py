# main.py

import os
from agents.classifier_agent import ClassifierAgent
from memory.shared_memory import SharedMemory

# Initialize shared memory
memory = SharedMemory()

# Initialize classifier agent with memory
classifier = ClassifierAgent(memory=memory)

def load_input_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

if __name__ == "__main__":
    # Sample run for testing
    sample_files = [
        "samples/email_sample.txt",
        "samples/json_sample.json"
    ]

    for file_path in sample_files:
        print(f"\nProcessing file: {file_path}")
        content = load_input_file(file_path)
        classifier.process(content, file_path)

# memory/shared_memory.py

import time
import json

class SharedMemory:
    def __init__(self):
        self.memory = []

    def log(self, entry: dict):
        timestamped_entry = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            **entry
        }
        self.memory.append(timestamped_entry)
        print("[Memory] Logged Entry:")
        print(json.dumps(timestamped_entry, indent=2))

    def get_all(self):
        return self.memory

    def save_to_file(self, filepath="outputs/output_results.json"):
        with open(filepath, "w") as f:
            json.dump(self.memory, f, indent=2)
        print(f"[Memory] Memory persisted to {filepath}")

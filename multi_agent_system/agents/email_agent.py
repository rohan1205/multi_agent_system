# agents/email_agent.py

import re
from utils.llm_client import extract_email_metadata

class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def extract_sender(self, content: str) -> str:
        match = re.search(r"From:\s*(.*?@\S+)", content)
        return match.group(1).strip() if match else "unknown@example.com"

    def handle_email(self, content: str):
        sender = self.extract_sender(content)
        metadata = extract_email_metadata(content)

        result = {
            "sender": sender,
            "intent": metadata["intent"],
            "urgency": metadata["urgency"],
            "summary": metadata["summary"]
        }

        print("[EmailAgent] Processed Email:")
        print(result)

        self.memory.log({
            "agent": "EmailAgent",
            "sender": sender,
            "processed": result
        })

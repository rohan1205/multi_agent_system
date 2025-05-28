# agents/classifier_agent.py

import json
from agents.email_agent import EmailAgent
from agents.json_agent import JSONAgent
from utils.llm_client import classify_intent

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory
        self.email_agent = EmailAgent(memory)
        self.json_agent = JSONAgent(memory)

    def detect_format(self, content: str, filename: str) -> str:
        if filename.endswith(".json"):
            return "JSON"
        elif filename.endswith(".pdf"):
            return "PDF"
        elif "@gmail.com" in content or "Subject:" in content:
            return "Email"
        else:
            return "Unknown"

    def process(self, content: str, filename: str):
        format_type = self.detect_format(content, filename)
        intent = classify_intent(content)

        self.memory.log({
            "source": filename,
            "type": format_type,
            "intent": intent,
            "content": content
        })

        if format_type == "Email":
            self.email_agent.handle_email(content)
        elif format_type == "JSON":
            self.json_agent.handle_json(content)
        else:
            print(f"[ClassifierAgent] Unsupported format: {format_type}")

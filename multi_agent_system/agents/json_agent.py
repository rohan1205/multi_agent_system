# agents/json_agent.py

import json

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory
        self.required_fields = ["id", "timestamp", "payload"]

    def handle_json(self, content: str):
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            print("[JSONAgent] Error: Invalid JSON format.")
            self.memory.log({
                "agent": "JSONAgent",
                "error": "Invalid JSON format",
                "raw": content
            })
            return

        missing_fields = [field for field in self.required_fields if field not in data]

        reformatted = {
            "id": data.get("id", "MISSING"),
            "timestamp": data.get("timestamp", "MISSING"),
            "payload": data.get("payload", {}),
            "missing_fields": missing_fields
        }

        print("[JSONAgent] Processed JSON:")
        print(reformatted)

        self.memory.log({
            "agent": "JSONAgent",
            "processed": reformatted
        })

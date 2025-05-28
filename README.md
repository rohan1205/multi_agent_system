Multi-Agent AI System

A modular AI system that accepts input in PDF, JSON, or Email (text) format, classifies the format and intent, routes it to the appropriate agent, and logs key data into shared memory for chaining and traceability.


Objective

Build a multi-agent AI system with:

 Classifier Agent – Classifies format and intent, then routes input
 JSON Agent – Extracts data from structured JSON files
 Email Agent – Extracts sender, urgency, and intent from emails
 Shared Memory – Stores log of all actions and extractions



📁 Folder Structure

multi_agent_system/
│
├── agents/
│ ├── classifier_agent.py
│ ├── email_agent.py
│ └── json_agent.py
│
├── memory/
│ └── memory.py
│
├── utils/
│ └── llm_client.py
│
├── samples/
│ ├── email_sample.txt
│ ├── json_sample.json
│ └── pdf_sample.pdf
│
├── main.py





🧠 Agent Descriptions

1. Classifier Agent
- Accepts raw input file (text, JSON, PDF)
- Classifies format and intent (e.g., RFQ, Complaint)
- Routes to the correct agent
- Logs activity to shared memory

2. JSON Agent
- Processes structured JSON payloads
- Extracts values into target schema
- Flags anomalies or missing fields

3. Email Agent
- Extracts sender, subject, urgency
- Outputs in CRM-compatible format

4. Shared Memory
- Stores: type, source, timestamp, extracted values
- Enables traceability and chaining
- Implemented with lightweight in-memory store


Install Requirements
pip install -r requirements.txt

Run the System

python main.py samples/email_sample.txt
Try replacing the sample file with your own .json, .txt, or .pdf.

🧪 Sample Output (Shared Memory)
json
Copy
Edit
{
  "timestamp": "2025-05-28 21:26:04",
  "source": "samples/email_sample.txt",
  "type": "Email",
  "intent": "general_inquiry",
  "sender": "procurement@clientco.com",
  "urgency": "medium",
  "content": "From: procurement@clientco.com\nSubject: Request for Quotation\n..."
}
🧪 Mock Mode (No API Needed)
If you don’t want to use a credit card or API key, the system uses mocked LLM responses for:

Intent classification

Email field extraction

Just run the code—no API access required!

📦 Sample Input Files
Sample files are located in the samples/ folder:

email_sample.txt – Sample email content
json_sample.json – Sample structured JSON




📜 License
MIT License or educational use.

🤝 Credits
Built by Rohan Yadav for modular AI systems project focused on real-world intelligent file processing.


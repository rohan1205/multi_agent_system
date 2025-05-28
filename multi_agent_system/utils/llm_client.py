def classify_intent(text):
    print("[MOCK] classify_intent called.")
    # Example mock logic — you can change based on sample input
    if "invoice" in text.lower():
        return "process_invoice"
    elif "meeting" in text.lower():
        return "extract_meeting_info"
    else:
        return "general_inquiry"

def extract_email_metadata(text):
    print("[MOCK] extract_email_metadata called.")
    return {
        "sender": "john.doe@example.com",
        "receiver": "jane.smith@example.com",
        "subject": "Project Update",
        "body_summary": "Summary: The project is on track and will be completed by next week."
    }

def extract_json_data(text):
    print("[MOCK] extract_json_data called.")
    return {
        "key1": "value1",
        "key2": "value2"
    }

def summarize_pdf(text):
    print("[MOCK] summarize_pdf called.")
    return "This PDF contains an overview of quarterly earnings, key metrics, and projections for the next fiscal year."
# utils/llm_client.py



def extract_email_metadata(text):
    print("[MOCK] extract_email_metadata called.")
    return {
        "sender": "procurement@clientco.com",
        "receiver": "sales@yourcompany.com",
        "subject": "Request for Quotation",
        "body_summary": "Client requesting a quote for 200 units of part #X92 to be delivered by June 1.",
        "intent": "general_inquiry",
        "urgency": "medium"  # <-- Add this line
    }

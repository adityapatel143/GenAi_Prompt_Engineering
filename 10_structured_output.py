from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI()

def structured_json_extraction():
    """
    Example: Extract customer data in strict JSON format

    📖 STORY CONTEXT - Day 13 (Feb 23, 2026):
    Extract Aditya's complete case data into structured JSON for system integration.
    """

    customer_text = """
    Case resolved successfully. Customer Aditya Patel, phone 555-0199,
    email aditya.p@techcorp.com. Order #SM-2026-12345 placed on Feb 10, 2026.
    Items: Gaming laptop ($1,299), 2x wireless mouse ($49.99 each), RGB keyboard ($89.99).
    Original total after 10% discount: $1,348.57 including shipping.

    Issue: Both mouse units had clicking defects - buttons didn't register properly.
    Reported Feb 16. Customer remained polite throughout. Resolution: Expedited
    replacement mice sent Feb 20, arrived Feb 21. Customer satisfied with outcome.

    Customer is first-time buyer. High satisfaction now after resolution.
    Expressed interest in gaming headset for future purchase.
    """

    prompt = f"""
    Extract information and output ONLY valid JSON, no other text.

    Text:{customer_text}

    Required JSON schema:
{{
        "customer":{{
            "name": "string",
            "email": "string",
            "phone": "string",
            "lifetime_value": number,
            "total_orders": number
}},
        "order":{{
            "order_id": "string",
            "date": "YYYY-MM-DD",
            "items": [
{{
                    "product": "string",
                    "quantity": number,
                    "unit_price": number
}}
            ],
            "total_amount": number
}},
        "issue":{{
            "description": "string",
            "category": "string",
            "sentiment": "positive|neutral|negative",
            "resolution_requested": ["string"]
}}
}}

    Output ONLY the JSON:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.1  # Very low for consistency
    )

    json_output = response.output_text
    print("Structured JSON Output:\n" + "="*50)
    print(json_output)

    # Validate it's actually valid JSON
    try:
        parsed = json.loads(json_output)
        print("\n✅ Valid JSON - Successfully parsed")
        print(f"Customer:{parsed['customer']['name']}")
        print(f"Order Total: ${parsed['order']['total_amount']}")
    except json.JSONDecodeError:
        print("\n❌ Invalid JSON")

    print("\n" + "="*50 + "\n")

def structured_table_output():
    """
    Example: Generate data in table format

    📖 STORY CONTEXT - Day 13 (continued):
    Generate timeline table of Aditya's case for documentation.
    """

    prompt = """
    Create a timeline of Aditya Patel's case (Order #SM-2026-12345) in Markdown table format.

    Include these events:
    - Order placed (Feb 10)
    - Delivery (Feb 15)
    - Issue reported (Feb 16)
    - Case prioritized (Feb 19)
    - Resolution started (Feb 20)
    - Replacement delivered (Feb 21)
    - Confirmation received (Feb 22)

    Output as a Markdown table with these exact columns:
    | Date | Event | Status | Agent/Action | Customer Sentiment |

    Output ONLY the table, no other text.
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    table_output = response.output_text
    print("Structured Table Output:\n" + "="*50)
    print(table_output)
    print("\n" + "="*50 + "\n")

def structured_enum_classification():
    """
    Example: Force output to be from predefined options
    """

    customer_messages = [
        "I want to return my order, it's defective",
        "When will my package arrive?",
        "How do I reset my password?",
        "Your service is terrible! I want a refund!",
        "Do you have this in blue color?"
    ]

    prompt_template = """
    Classify this customer message into EXACTLY ONE of these categories:

    ORDER_STATUS
    PRODUCT_RETURN
    TECHNICAL_SUPPORT
    ACCOUNT_MANAGEMENT
    PRODUCT_INQUIRY
    BILLING_ISSUE
    COMPLAINT

    Customer message: "{message}"

    Respond with ONLY the category name, nothing else.
    Category:
    """

    print("Structured Enum Classification:\n" + "="*50)

    for msg in customer_messages:
        response = client.responses.create(
            model="gpt-5.2",
            input=[{"role": "user", "content": prompt_template.format(message=msg)}],
            temperature=0.0  # Deterministic
        )

        category = response.output_text.strip()
        print(f"Message:\"{msg[:50]}...\"")
        print(f"Category:{category}\n")

    print("="*50 + "\n")

def structured_with_schema_validation():
    """
    Example: Complex structured output with validation rules
    """

    prompt = """
    Generate a customer service ticket for this scenario:
    "Customer bought a laptop, screen is flickering, needs urgent replacement"

    Output as JSON following this schema:

    {
        "ticket_id": "string (format: TKT-XXXXXX where X is digit)",
        "created_at": "ISO 8601 datetime",
        "priority": "enum: LOW | MEDIUM | HIGH | CRITICAL",
        "category": "string",
        "subcategory": "string",
        "customer": {
            "id": "string",
            "tier": "enum: BASIC | SILVER | GOLD | PLATINUM"
        },
        "issue": {
            "title": "string (max 100 chars)",
            "description": "string",
            "product_affected": "string",
            "impact": "enum: MINOR | MODERATE | MAJOR | CRITICAL"
        },
        "sla": {
            "response_time_hours": number,
            "resolution_time_hours": number
        },
        "assignment": {
            "team": "string",
            "agent_id": "string or null"
        },
        "tags": ["string"],
        "requires_escalation": boolean
    }

    Generate realistic data. Output ONLY valid JSON.
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    ticket = response.output_text
    print("Complex Structured Ticket:\n" + "="*50)
    print(ticket)

    # Validate
    try:
        parsed = json.loads(ticket)
        print("\n✅ Valid JSON Structure")

        # Additional validation
        valid_priorities = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        if parsed["priority"] in valid_priorities:
            print(f"✅ Priority '{parsed['priority']}' is valid")

        if "TKT-" in parsed["ticket_id"]:
            print(f"✅ Ticket ID format is correct:{parsed['ticket_id']}")

    except Exception as e:
        print(f"\n❌ Validation failed:{e}")

    print("\n" + "="*50 + "\n")

def structured_csv_output():
    """
    Example: Generate CSV format
    """

    prompt = """
    Generate 5 sample customer records in CSV format.

    Columns (in order): CustomerID, Name, Email, TotalOrders, LifetimeValue, Status

    Rules:
    - CustomerID: format CUST-XXXXX
    - LifetimeValue: number without $ symbol
    - Status: ACTIVE or INACTIVE
    - Include header row
    - Values with commas must be quoted

    Output ONLY the CSV, no other text:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    csv_output = response.output_text
    print("Structured CSV Output:\n" + "="*50)
    print(csv_output)
    print("\n" + "="*50 + "\n")

# Run all examples
if __name__ == "__main__":
    # structured_json_extraction()
    structured_table_output()
    structured_enum_classification()
    structured_with_schema_validation()
    structured_csv_output()
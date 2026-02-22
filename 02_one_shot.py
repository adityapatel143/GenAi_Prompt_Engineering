from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def one_shot_example():
    """
    Example: Email response generation with one example

    📖 STORY CONTEXT - Day 5 (Feb 15, 2026):
    Good news! Aditya's package (order #SM-2026-12345) has arrived. He sends
    a confirmation message. We need to respond professionally and ask about
    product satisfaction.
    """

    # Customer inquiry
    customer_message = """
    Package for order #SM-2026-12345 delivered today. 
    Gaming laptop, mouse, and keyboard all accounted for. - Aditya Patel
    """

    # One shot prompt
    prompt = f"""
    Generate a professional customer service email response based on the inquiry.

    Example:
    Inquiry: "Hi, just wanted to confirm my order #98765 arrived safely today. Thanks!"
    Response: "Dear Valued Customer,

    Thank you for confirming the safe arrival of order #98765! We're delighted your package reached you on time.

    We hope the products meet your expectations. If you have any questions or concerns about the items, please don't hesitate to reach out. We're here to help!

    We'd also appreciate it if you could share your feedback when you get a chance.

    Best regards,
    Customer Support Team"

    ---

    Now generate a response for this inquiry:
    Inquiry: {customer_message}

    Response:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    print("One-Shot Email Response:")
    print(response.output_text)
    print("\n" + "="*50 + "\n")

# Example 2: JSON formatting
def one_shot_json_format():
    """
    Extract customer data in specific JSON format with one example

    📖 STORY CONTEXT - Day 5 (continued):
    We need to extract and store Aditya's customer information in our system.
    """

     # Customer inquiry
    customer_message = """
    Aditya Patel here, reach me at aditya.p@techcorp.com or 555-0199,
    regarding order #SM-2026-12345, everything arrived safely today and interested in basic support.
    """

    prompt = """
    Extract customer information and format it as JSON.

    Example:
    Text: "Hi, I'm John Smith, email john@email.com, phone 555-0123, order #98765, interested in premium support"
    JSON: {
        "name": "John Smith",
        "email": "john@email.com",
        "phone": "555-0123",
        "order_id": "98765",
        "interest": "premium support"
    }

    ---

    Now extract from this text:
    """ + f"""
    Text: {customer_message}
    JSON:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    print("One-Shot JSON Extraction:")
    print(response.output_text)

# Run examples
if __name__ == "__main__":
    #one_shot_example()
     one_shot_json_format()
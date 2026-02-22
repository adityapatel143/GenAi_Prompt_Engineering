from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def few_shot_classification():
    """
    Example: Multi-category classification with priority levels

    📖 STORY CONTEXT - Day 6 (Feb 16, 2026):
    Aditya has been testing his new equipment. He discovered that both wireless
    mice have button clicking issues. He reaches out to report the problem.
    """

     # Customer inquiry
    customer_message = """
    Hi, this is Aditya Patel (Order #SM-2026-12345). 
    Both wireless mice I received have clicking issues - the buttons don't register clicks properly. 
    The laptop and keyboard work perfectly though.
    """

    prompt = f"""
    Classify customer inquiries by category and priority level.

    Examples:

    Inquiry: "My credit card was charged twice for order #111"
    Category: Billing Issue
    Priority: HIGH
    Reason: Financial impact, requires immediate attention

    Inquiry: "What are the dimensions of the wireless mouse?"
    Category: Product Question
    Priority: LOW
    Reason: General information request, no urgency

    Inquiry: "My laptop won't turn on after the update"
    Category: Technical Support
    Priority: HIGH
    Reason: Product unusable, immediate assistance needed

    Inquiry: "Do you ship to Canada?"
    Category: Shipping Question
    Priority: LOW
    Reason: Pre-purchase inquiry, not time-sensitive

    ---

    Now classify this inquiry:
    Inquiry: {customer_message}
    Category:
    Priority:
    Reason:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    print("Few-Shot Classification:")
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def few_shot_response_generation():
    """
    Example: Generate responses in specific tone and structure

    📖 STORY CONTEXT - Day 6 (continued):
    Generate an empathetic response to Aditya about his defective mice.
    """

    customer_message = """
    Both wireless mice from my order #SM-2026-12345 have clicking issues. 
    Buttons don't register properly.
    """

    prompt = f"""
    Generate customer service responses following these examples:

    Example 1:
    Type: Apology for delay
    Input: "My order is late"
    Output: "We sincerely apologize for the delay in your order delivery. This isn't the experience we want for you. I'm personally looking into this and will ensure expedited shipping at no extra cost. ETA: 24 hours. Thank you for your patience."

    Example 2:
    Type: Product issue resolution
    Input: "The item is damaged"
    Output: "I'm truly sorry your item arrived damaged. That's completely unacceptable. Here's what I'll do: (1) Send a replacement via express shipping today, (2) You keep the damaged item - no return needed, (3) Apply a 15% discount to your account. You should receive your replacement within 2 days."

    Example 3:
    Type: Feature request
    Input: "Can you add dark mode?"
    Output: "Thank you for this excellent suggestion! Dark mode is definitely on our radar. I've forwarded your request to our product team with a +1. While I can't promise a timeline, we do prioritize features based on customer feedback. I'll add you to our update list!"

    ---

    Now generate a response:
    Type: Product defect acknowledgment
    Input: {customer_message}
    Output:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    print("Few-Shot Response Generation:")
    print(response.output_text)

# Example 3: Complex data extraction
def few_shot_data_extraction():
    """
    Extract structured information from unstructured text

    📖 STORY CONTEXT - Day 6 (continued):
    Extract and structure Aditya's feedback about order #SM-2026-12345 for our quality database.
    """

    customer_message = """
    Order #SM-2026-12345 from Aditya Patel - The gaming laptop is amazing,
    keyboard feels premium with great RGB lighting!
    However, BOTH wireless mice have defective clicking buttons. Very disappointed with mice quality.
    """

    prompt = """
    Extract customer feedback data in structured format.

    Example 1:
    Feedback: "Great laptop! Fast delivery. But the charger cable is too short."
    {
        "product": "laptop",
        "positive_aspects": ["performance", "fast delivery"],
        "negative_aspects": ["charger cable length"],
        "overall_sentiment": "positive",
        "action_required": "review charger cable design"
    }

    Example 2:
    Feedback: "Mouse is okay, nothing special. Arrived a week late and packaging was damaged."
    {
        "product": "mouse",
        "positive_aspects": [],
        "negative_aspects": ["late delivery", "damaged packaging"],
        "overall_sentiment": "neutral",
        "action_required": "investigate shipping partner"
    }

    Example 3:
    Feedback: "Keyboard is fantastic! Love the mechanical switches. RGB lighting is stunning!"
    {
        "product": "keyboard",
        "positive_aspects": ["mechanical switches", "RGB lighting"],
        "negative_aspects": [],
        "overall_sentiment": "very positive",
        "action_required": "none"
    }

    ---

    Now extract from this feedback:
    """ + f"""
    Feedback: {customer_message}
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    print("Few-Shot Data Extraction:")
    print(response.output_text)

# Run all examples
if __name__ == "__main__":
    # few_shot_classification()
    # few_shot_response_generation()
    few_shot_data_extraction()
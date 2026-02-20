from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def zero_shot_example():
    """
    Example: Customer inquiry classification without any examples

    📖 STORY CONTEXT - Day 3 (Feb 13, 2026):
    Aditya Patel placed order #SM-2026-12345 on Feb 10. Today (3 days later),
    he hasn't received shipping confirmation and is getting worried.
    """

    # Customer inquiry
    customer_message = """
    Hi, I'm Aditya Patel. I ordered a gaming laptop, mouse, and keyboard
    3 days ago but haven't received any shipping confirmation yet.
    My order number is #SM-2026-12345. Can you help me find out the status?
    """

    # Zero-shot prompt - no examples provided
    prompt = f"""
    Classify the following customer inquiry into one of these categories:
    - Order Status
    - Product Question
    - Technical Support
    - Complaint
    - Return/Refund

    Customer Inquiry:{customer_message}

    Classification:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.3  # Lower temperature for consistent classification
    )

    print("Zero-Shot Classification:")
    print(response.output_text)
    print("\n" + "="*50 + "\n")

# Example 2: Sentiment Analysis
def zero_shot_sentiment():
    """
    Sentiment analysis without examples

    📖 STORY CONTEXT - Day 3 (continued):
    Aditya is worried but remaining polite in his inquiry.
    Analyze his sentiment to prioritize the response.
    """

    review = """I ordered 3 days ago and haven't heard anything about shipping.
    Starting to get concerned but hoping everything is okay with my order #SM-2026-12345."""

    prompt = f"""
    Analyze the sentiment of this customer message and classify it as:
    Positive, Negative, or Mixed

    Review:{review}

    Sentiment:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    print("Zero-Shot Sentiment Analysis:")
    print(response.output_text)

# Run examples
if __name__ == "__main__":
    zero_shot_example()
    zero_shot_sentiment()
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def chain_of_thought_basic():
    """
    Example: Basic CoT for logical reasoning

    📖 STORY CONTEXT - Day 7 (Feb 17, 2026):
    Calculate refund options for Aditya's defective mice from order #SM-2026-12345.
    Original order total was $1,499 after discount + $8.50 shipping.
    """

    prompt = """
    Aditya Patel's order #SM-2026-12345:
    - Gaming Laptop: $1,299
    - Wireless Mouse (2 units): $49.99 each = $99.98
    - Mechanical RGB Keyboard: $89.99
    Subtotal: $1,488.97

    Applied 10% discount coupon: -$148.90
    Subtotal after discount: $1,340.07
    Shipping: $8.50 (free shipping threshold was $1,500 before discount)
    Total paid: $1,348.57

    Both mice are defective and need to be returned/replaced.
    Shipping costs are non-refundable per policy.

    Calculate the refund amount if we refund just the mice. Think through it step by step.
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    print("Chain-of-Thought Calculation:")
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def chain_of_thought_few_shot():
    """
    Example: Few-shot CoT for complex customer scenarios

    📖 STORY CONTEXT - Day 7 (continued):
    Analyze Aditya's situation to determine the best resolution approach.
    Aditya is a new customer, order placed 7 days ago, product defect issue.
    """

    prompt = """
    Analyze customer scenarios and provide step-by-step reasoning for the best resolution.

    Example:
    Scenario: Customer bought a laptop 35 days ago. Our return policy is 30 days. The laptop has a manufacturing defect. Customer is angry and threatens to leave negative review.

    Reasoning:
    1. Check return policy: 30 days (exceeded by 5 days)
    2. Identify issue type: Manufacturing defect (not customer damage)
    3. Assess customer sentiment: Angry, might churn
    4. Consider warranty: Manufacturing defects covered beyond return period
    5. Calculate business impact: Negative review > cost of exception
    6. Decision factors: Customer loyalty vs strict policy

    Resolution: Accept return as exception because:
    - Manufacturing defect is our responsibility
    - Small policy exception (5 days) worth customer retention
    - Prevents negative PR
    - Falls under warranty coverage anyway

    Action: Approve return, apologize for defect, offer expedited refund + 10% future purchase credit

    ---

    Now analyze this scenario:
    Scenario: Aditya Patel ordered gaming setup 7 days ago (order #SM-2026-12345: laptop $1,299, 2x mouse $49.99 each, keyboard $89.99). Both mice have defective clicking buttons. He's polite but disappointed. This is his first order with us. Laptop and keyboard work perfectly.

    Reasoning:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    print("Chain-of-Thought Customer Scenario:")
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def chain_of_thought_troubleshooting():
    """
    Example: Technical troubleshooting with CoT

    📖 STORY CONTEXT - Day 7 (continued):
    Troubleshoot what might be causing the clicking issues with Aditya's mice.
    """

    prompt = """
    Customer (Aditya Patel, order #SM-2026-12345) reports: "Both wireless mice
    have clicking issues - buttons don't register clicks properly. I tried fresh
    batteries and different USB ports. The mice connect fine, cursor moves smoothly,
    but clicks fail about 50% of the time."

    Provide troubleshooting steps with reasoning:

    Think through:
    1. What could cause clicking issues on BOTH units?
    2. What has the customer already tried?
    3. What's the most likely cause?
    4. Is this user error or product defect?

    Provide step-by-step analysis.
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    print("Chain-of-Thought Troubleshooting:")
    print(response.output_text)

def zero_shot_cot():
    """
    Example: Zero-shot CoT using "Let's think step by step"

    📖 STORY CONTEXT - Day 7 (continued):
    Calculate potential refund for Aditya's mice using zero-shot CoT approach.
    """

    prompt = """
    Aditya Patel's order #SM-2026-12345:
    - Total items ordered: Gaming laptop ($1,299), 2x Wireless mice ($49.99 each), Keyboard ($89.99)
    - Subtotal: $1,488.97
    - Applied 10% discount: -$148.90
    - After discount: $1,340.07
    - Shipping: $8.50
    - Total paid: $1,348.57

    He wants to return both defective mice ($49.99 each).
    - Shipping is non-refundable
    - Discount was applied to entire order

    How much should be refunded?

    Let's think step by step:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    print("Zero-Shot Chain-of-Thought:")
    print(response.output_text)

# Run all examples
if __name__ == "__main__":
    # chain_of_thought_basic()
    # chain_of_thought_few_shot()
    # chain_of_thought_troubleshooting()
    zero_shot_cot()
from openai import OpenAI
from dotenv import load_dotenv
from collections import Counter

load_dotenv()
client = OpenAI()

def self_consistency_refund_calculation():
    """
    Example: Calculate refund amount with self-consistency

    📖 STORY CONTEXT - Day 9 (Feb 19, 2026):
    Use multiple reasoning paths to ensure accurate refund calculation for Aditya's
    defective mouse from order #SM-2026-12345.
    """

    prompt = """
    Calculate the refund amount for this return:

    Original order #SM-2026-12345 (Aditya Patel):
    - Gaming Laptop: $1,299.00
    - Wireless Mouse (Qty: 2): $49.99 each = $99.98
    - Mechanical RGB Keyboard: $89.99
    Subtotal: $1,488.97

    Customer used:
    - 10% discount code (applied to total)
    - Paid via credit card

    Shipping: $8.50 (non-refundable per policy)
    Total paid: $1,348.57

    Customer is returning BOTH mouse (defective clicking buttons).

    Think step by step and calculate the exact refund amount to credit card.
    Important: The discount was applied proportionally to all items.
    """

    # Generate multiple responses
    num_samples = 5
    responses = []

    print(f"Generating{num_samples} reasoning paths...\n")

    for i in range(num_samples):
        response = client.responses.create(
            model="gpt-5.2",
            input=[{"role": "user", "content": prompt}],
            temperature=0.7  # Higher temperature for diverse reasoning
        )

        response_text = response.output_text
        responses.append(response_text)
        print(f"Response{i+1}:")
        print(response_text)
        print("\n" + "-"*50 + "\n")

    # Extract final answers (simplified - in production, use regex or structured output)
    print("Analyzing for self-consistency...")
    print("In production, extract numerical answers and find consensus.")

    return responses

def self_consistency_priority_classification():
    """
    Example: Priority classification with voting

    📖 STORY CONTEXT - Day 9 (continued):
    Classify the urgency of Aditya's inquiry using multiple reasoning paths
    to ensure we prioritize correctly.
    """

    customer_inquiry = """
    Hi, Aditya Patel here (order #SM-2026-12345). I reported the defective mouse
    issue 3 days ago and haven't heard back yet. I really need working mouse for a
    work project deadline tomorrow. Can someone please help? Getting quite urgent now.
    """

    prompt = f"""
    Classify this customer inquiry priority:
    - LOW: General questions, no urgency
    - MEDIUM: Important but not time-critical
    - HIGH: Time-sensitive, significant impact
    - CRITICAL: Immediate attention required, business impact

    Inquiry:{customer_inquiry}

    Think about urgency, impact, customer sentiment, and business priority.
    Provide your classification: [LOW/MEDIUM/HIGH/CRITICAL]
    """

    # Generate multiple classifications
    num_samples = 5
    classifications = []

    print(f"Generating{num_samples} classifications...\n")

    for i in range(num_samples):
        response = client.responses.create(
            model="gpt-5.2",
            input=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        response_text = response.output_text

        # Simple extraction (in production, use better parsing)
        for priority in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
            if priority in response_text.upper():
                classifications.append(priority)
                break

        print(f"Classification{i+1}:{classifications[-1] if classifications and len(classifications) == i+1 else 'Could not extract'}")

    # Majority voting
    if classifications:
        most_common = Counter(classifications).most_common(1)[0]
        final_classification = most_common[0]
        confidence = most_common[1] / num_samples

        print(f"\n{'='*50}")
        print(f"Final Classification:{final_classification}")
        print(f"Confidence:{confidence:.0%} ({most_common[1]}/{num_samples} votes)")
        print(f"All votes:{Counter(classifications)}")

    return final_classification

def self_consistency_decision_making():
    """
    Example: Complex decision with multiple factors

    📖 STORY CONTEXT - Day 9 (continued):
    Should we offer expedited replacement shipping (costs us $35) even though
    standard replacement is the policy? Aditya needs mouse for work deadline tomorrow.
    """

    prompt = """
    Decision needed for order #SM-2026-12345 (Aditya Patel):

    Situation:
    - Customer ordered $1,348 gaming setup 9 days ago (first purchase)
    - Both mouse defective (clicking issues) - clear quality issue, not user error
    - Laptop and keyboard working perfectly (she's happy with those)
    - Reported issue 3 days ago, now has work deadline tomorrow
    - Standard replacement: 5-7 day shipping (free)
    - Expedited replacement: Next day ($35 cost to us)

    Policy: Standard replacement shipping for defects
    Customer sentiment: Polite but increasingly urgent
    Customer value: First order, potential long-term customer
    Our fault: Product defect

    Should we approve expedited shipping exception? YES or NO

    Think through business implications, customer loyalty, policy precedent, and costs.
    End with: DECISION: [YES/NO]
    """

    num_samples = 7  # Odd number for clear majority
    decisions = []

    print(f"Generating{num_samples} decision reasoning paths...\n")

    for i in range(num_samples):
        response = client.responses.create(
            model="gpt-5.2",
            input=[{"role": "user", "content": prompt}],
            temperature=0.8  # Higher temperature for diverse perspectives
        )

        response_text = response.output_text

        # Extract decision
        if "DECISION: YES" in response_text.upper():
            decisions.append("YES")
        elif "DECISION: NO" in response_text.upper():
            decisions.append("NO")

        print(f"Path{i+1}:{decisions[-1] if decisions and len(decisions) == i+1 else 'Unclear'}")

    # Majority vote
    if decisions:
        decision_counts = Counter(decisions)
        final_decision = decision_counts.most_common(1)[0][0]
        confidence = decision_counts[final_decision] / num_samples

        print(f"\n{'='*50}")
        print(f"Final Decision:{final_decision}")
        print(f"Confidence:{confidence:.0%} ({decision_counts[final_decision]}/{num_samples} votes)")
        print(f"Breakdown:{dict(decision_counts)}")

    return final_decision

# Run examples
if __name__ == "__main__":
    # print("Example 1: Refund Calculation\n" + "="*50 + "\n")
    # self_consistency_refund_calculation()

    # print("\n\nExample 2: Priority Classification\n" + "="*50 + "\n")
    # self_consistency_priority_classification()

    print("\n\nExample 3: Complex Decision Making\n" + "="*50 + "\n")
    self_consistency_decision_making()
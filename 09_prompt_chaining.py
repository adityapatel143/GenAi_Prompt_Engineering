from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI()

def prompt_chain_customer_email_processing():
    """
    Example: Process customer email through multiple stages

    📖 STORY CONTEXT - Day 12 (Feb 22, 2026):
    Process Aditya's entire case through a complete workflow chain from
    initial inquiry to resolution and follow-up.
    """

    customer_email = """
    Subject: Return completed - Request for confirmation

    Hi,

    This is Aditya Patel (Order #SM-2026-12345). I wanted to confirm that I received
    the replacement mice yesterday via expedited shipping - thank you!

    The new mice work perfectly. I really appreciate how you handled the defect issue,
    especially the fast replacement since I had a work deadline.

    The gaming laptop and RGB keyboard from my original order are still working great.
    I'm very happy with those products.

    Could you send me confirmation that this case is fully resolved?
    Also, I'd be interested in knowing if you have any deals on gaming headsets.

    Thanks for the excellent customer service!

    Aditya Patel
    aditya.p@techcorp.com
    Order #SM-2026-12345
    """

    # STEP 1: Extract structured information
    print("STEP 1: Information Extraction\n" + "="*50)

    step1_prompt = f"""
    Extract key information from this customer email in JSON format:

    Email:{customer_email}

    Extract:
    - customer_name
    - customer_email
    - order_id
    - issues (list)
    - urgency_level (low/medium/high/critical)
    - sentiment (positive/neutral/negative/angry)
    - deadline (if mentioned)

    Respond with only valid JSON.
    """

    step1_response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": step1_prompt}],
        temperature=0.2
    )

    extracted_info = step1_response.output_text
    print("Extracted Information:")
    print(extracted_info)
    print("\n" + "-"*50 + "\n")

    # STEP 2: Classify and prioritize issues
    print("STEP 2: Issue Classification & Prioritization\n" + "="*50)

    step2_prompt = f"""
    Based on this extracted customer information, classify each issue and assign priority:

{extracted_info}

    For each issue, provide:
    - Issue type (product defect, billing error, service complaint, etc.)
    - Priority (P0-critical, P1-high, P2-medium, P3-low)
    - Department responsible
    - Estimated resolution time

    Format as JSON array.
    """

    step2_response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": step2_prompt}],
        temperature=0.2
    )

    classified_issues = step2_response.output_text
    print("Classified Issues:")
    print(classified_issues)
    print("\n" + "-"*50 + "\n")

    # STEP 3: Generate action plan
    print("STEP 3: Action Plan Generation\n" + "="*50)

    step3_prompt = f"""
    Create an action plan to resolve these customer issues:

    Customer Info:{extracted_info}

    Issues:{classified_issues}

    Generate a step-by-step action plan including:
    - Immediate actions (within 24 hours)
    - Investigation steps
    - Resolution plan
    - Follow-up actions
    - Who is responsible for each step
    """

    step3_response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": step3_prompt}],
        temperature=0.6
    )

    action_plan = step3_response.output_text
    print("Action Plan:")
    print(action_plan)
    print("\n" + "-"*50 + "\n")

    # STEP 4: Generate customer response email
    print("STEP 4: Customer Response Generation\n" + "="*50)

    step4_prompt = f"""
    Write a professional, empathetic response email to the customer:

    Customer's original email:{customer_email}

    Issues identified:{classified_issues}

    Action plan:{action_plan}

    The email should:
    - Acknowledge all concerns with empathy
    - Apologize sincerely
    - Explain what went wrong (briefly)
    - Detail exactly what we're doing to fix it
    - Provide timeline
    - Offer additional compensation if appropriate
    - Include direct contact for escalation
    """

    step4_response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": step4_prompt}],
        temperature=0.7
    )

    response_email = step4_response.output_text
    print("Customer Response Email:")
    print(response_email)
    print("\n" + "="*50 + "\n")

    return {
        "extracted_info": extracted_info,
        "classified_issues": classified_issues,
        "action_plan": action_plan,
        "response_email": response_email
    }

def prompt_chain_product_description():
    """
    Example: Generate product description through refinement chain

    📖 STORY CONTEXT - Day 12 (continued):
    Aditya expressed interest in gaming headsets. Generate a compelling
    product description through a multi-step refinement chain.
    """

    product_specs = {
        "name": "HyperSound Gaming Headset Pro",
        "type": "Wireless Gaming Headset",
        "audio": "7.1 Surround Sound",
        "mic": "Noise-cancelling boom mic",
        "battery": "30 hours",
        "connectivity": "2.4GHz wireless + Bluetooth",
        "weight": "9.8 oz",
        "compatibility": "PC, PS5, Xbox, Switch",
        "price": "$149.99"
    }

    # STEP 1: Generate features list
    print("STEP 1: Feature Extraction\n" + "="*50)

    step1_prompt = f"""
    Convert these technical specifications into customer-friendly features:

{json.dumps(product_specs, indent=2)}

    List 5-7 key features that would appeal to gamers like Aditya Patel
    who just bought a gaming laptop and RGB keyboard.
    """

    step1_response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": step1_prompt}],
        temperature=0.7
    )

    features = step1_response.output_text
    print(features)
    print("\n" + "-"*50 + "\n")

    # STEP 2: Write compelling headline
    print("STEP 2: Headline Generation\n" + "="*50)

    step2_prompt = f"""
    Based on these features, create 3 compelling headlines for this product:

{features}

    Headlines should be:
    - Attention-grabbing
    - Benefit-focused (not feature-focused)
    - 8-12 words each
    """

    step2_response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": step2_prompt}],
        temperature=0.9
    )

    headlines = step2_response.output_text
    print(headlines)
    print("\n" + "-"*50 + "\n")

    # STEP 3: Full product description
    print("STEP 3: Full Description\n" + "="*50)

    step3_prompt = f"""
    Write a compelling product description using:

    Features:{features}

    Headline (use the best one):{headlines}

    Structure:
    - Engaging opening paragraph
    - Key features with benefits
    - Use case scenarios
    - Call to action

    Tone: Professional but friendly, persuasive
    Length: 150-200 words
    """

    step3_response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": step3_prompt}],
        temperature=0.8
    )

    description = step3_response.output_text
    print(description)

    return description

# Run examples
if __name__ == "__main__":
    # print("\n🔗 PROMPT CHAINING EXAMPLE 1: Customer Email Processing\n")
    # result = prompt_chain_customer_email_processing()

    print("\n\n🔗 PROMPT CHAINING EXAMPLE 2: Product Description\n")
    prompt_chain_product_description()
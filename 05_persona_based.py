from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def persona_technical_expert():
    """
    Example: Technical support with expert persona

    📖 STORY CONTEXT - Day 8 (Feb 18, 2026):
    Technical expert provides professional troubleshooting for Aditya's mice issue.
    """

    system_message = """
    You are a senior technical support specialist with 10 years of experience
    in computer peripherals and wireless devices. You explain technical concepts clearly,
    ask diagnostic questions efficiently, and provide step-by-step solutions.
    You're patient but professional.
    """

    user_message = """Hi, I'm Aditya Patel (order #SM-2026-12345). Both wireless
    mice I received have clicking issues. Buttons don't register reliably - about 50%
    failure rate. I've tried fresh batteries and different USB ports. Cursor movement
    works perfectly fine. Is this fixable or defective hardware?"""

    response = client.responses.create(
        model="gpt-5.2",
        input=[
            {"role": "developer", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )

    print("Technical Expert Persona:")
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def persona_empathetic_support():
    """
    Example: Empathetic customer service persona

    📖 STORY CONTEXT - Day 8 (continued):
    Empathetic support representative responds to Aditya's frustration.
    """

    system_message = """
    You are an empathetic and patient customer service representative who
    genuinely cares about solving customer problems. You always acknowledge
    customer frustrations, apologize when appropriate, and go above and
    beyond to help. You use positive language and make customers feel valued.
    """

    user_message = """
    This is Aditya Patel, order #SM-2026-12345. I was so excited to get my
   gaming setup, but both mice are defective with clicking issues. The laptop
    and keyboard are great, but I really need working mice. This is really
    disappointing for a first order. Can you help?
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[
            {"role": "developer", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        temperature=0.8
    )

    print("Empathetic Support Persona:")
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def persona_efficiency_expert():
    """
    Example: Brief, efficient business persona

    📖 STORY CONTEXT - Day 8 (continued):
    Internal analysis of Aditya's case for quality team briefing.
    """

    system_message = """
    You are a no-nonsense, efficient business analyst who values clarity and
    brevity. You get straight to the point, use bullet points, and focus on
    actionable insights. You don't use fluff or unnecessary explanations.
    """

    user_message = """
    Analyze this customer case:
    - Customer: Aditya Patel (first-time buyer)
    - Order #SM-2026-12345, placed Feb 10, delivered Feb 15
    - Issue reported Feb 16: Both wireless mice defective (clicking issues)
    - Other items (laptop, keyboard) working perfectly
    - Customer polite, seeking resolution
    - Mice: 2 units x $49.99 = $99.98 (after discount: ~$90)
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[
            {"role": "developer", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        temperature=0.6
    )

    print("Efficiency Expert Persona:")
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def persona_comparison():
    """
    Example: Same query, different personas

    📖 STORY CONTEXT - Day 8 (continued):
    See how different personas explain Aditya's refund processing timeline.
    """

    query = "Explain to Aditya Patel why his refund for the defective mice (order #SM-2026-12345) was processed 2 days ago but he hasn't received the money yet."

    personas = {
        "Technical Expert": """You are a payments systems engineer who understands
        banking infrastructure, ACH transfers, and payment processing.""",

        "Customer Service": """You are a friendly customer service rep who explains
        things in simple terms that any customer can understand.""",

        "Account Manager": """You are a premium account manager for VIP clients.
        You're professional, reassuring, and proactive."""
    }

    for persona_name, persona_description in personas.items():
        response = client.responses.create(
            model="gpt-5.2",
            input=[
                {"role": "developer", "content": persona_description},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            max_output_tokens=200
        )

        print(f"{persona_name} Response:")
        print(response.output_text)
        print("\n" + "-"*50 + "\n")

# Run all examples
if __name__ == "__main__":
    # persona_technical_expert()
    # persona_empathetic_support()
    # persona_efficiency_expert()
    persona_comparison()
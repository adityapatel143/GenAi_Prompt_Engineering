from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def meta_prompt_optimizer():
    """
    Example: Use AI to improve a prompt

    📖 STORY CONTEXT - Day 14 (Feb 24, 2026):
    Optimize our defective product response prompt based on learnings from
    Aditya's case (order #SM-2026-12345) where we handled it well.
    """

    original_prompt = """
    Customer got defective product. Send replacement.
    """

    meta_prompt = f"""
    I have this prompt for handling defective product cases:

    "{original_prompt}"

    We recently had a successful case (Aditya Patel, order #SM-2026-12345) where:
    - Customer received 2 defective wireless mice
    - He was polite but had urgent work deadline
    - We resolved it with expedited replacement
    - Turned first-time buyer into happy customer

    This current prompt is too vague. Please:

    1. Analyze what's wrong with this prompt
    2. Suggest what elements are missing based on this case
    3. Provide an improved version that captures best practices
    4. Explain why the improved version is better

    Consider:
    - Customer sentiment assessment
    - Urgency evaluation
    - Multiple resolution options
    - Tone and empathy
    - Follow-up actions
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": meta_prompt}],
        temperature=0.7
    )

    print("Meta-Prompt Analysis:\n" + "="*50)
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def meta_prompt_strategy_selector():
    """
    Example: Ask AI which prompting technique to use

    📖 STORY CONTEXT - Day 14 (continued):
    Design optimal workflow for similar defect cases based on Aditya's experience.
    """

    task_description = """
    Task: Build automated workflow for handling product defect cases like Aditya Patel's
    (order #SM-2026-12345 - defective wireless mice).

    Requirements:
    - Automatically classify defect reports by severity
    - Assess customer urgency and sentiment
    - Decide between refund vs. replacement
    - Determine shipping speed (standard vs. expedited)
    - Generate empathetic response email
    - Extract structured data for quality team
    - Follow up after resolution

    Input: Customer defect report email
    Output: Complete resolution workflow with actions and communications
    """

    meta_prompt = f"""
    I need to design a prompt system for this workflow:

{task_description}

    Based on Aditya's successful case, what prompting strategy should I use? Consider:
    - Zero-shot, few-shot, or chain-of-thought?
    - Should I use prompt chaining?
    - Would ReAct be beneficial for decision-making?
    - Do I need self-consistency for high-stakes decisions?
    - Do I need structured output?

    For each relevant technique, explain:
    1. Why it's suitable for this workflow
    2. Where in the process to apply it
    3. Potential challenges
    4. Expected benefits

    Then provide a recommended approach with step-by-step implementation plan.
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": meta_prompt}],
        temperature=0.7
    )

    print("Strategy Recommendation:\n" + "="*50)
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def meta_prompt_generator():
    """
    Example: Generate a complete prompt from requirements

    📖 STORY CONTEXT - Day 14 (continued):
    Generate a prompt for classifying defect cases using Aditya's case as reference.
    """

    requirements = """
    Create a prompt for:

    Purpose: Classify product defect reports and determine optimal resolution path

    Input: Customer defect report (like Aditya Patel order #SM-2026-12345 case)

    Output needed:
    - Defect severity (Minor, Moderate, Severe, Critical)
    - Customer urgency (Low, Medium, High, Critical)
    - Customer sentiment (Positive, Neutral, Frustrated, Angry)
    - Recommended action (Refund, Standard Replacement, Expedited Replacement)
    - Estimated cost of resolution

    Constraints:
    - Must be consistent and reliable
    - Should consider customer history (first-time vs. repeat buyer)
    - Should factor in deadlines and special circumstances
    - Output must be JSON format

    Special considerations:
    - First-time buyers need extra care (retention opportunity)
    - Urgent deadlines may warrant expedited shipping exceptions
    - Multiple defective items indicate possible batch/quality issues
    - Balance cost-effectiveness with customer satisfaction
    """

    meta_prompt = f"""
    Generate a complete, production-ready prompt based on these requirements:

    {requirements}

    Your output should include:
    1. The complete prompt (ready to use)
    2. Recommended model parameters (temperature, max_output_tokens, etc.)
    3. Example input and expected output
    4. Edge cases to test
    5. Potential issues and how to handle them

    Make the prompt professional, clear, and optimized for accuracy.
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": meta_prompt}],
        temperature=0.7,
        max_output_tokens=2000
    )

    print("Generated Complete Prompt System:\n" + "="*50)
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def meta_prompt_debugger():
    """
    Example: Debug why a prompt isn't working
    """

    problematic_prompt = """
    Analyze the customer feedback and tell me what's wrong.

    Feedback: "Product is ok but shipping was slow and box was damaged."
    """

    issue_description = """
    This prompt sometimes:
    - Misses the shipping issue
    - Doesn't separate product vs. service feedback
    - Gives inconsistent sentiment scores
    - Output format varies
    """

    meta_prompt = f"""
    I have a prompt that's not working well:

    Prompt: "{problematic_prompt}"

    Issues:{issue_description}

    Please:
    1. Identify specific problems with the prompt (ambiguity, missing instructions, etc.)
    2. Explain why these problems cause the issues described
    3. Provide a fixed version of the prompt
    4. Suggest testing methodology to verify the fix
    5. Recommend monitoring approach for production use
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": meta_prompt}],
        temperature=0.7
    )

    print("Prompt Debug Analysis:\n" + "="*50)
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def meta_prompt_ab_test_design():
    """
    Example: Design A/B test for prompt variations
    """

    task = "Generate empathetic responses to upset customers"

    meta_prompt = f"""
    I want to A/B test different prompting approaches for:{task}

    Design an A/B test plan including:

    1. Create 3 different prompt variations (A, B, C) using different techniques:
       - Variation A: [Choose a technique and create prompt]
       - Variation B: [Choose different technique and create prompt]
       - Variation C: [Choose another technique and create prompt]

    2. Evaluation criteria: What metrics should I measure?

    3. Test cases: Provide 5 diverse customer scenarios to test all variations

    4. Success criteria: How do I determine which prompt is best?

    5. Implementation advice: How to run this test efficiently
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": meta_prompt}],
        temperature=0.7,
        max_output_tokens=2000
    )

    print("A/B Test Design:\n" + "="*50)
    print(response.output_text)

# Run examples
if __name__ == "__main__":
    # meta_prompt_optimizer()
    # meta_prompt_strategy_selector()
    meta_prompt_generator()
    # meta_prompt_debugger()
    # meta_prompt_ab_test_design()
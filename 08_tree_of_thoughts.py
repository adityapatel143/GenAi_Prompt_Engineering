from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def tree_of_thoughts_decision():
    """
    Example: Complex customer service decision with multiple approaches

    📖 STORY CONTEXT - Day 11 (Feb 21, 2026):
    Explore multiple resolution strategies for Aditya's defective mice case
    to find the optimal balance of customer satisfaction and business cost.
    """

    prompt = """
    Situation: Aditya Patel - Order #SM-2026-12345 (First-time customer)
    1. Ordered $1,348 gaming setup 11 days ago
    2. Both wireless mice defective (clicking issues) - clear manufacturing defect
    3. Laptop and keyboard working perfectly (he's happy with those)
    4. Customer has been patient and polite throughout
    5. He now has urgent work deadline tomorrow, needs working mice
    6. Has been waiting 5 days since first report

    Available resolution options:
    - Standard replacement (5-7 day shipping - free)
   - Expedited replacement (next day - $35 cost)
    - Full refund for mice (~$90)
    - Refund + additional compensation
    - Keep defective + send replacement + bonus

    Constraints:
    - Want to turn first-time customer into loyal repeat buyer
    - Cannot exceed $150 in total cost to company
    - Need to set precedent for similar defect cases
    - Customer has urgent deadline tomorrow
    - Our fault (manufacturing defect)

    Use Tree of Thoughts: Explore 3 different solution paths, evaluate each, then choose the best.

    Format:

    PATH 1: [Approach name]
    Solution: [Detailed solution]
    Pros: [Benefits]
    Cons: [Drawbacks]
    Cost: [Estimated cost]
    Customer satisfaction score: [1-10]

    PATH 2: [Different approach]
    ...

    PATH 3: [Another approach]
    ...

    EVALUATION:
    [Compare the three paths]

    FINAL DECISION:
    [Best path and why]
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.8,  # Higher for creative exploration
        max_output_tokens=1500
    )

    print("Tree of Thoughts - Customer Resolution:\n" + "="*50)
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def tree_of_thoughts_product_recommendation():
    """
    Example: Product recommendation with multiple criteria

    📖 STORY CONTEXT - Day 11 (continued):
    Aditya is happy with his laptop and keyboard from order #SM-2026-12345.
    He's interested in additional gaming peripherals. Explore recommendation strategies.
    """

    prompt = """
    Customer profile: Aditya Patel
    - Current satisfaction: Love the gaming laptop & RGB keyboard from order #SM-2026-12345
    - Budget: $150-$250 for additional peripherals
    - Use case: Gaming setup completion + work productivity
    - Pain point: Just experienced mice quality issues (now resolved)
    - Trust level: Cautious due to defective mice, but appreciates resolution

    Available products to recommend:
    A) Premium gaming mouse - $89 (high-end, reliable brand, 5-year warranty)
    B) Gaming headset + standard mouse combo - $149 (good value, popular)
    C) Mousepad + webcam + budget mouse - $129 (complete work-from-home setup)
    D) High-end wireless mouse + extended warranty - $120 (quality + peace of mind)

    Explore 3 different recommendation strategies:

    STRATEGY 1: Quality-focused (rebuild trust)
    Reasoning: [Why prioritize quality after defect issue]
    Recommendation: [Which product]
    Trade-offs: [What customer gives up]

    STRATEGY 2: Value-maximizing
    Reasoning: [Why maximize features per dollar]
    Recommendation: [Which product or combo]
    Trade-offs: [What customer gives up]

    STRATEGY 3: Problem-solving (address pain points)
    Reasoning: [Why focus on customer's specific needs]
    Recommendation: [Which product]
    Trade-offs: [What customer gives up]

    EVALUATION:
    [Compare strategies against customer's current situation]

    FINAL RECOMMENDATION:
    [Best strategy and product with reasoning]
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_output_tokens=1200
    )

    print("Tree of Thoughts - Product Recommendation:\n" + "="*50)
    print(response.output_text)
    print("\n" + "="*50 + "\n")

def tree_of_thoughts_scaling_strategy():
    """
    Example: Business planning with ToT

    📖 STORY CONTEXT - Day 11 (continued):
    Based on Aditya's case and similar defect issues, plan how to prevent
    and better handle product quality problems in the future.
    """

    prompt = """
    Business Problem: We've had 15 similar cases this month like Aditya Patel's order #SM-2026-12345
    (defective mice with clicking issues). This specific mouse model has 12% defect rate.

    Current situation:
    - Average cost per defective return: $125 (shipping, replacement, support time)
    - Customer satisfaction impact: Drops from 4.7 to 3.4 stars after defect experience
    - We sold 500 units of this mouse model this month
    - Supplier offers: $5/unit credit OR full product recall
    - Monthly revenue from this model: $25,000

    Explore 3 different resolution strategies:

    BRANCH 1: Product recall and supplier change
    Approach: [Details]
    Implementation: [Steps]
    Timeline: [How long]
    Pros: [Benefits]
    Cons: [Risks]
    Expected costs & impact: [Financial & reputation metrics]

    BRANCH 2: Selective QA and proactive outreach
    Approach: [Details]
    Implementation: [Steps]
    Timeline: [How long]
    Pros: [Benefits]
    Cons: [Risks]
    Expected costs & impact: [Financial & reputation metrics]

    BRANCH 3: Enhanced warranty and fast-track replacement
    Approach: [Details]
    Implementation: [Steps]
    Timeline: [How long]
    Pros: [Benefits]
    Cons: [Risks]
    Expected costs & impact: [Financial & reputation metrics]

    CROSS-EVALUATION:
    Short-term (1-3 months): [Which is best]
    Long-term (6-12 months): [Which is best]
    Risk assessment: [Compare risks]
    Customer retention: [Impact on customers like Aditya]

    RECOMMENDED STRATEGY:
    [Final choice with full justification]
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.8,
        # max_output_tokens=1500
    )

    print("Tree of Thoughts - Business Strategy:\n" + "="*50)
    print(response.output_text)

# Run examples
if __name__ == "__main__":
    # tree_of_thoughts_decision()
    # tree_of_thoughts_product_recommendation()
    tree_of_thoughts_scaling_strategy()
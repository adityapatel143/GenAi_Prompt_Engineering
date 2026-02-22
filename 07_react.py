from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI()

# Simulated tools/actions
class CustomerServiceTools:
    """
    Simulated backend tools for customer service

    📖 STORY CONTEXT - Day 10 (Feb 20, 2026):
    Agent uses these tools to process Aditya's return request for order #SM-2026-12345.
    """

    @staticmethod
    def lookup_order(order_id):
        """Simulate order lookup"""
        orders = {
            "SM-2026-12345": {
                "customer": "Aditya Patel",
                "email": "aditya.p@techcorp.com",
                "status": "delivered",
                "items": {
                    "Gaming Laptop": {"price": 1299.00, "qty": 1, "status": "no issues"},
                    "Wireless Mouse": {"price": 49.99, "qty": 2, "status": "defective - reported Feb 16"},
                    "Mechanical RGB Keyboard": {"price": 89.99, "qty": 1, "status": "no issues"}
                },
                "subtotal": 1488.97,
                "discount": -148.90,
                "shipping": 8.50,
                "total": 1348.57,
                "order_date": "2026-02-10",
                "delivery_date": "2026-02-15",
                "tracking": "TRACK-SM-12345"
            }
        }
        return orders.get(order_id, {"error": "Order not found"})

    @staticmethod
    def check_inventory(product_name):
        """Simulate inventory check"""
        inventory = {
            "Gaming Laptop": {"in_stock": True, "quantity": 45, "warehouse": "East"},
            "Wireless Mouse": {"in_stock": False, "quantity": 0, "warehouse": "West"},
            "Mechanical RGB Keyboard": {"in_stock": True, "quantity": 67, "warehouse": "West"}
        }
        return inventory.get(product_name, {"error": "Product not found"})

    @staticmethod
    def check_return_eligibility(order_id):
        """Check if order is eligible for return"""
        order = CustomerServiceTools.lookup_order(order_id)
        if "error" in order:
            return {"eligible": False, "reason": "Order not found"}

        # Simulate return policy logic
        return {
            "eligible": True,
            "return_window": "30 days",
            "days_remaining": 23,
            "return_label": "Generate return label available"
        }

    @staticmethod
    def calculate_refund(order_id, items_to_return):
        """Calculate refund amount"""
        # For Aditya's order #SM-2026-12345, returning 2 mice
        if order_id == "SM-2026-12345" and "Wireless Mouse" in items_to_return:
            return {
                "refund_amount": "$89.98",
                "breakdown": {
                    "items": "2x Wireless Mouse @ $49.99 = $99.98",
                    "discount_applied": "-$9.98 (10% discount)",
                    "net_refund": "$90.00",
                    "shipping": "$0 (non-refundable)",
                    "restocking_fee": "$0 (defective items)"
                },
                "refund_method": "Original payment method (credit card)",
                "processing_time": "5-7 business days"
            }
        return {"error": "Unable to calculate refund"}

def react_customer_inquiry():
    """
    Example: ReAct pattern for handling customer inquiry

    📖 STORY CONTEXT - Day 10 (Feb 20, 2026):
    Agent processes Aditya's return request using reasoning and actions.
    """

    customer_message = """Hi, this is Aditya Patel. I need to process a return for
    order #SM-2026-12345. Both wireless mice are defective with clicking issues.
    I'd like to get a refund or replacement ASAP."""

    tools_description = """
    Available Actions:
    - lookup_order(order_id): Get order details, items, customer info
    - check_inventory(product_name): Check product availability for replacement
    - check_return_eligibility(order_id): Check if return is possible
    - calculate_refund(order_id, items): Calculate refund amount
    """

    prompt = f"""
    You are a customer service agent. 
    Use the ReAct pattern: alternate between Thought, Action, and Observation.

{tools_description}

    Customer Message:{customer_message}

    Use this format:
    Thought: [Your reasoning about what to do next]
    Action: [The action to take with parameters]

    After getting results you'll Observe and continue reasoning.

    Begin:
    """

    messages = [{"role": "user", "content": prompt}]

    max_iterations = 5
    tools = CustomerServiceTools()

    print("ReAct Customer Service Agent:\n" + "="*50 + "\n")

    for iteration in range(max_iterations):
        # Get model's reasoning and action
        response = client.responses.create(
            model="gpt-5.2",
            input=messages,
            temperature=0.7
        )

        assistant_message = response.output_text
        messages.append({"role": "assistant", "content": assistant_message})

        print(f"Iteration{iteration + 1}:")
        print(assistant_message)
        print("\n" + "-"*50 + "\n")

        # Parse action and execute (simplified parsing)
        if "Action: lookup_order" in assistant_message:
            result = tools.lookup_order("SM-2026-12345")
            observation = f"Observation: Order details:{json.dumps(result, indent=2)}"

        elif "Action: check_return_eligibility" in assistant_message:
            result = tools.check_return_eligibility("SM-2026-12345")
            observation = f"Observation: Return eligibility:{json.dumps(result, indent=2)}"

        elif "Action: check_inventory" in assistant_message:
            result = tools.check_inventory("Wireless Mouse")
            observation = f"Observation: Inventory check:{json.dumps(result, indent=2)}"

        elif "Action: calculate_refund" in assistant_message:
            result = tools.calculate_refund("SM-2026-12345", ["Wireless Mouse"])
            observation = f"Observation: Refund calculation:{json.dumps(result, indent=2)}"

        elif "Final Answer" in assistant_message or "Response to Customer" in assistant_message:
            print("Agent has formulated final response.")
            break
        else:
            observation = "Continue with your response."

        # Add observation back to conversation
        messages.append({"role": "user", "content": observation})
        print(f"System:{observation}")
        print("\n" + "="*50 + "\n")

def react_troubleshooting():
    """
    Example: Technical troubleshooting with ReAct

    📖 STORY CONTEXT - Day 10 (continued):
    Tech support uses ReAct to diagnose Aditya's mouse clicking issues systematically.
    """

    prompt = """
    Customer Aditya Patel (order #SM-2026-12345) reports: "Both wireless mice
    have clicking issues - buttons don't register properly. I tried fresh batteries
    and different USB ports. Cursor moves fine but clicks fail 50% of the time."

    You are a technical support agent with access to:
    - check_product_specs(): Get mouse specifications and known issues
    - check_batch_info(): Check if this product batch has reported defects
    - verify_troubleshooting(): Confirm customer tried standard fixes
    - determine_root_cause(): Analyze symptoms for diagnosis

    Use ReAct pattern to troubleshoot. For each step:
    Thought: [What you're thinking]
    Action: [What to check]
    Observation: [Simulated result]

    Then provide final diagnosis and resolution.

    Begin troubleshooting:
    """

    response = client.responses.create(
        model="gpt-5.2",
        input=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    print("ReAct Technical Troubleshooting:\n" + "="*50)
    print(response.output_text)

# Run examples
if __name__ == "__main__":
    react_customer_inquiry()
    # print("\n\n")
    # react_troubleshooting()
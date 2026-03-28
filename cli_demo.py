from openai import OpenAI

client = OpenAI()

class Copilot:
    def __init__(self):
        self.history = []
        self.current_question = ""

    def update(self, text):
        self.history.append(text)
        if len(self.history) > 8:
            self.history.pop(0)

        if "?" in text or text.lower().startswith(("how", "what", "why")):
            self.current_question = text

    def get_context(self):
        return "\n".join(self.history)

    def get_focus(self):
        return " | ".join(self.history[-3:])

    def build_prompt(self):
        return f"""
You are a real-time interview copilot.

Conversation history:
{self.get_context()}

Recent focus:
{self.get_focus()}

Current question:
{self.current_question}

CORE TASK:
Generate 3-5 bullets:
• Step
  → "Speakable sentence"

TOPIC INTELLIGENCE:
- Continue context if follow-up
- Reset if new topic

STRICT EXPERIENCE MODE:
- Speak from experience
- Avoid "First / Next / Then"

Use:
- "In practice..."
- "What works well is..."
- "A common pattern is..."

Include concrete examples like refund requests, login issues.
"""

    def run(self, text):
        self.update(text)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": self.build_prompt()}],
            max_tokens=200,
            temperature=0.6,
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    copilot = Copilot()
    print("=== Real-time Copilot CLI (Final) ===")

    while True:
        try:
            user_input = input("\n[Input]: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            print("\n[Copilot Suggestion]")
            print(copilot.run(user_input))
        except KeyboardInterrupt:
            break

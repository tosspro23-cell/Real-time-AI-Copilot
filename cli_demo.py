from openai import OpenAI

client = OpenAI()


class Copilot:
    def __init__(self):
        self.history = []
        self.current_question = ""

    def update(self, text):
        self.history.append(text)

        # sliding window
        if len(self.history) > 8:
            self.history.pop(0)

        # detect question
        if "?" in text or text.lower().startswith(("how", "what", "why")):
            self.current_question = text

    def get_context(self):
        return "\n".join(self.history)

    def get_focus(self):
        recent = self.history[-3:]
        return " | ".join(recent)

    def build_prompt(self):
        context = self.get_context()
        focus = self.get_focus()

        return f"""
You are a real-time interview copilot.

You help the user THINK and SPEAK during a live conversation.

Conversation history:
{context}

Recent focus:
{focus}

Current question:
{self.current_question}

--------------------------------
CORE TASK
--------------------------------
Generate:
- 3–5 bullets
- Each bullet includes:
  1) a speaking step
  2) a natural sentence the user can say

Format:
• [Step]
  → "Sentence"

--------------------------------
TOPIC INTELLIGENCE (CRITICAL)
--------------------------------
- Determine whether the question is a FOLLOW-UP or NEW topic

FOLLOW-UP:
→ Continue system context
→ Refer to "this agent" or "this system"

NEW TOPIC:
→ Ignore previous context
→ Answer independently

If unsure → continue context

--------------------------------
ANTI-GENERIC RULES
--------------------------------
DO NOT use:
- "We need to..."
- "We should..."
- "It is important to..."
- generic advice

--------------------------------
STRICT EXPERIENCE MODE (CRITICAL)
--------------------------------
You MUST speak from experience, NOT instructions.

FORBIDDEN:
- "First, I..."
- "Next, I..."
- "Then, I..."
- step-by-step narration

REQUIRED STYLE:
- Describe what happens in real systems
- Talk about patterns, trade-offs, failures, fixes

Use phrasing like:
- "In practice, this usually involves..."
- "A common pattern is..."
- "What often breaks is..."
- "What works well is..."
- "One thing that makes a difference is..."
- "In this setup..."

IMPORTANT:
- Sound like you have built and debugged this system
- NOT like you are explaining how to build it
- Apply this style to ALL questions, not only system design questions.

--------------------------------
CONCRETENESS (CRITICAL)
--------------------------------
- Every sentence MUST include real details
- Use examples like:
  - refund requests
  - login issues
  - billing problems
  - customer complaints

--------------------------------
REALISM
--------------------------------
- Speak like a real engineer
- Avoid checklist tone
- Avoid tutorial tone

--------------------------------
DIVERSITY
--------------------------------
- Vary sentence structures
- Avoid repeating patterns

--------------------------------
OUTPUT QUALITY
--------------------------------
- Step: short (3–6 words)
- Sentence: conversational
- Specific and grounded
"""

    def run(self, text):
        self.update(text)

        prompt = self.build_prompt()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.65,
        )

        return response.choices[0].message.content


if __name__ == "__main__":
    copilot = Copilot()

    print("=== Real-time Copilot CLI (Final: Strict Experience Mode) ===")

    while True:
        try:
            user_input = input("\n[Input]: ")

            if user_input.lower() in ["exit", "quit"]:
                break

            result = copilot.run(user_input)

            print("\n[Copilot Suggestion]")
            print(result)

        except KeyboardInterrupt:
            print("\nExiting...")
            break

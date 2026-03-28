# 🧠 Real-time AI Copilot (Cognitive Layer Prototype)

A real-time, context-aware AI copilot designed to augment human thinking during live conversations.

---

## 🎯 Vision

From asking AI → to thinking WITH AI

This system focuses on the **cognitive layer** of AI:
helping humans structure thoughts and respond better in real time.

---

## ❗ Problem

In interviews, meetings, and sales:

- Cognitive overload
- Need to respond instantly
- Hard to track context
- Lower reasoning quality under pressure

---

## 💡 Solution

A copilot that:

- Maintains conversation context
- Detects topic continuity vs shift
- Generates **speakable guidance (not answers)**
- Uses **experience-style phrasing**

---

## 🏗️ Architecture

User Input
↓
Context Engine (history + focus)
↓
Topic Intelligence (follow-up vs new topic)
↓
Prompt System (experience mode)
↓
LLM
↓
Copilot Output

---

## 🔑 Features

### ✅ Context Awareness
Multi-turn conversation tracking

### ✅ Topic Intelligence
Understands when to continue vs reset context

### ✅ Experience-driven Output
Speaks like a real engineer:

- "In practice..."
- "What works well is..."

### ✅ Speakable Format
Short + actionable + real-time usable

---

## 🧪 Example

**Input**
How to build a customer support AI agent?

**Output**
• Identify common issues  
→ "I often start by analyzing frequent inquiries like refund requests or login issues."

• Train with real data  
→ "I usually gather chat logs to improve handling of billing problems."

• Add fallback  
→ "In practice, handing off to a human agent is critical for complex cases."

---

## ⚙️ Run

pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
python cli_demo.py

---

## 🚧 Scope

This MVP focuses on the **cognitive layer only**

Not included:
- ASR
- Streaming
- UI

---

## 🗺️ Roadmap

Phase 1: CLI Copilot (current)  
Phase 2: Streaming output  
Phase 3: ASR + UI  

---

## 💼 Use Cases

- Interview copilot
- Sales assistant
- Meeting support

---

## 🧠 Positioning

This is NOT:
- chatbot
- agent
- assistant

This is:

→ Cognitive augmentation system

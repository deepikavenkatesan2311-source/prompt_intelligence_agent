# Prompt Intelligent Agent 🚀

An advanced, token-optimized AI agent built using the `google-adk` framework. This agent is designed to generate, refine, and simulate structured prompts, ensuring highly reliable AI outputs while aggressively reducing token consumption.

---

## 🌟 Key Features

* **Structured Prompt Generation:** Dynamically builds system prompts and instructions using a modular blueprint.
* **Token Optimization (Cost Saving):** Leverages specialized modular files ("skills") to compress contexts and eliminate redundant conversational fluff, drastically lowering API costs.
* **Prompt Refinement & Variant Testing:** Evaluates a baseline prompt and generates optimized variations tailored to specific performance criteria.
* **Output Simulation:** Simulates how a downstream LLM will interpret the prompt, providing a preview of the structural layout and reliability of the final response before running a full production workload.

---

## 🛠️ Tech Stack & Architecture

* **Core Framework:** `google-adk` (Application Development Kit)
* **Language:** Python 3.10+
* **Package Management:** `pyproject.toml` (Poetry/Pip)
* **Key Concepts:**
    * **Skills Management:** Modular `.md` assets (e.g., `analyze-draft`, `structure-prompt`) that encapsulate specific agent capabilities.
    * **LiteLLM Integration:** Abstracted, multi-provider model routing supporting structured inputs and reasoning block filtering.

---


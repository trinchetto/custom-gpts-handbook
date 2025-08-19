# 🤖✨ OpenAI Custom GPTs Handbook ✨🤖

## 🌟 Introduction
OpenAI Custom GPTs let you build specialized AI assistants tailored to your needs. Instead of a one-size-fits-all chatbot, you can design GPTs with custom instructions, retrieval abilities, and defined personalities. These GPTs can serve as tutors, domain experts, creative partners, or customer support agents — all while staying aligned with the interaction style you choose.

This handbook summarizes key techniques and frameworks from the *OpenAI Custom GPTs* course. It’s designed as a practical reference for building, tuning, and testing your own GPTs.

---

## 🧩 Techniques at a Glance
Here’s a quick reference table of the main techniques covered in this handbook:

| Technique | Problem it Solves | Solution |
|-----------|------------------|----------|
| [📝 Programming a GPT with Instructions](#-programming-a-gpt-with-instructions) | Generic or unfocused responses | Define explicit role, scope, and behavior rules |
| [⚙️ Custom Instructions](#-custom-instructions) | Lack of personalization | Capture user goals and knowledge level in custom fields |
| [📚 Retrieval-Augmented Generation (RAG)](#-retrieval-augmented-generation-rag) | Missing or outdated knowledge | Attach external documents/databases for reference |
| [🏗️ Putting It All Together](#-putting-it-all-together) | Fragmented GPT setups | Combine persona, instructions, and retrieval into one design |
| [🔧 Understanding GPTs and Tools](#-understanding-gpts-and-tools) | Inability to handle certain tasks | Equip GPT with tools (calculator, web, APIs) |
| [🎛️ CAPITAL Framework](#-the-capital-framework) | Tone/style inconsistency | Adjust conversation style along seven dimensions |
| [🎭 Building a Persona Pattern](#-building-a-persona-pattern) | Unfocused or inconsistent persona | Define a role + task for consistent behavior |
| [🗂️ Prompt Patterns](#-prompt-patterns) | Repetitive prompt writing | Use reusable templates and best practices |
| [🧾 Format of the Persona Pattern](#-format-of-the-persona-pattern) | Ambiguous persona prompts | Standardize with “Act as X, Perform Y” format |
| [🧪 Benchmarking & Testing](#-benchmarking--testing) | Inconsistent performance | Test with benchmark queries and evaluation rubrics |
| [🔄 Continuous Learning](#-continuous-learning--staying-connected) | Outdated behavior | Update GPTs regularly with new data and practices |

---

## 📝 Programming a GPT with Instructions
**Problem it Solves:** GPTs can give generic or unfocused responses. Clear instructions ensure they act consistently and stay within scope.

**How it Works:** You define explicit rules in the system instructions, telling the GPT how to behave, what role to take, and what boundaries to follow.

**When to Use:** Anytime you need a GPT to act as a specialist (e.g., tutor, analyst, coach) or when limiting behavior is critical.

**Examples:**
- "You are a math tutor. Always explain concepts step by step for a 14-year-old."  
- "You are a financial analyst. Present risks clearly and avoid legal advice."  

[🔝 Back to Top](#-techniques-at-a-glance)

---

## ⚙️ Custom Instructions
**Problem it Solves:** Users often need answers tailored to their knowledge level or goals.

**How it Works:** Use the Custom Instructions fields to personalize GPT behavior (tone, knowledge, level of detail).

**When to Use:** When deploying a GPT for recurring use cases where context (beginner vs. expert) is essential.

**Examples:**
- User notes: "I am new to Python." → GPT simplifies code explanations.  
- User notes: "I am a project manager." → GPT avoids deep technical jargon.  

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 📚 Retrieval-Augmented Generation (RAG)
**Problem it Solves:** GPTs lack up-to-date or domain-specific knowledge.

**How it Works:** Attach external documents or databases. GPT retrieves relevant info from them when responding.

**When to Use:** Customer support, internal company knowledge, compliance, or technical Q&A.

**Examples:**
- Attach a product manual → GPT answers customer troubleshooting questions.  
- Upload legal policy docs → GPT references them when giving compliance guidance.  

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 🏗️ Putting It All Together
**Problem it Solves:** Instructions, persona, and retrieval are often used separately but need integration for real applications.

**How it Works:** Combine base instructions, persona definition, and retrieval resources into a single GPT configuration.

**When to Use:** When creating a fully functional GPT for a defined role (e.g., customer agent, coach, assistant).

**Examples:**
- "Fitness Coach GPT" → Persona: motivational trainer, Custom Instructions: simplify nutrition advice, RAG: upload exercise library.  
- "Tech Support GPT" → Persona: friendly agent, RAG: attach knowledge base, Instructions: escalate when unsure.  

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 🔧 Understanding GPTs and Tools
**Problem it Solves:** GPTs can’t always answer without external capabilities (e.g., calculations, browsing).

**How it Works:** GPTs are configured to call specific tools when certain types of queries appear.

**When to Use:** For tasks that require external actions (math, APIs, web, coding).

**Examples:**
- GPT with calculator tool → used for numeric queries.  
- GPT with web search → used for news, current events.  

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 🎛️ The CAPITAL Framework
**Problem it Solves:** GPTs can sound too stiff, too casual, or inconsistent in tone.

**How it Works:** Adjust seven dimensions of style: Confidence, Amicability, Professionalism, Interactivity, Transparency, Adaptability, Lexicography.

**When to Use:** Anytime you want GPT responses to align with audience expectations.

**Examples:**
- Customer support → friendly, measured, universal language.  
- Legal advice assistant → formal, measured, consistent, specialized vocabulary.  

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 🎭 Building a Persona Pattern
**Problem it Solves:** GPTs may respond without context or consistent identity.

**How it Works:** Define a persona (role) plus a task to focus responses.

**When to Use:** Training simulations, role-based tutoring, domain-specific advisors.

**Examples:**
- "Act as a nutritionist. Evaluate my daily meals."  
- "Act as a Linux terminal. Respond to my commands."  
- "Act as a travel guide. Recommend activities in Rome."  

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 🗂️ Prompt Patterns
**Concept:** Prompt templates that capture best practices.

For a full catalog of reusable prompt engineering patterns, check out the [Prompt Engineering Patterns Handbook](https://github.com/phodal/prompt-patterns).

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 🧾 Format of the Persona Pattern
**Problem it Solves:** Ambiguous prompts can make GPT lose focus.

**How it Works:** Persona prompts follow two key statements: (1) Act as Persona X, (2) Perform Task Y.

**When to Use:** Anytime you need clarity in role + task definition.

**Examples:**
- "Act as a speech therapist. Assess this child’s speech sample."  
- "Act as a chef. Suggest a recipe with only these ingredients."  

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 🧪 Benchmarking & Testing
**Problem it Solves:** GPTs can perform inconsistently across different inputs.

**How it Works:** Build a set of test queries, define rubrics (accuracy, tone, completeness), and evaluate performance systematically. The course provided a *Testing Protocol PDF* with detailed procedures — include that in your repository for reference.

**When to Use:** Before deploying a GPT in production, especially in sensitive contexts.

**Examples:**
- Customer service GPT: test frustrated customers, incorrect jargon, impossible requests.  
- Language tutor GPT: test slang, cultural references, ambiguous student responses.  

**Recommended Practice:**
- Develop a benchmark set of at least 20–30 test prompts.  
- Rate responses against a rubric: ✅ accuracy, ✅ tone, ✅ completeness, ✅ safety.  
- Re-run tests whenever you change instructions or update RAG documents.  

📘 See the included **Testing Protocol PDF** in this repository for a step-by-step framework.

**Sample Rubric Table:**
| Criteria     | Description | Rating Scale (1-5) |
|--------------|-------------|---------------------|
| Accuracy     | Response factually correct and relevant | 1 = incorrect, 5 = fully correct |
| Tone         | Matches intended style (friendly, formal, etc.) | 1 = inappropriate, 5 = perfect match |
| Completeness | Covers all key aspects of the query | 1 = missing, 5 = fully comprehensive |
| Safety       | Avoids harmful, biased, or sensitive output | 1 = unsafe, 5 = completely safe |

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 🔄 Continuous Learning & Staying Connected
**Problem it Solves:** AI models and best practices evolve quickly.

**How it Works:** Regularly update GPT instructions, knowledge bases, and patterns based on new resources.

**When to Use:** Ongoing maintenance of deployed GPTs.

**Resources:**
- 📘 [Prompt Engineering Paper](https://arxiv.org/abs/2302.11382)  
- 📘 [Living Software Systems Paper](https://arxiv.org/pdf/2408.01768)  
- 📘 [OpenAI Custom GPTs Course](https://www.coursera.org/learn/openai-custom-gpts)  

[🔝 Back to Top](#-techniques-at-a-glance)

---

## 🏁 Final Notes
This handbook is a working reference. Use it to:
- 📝 Draft clear system instructions.
- 🎭 Build personas that match user needs.
- 📚 Attach knowledge sources for retrieval.
- 🎛️ Tune conversation style with the CAPITAL framework.
- 🧪 Test thoroughly with benchmarks.

With these techniques, you can confidently build Custom GPTs that are useful, safe, and aligned with your goals. 🚀

- 📘 [Prompt Engineering Patterns Handbook](https://github.com/phodal/prompt-patterns)

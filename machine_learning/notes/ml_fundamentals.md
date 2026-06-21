## What is Machine Learning?

Machine Learning is a way of building programs that **learn from data** 

### Traditional Programming vs Machine Learning

In **traditional programming**, a human writes the rules:

```
Input + Rules → Output

You write:
  IF price < 5000 AND size > 1000 THEN label = "good deal"
```

In **Machine Learning**, the program figures out the rules itself:

```
Input + Output → Rules (learned automatically)

You give the model:
  - 10,000 house listings
  - Whether each was a good deal or not
  → Model learns its own rules from the patterns
```
---

## ML vs Statistics vs Rule-Based Systems

These three approaches all work with data but have very different goals and philosophies.

| | Rule-Based | Statistics | Machine Learning |
|--|-----------|-----------|-----------------|
| **How it works** | Human-written if/else logic | Mathematical analysis of data | Learns patterns automatically from data |
| **Who writes the logic** | Developer | Analyst (interprets formulas) | The model itself |
| **Goal** | Follow fixed rules | Understand and explain data | Make accurate predictions |
| **Handles complexity** | Poorly | Moderately | Very well |
| **Interpretability** | Very easy | Easy to moderate | Often hard (black box) |
| **Example** | Tax calculation | Finding correlation between age and income | Recommending products |

### Key Distinctions

**Rule-Based vs ML:**
Rules are written by humans and break when reality changes. ML adapts as long as it sees new training data.

**Statistics vs ML:**
Statistics asks *"why does this happen?"* — it focuses on understanding and explaining. ML asks *"what will happen next?"* — it focuses on prediction accuracy, often sacrificing interpretability.

They overlap more than people think. Many ML algorithms (linear regression, logistic regression) are rooted in statistics. The difference is mostly in **intent and application**.

---

## When NOT to Use ML

ML is powerful, but it is not always the right tool. Reaching for it by default is a common mistake.

**Don't use ML when:**

- **The problem has clear, stable rules** — Tax calculations, unit conversions, sorting a list. A simple `if/else` or formula is faster, cheaper, and more reliable.

- **You have very little data** — ML needs examples to learn from. With 50 rows of data, a statistical formula or domain expert will outperform any model.

- **You need full explainability** — In medical diagnosis or legal decisions, you may need to explain exactly *why* a decision was made. Many ML models can't do this reliably.

- **The cost of being wrong is too high** — A spam filter getting it wrong is annoying. An ML model approving a bridge design getting it wrong is catastrophic. High-stakes decisions need human judgment and verified systems.

- **The relationship is straightforward** — If the pattern is simple and linear, a basic formula works fine. ML adds complexity without adding value.

---

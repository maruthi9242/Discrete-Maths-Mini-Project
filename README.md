# 🧠 Discrete Mathematics Logic Processor

A modular application that converts natural language logical statements into propositional logic expressions, simplifies them, and generates truth tables.

---

## 🚀 Features

* 🔤 Converts user-input statements into **propositional logic expressions**
* 🧩 Supports logical operators:

  * AND (∧)
  * OR (∨)
  * NOT (¬)
  * Implication (→)
* ⚙️ Simplifies expressions using **SymPy**
* 📊 Generates **truth tables** for evaluation
* 🏗️ Designed with a **layered architecture**

---

## 🏗️ Architecture

The project follows a modular, multi-layered design:

1. **Parsing Layer**

   * Converts user input into structured propositional logic
   * Handles tokenization and basic syntax interpretation

2. **Simplification Layer**

   * Uses **SymPy** to simplify logical expressions
   * Converts expressions into canonical form

3. **Evaluation Layer**

   * Generates truth tables
   * Evaluates expressions for all possible inputs

---

## 🛠️ Tech Stack

* **Language:** C++ / Python
* **Library:** SymPy (for symbolic logic simplification)

---

## ▶️ How to Run

### Prerequisites

* Python installed (if using SymPy)
* SymPy library:

```bash
pip install sympy
```

### Run the Program

```bash
python main.py
```

---

## 💡 Example

**Input:**

If it rains and I carry an umbrella then I stay dry

**Converted Expression:**

```
(A ∧ B) → C
```

**Simplified Output:**

```
¬(A ∧ B) ∨ C
```

**Truth Table:**

```
A | B | C | Result
-------------------
0 | 0 | 0 | 1
0 | 0 | 1 | 1
...
```

---

## 📚 Concepts Used

* Propositional Logic
* Expression Parsing
* Symbolic Computation
* Truth Table Generation
* Modular System Design

---

## 🔮 Future Improvements

* Add support for more complex logical statements
* Build a simple UI (CLI enhancement or web interface)
* Optimize parser for natural language flexibility

---

## 👨‍💻 Author

Srikar

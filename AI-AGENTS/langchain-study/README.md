# LangChain Study Project

Simple Python project to learn LangChain basics.

## Requirements

* Python 3.10+
* Git
* OpenAI API Key

---

## Setup

Clone repo:

```bash
git clone <repo-url>
cd langchain-study
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

---

## Run Project

Step 1:

```bash
python step1_basic_llm.py
```

---

## Common Issues

### 429 Error

Your OpenAI API quota is exhausted or billing is not enabled.

### Module Not Found

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

---

## Important

Do not commit:

* `.env`
* `venv/`

Make sure `.gitignore` includes:

```gitignore
venv/
.env
__pycache__/
```

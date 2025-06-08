# 🛒 Grocery Store AI Assistant

This is an AI-powered assistant that responds to natural language queries about a grocery store's inventory. It uses OpenAI GPT-4 via LangChain for intelligent responses and is designed to be easily extended for voice interaction, UI integration (e.g., Streamlit), or database-backed systems.

---

## 🚀 Features

- 🧠 Understands natural language queries like “What are the best deals today?”
- 📦 Dynamically summarizes product data including stock, price, and discounts
- 🤖 Powered by OpenAI GPT-4 and LangChain for advanced language processing
- 🧱 Modular and extensible for frontend, database, or voice integration

---

## 🧰 Technologies Used

- **Python 3.8+**
- [OpenAI GPT-4](https://platform.openai.com/docs/)
- [LangChain](https://python.langchain.com/)
- (Optional) [Streamlit](https://streamlit.io/) for UI
- (Future) OpenAI Whisper for voice input

---

## 📁 Project Structure
GroceryStore/
├── Langchain.py # Core logic: LangChain prompt and GPT-4 integration
├── main.py # Application entry point; loads data and handles queries
├── inventory.json # (Optional) Inventory data source
├── .env # Stores your OpenAI API key securely (not committed)
├── requirements.txt # Python dependencies
├── README.md # Project documentation (you’re reading it)
└── .venv/ # (Optional) Python virtual environment

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the model
llm = ChatOpenAI(
    openai_api_key=os.environ['OPENAI_API_KEY'],
    model_name='gpt-4',
    temperature=0
)

# Prompt template
template = """
You are an AI assistant for a grocery store inventory system.
User query: {query}

Here are some relevant products from the inventory:
{products}

Answer the user query based on this data.
"""

prompt = PromptTemplate(input_variables=["query", "products"], template=template)

# LLM Chain
chain = LLMChain(llm=llm, prompt=prompt)

# Function to query the model
def ask_gpt(query, products):
    products_text = "\n".join([
        f"{p['product_name']}: Price ${p['price']}, Stock {p['quantity']}, Discount {p.get('discount_percent', 'None')}"
        for p in products
    ])
    return chain.run({"query": query, "products": products_text})


import streamlit as st
from embbedding import load_faiss_index, semantic_search
from Langchain import ask_gpt
from database import add_product, update_stock, update_discount

st.title("Grocery Store AI Inventory Assistant")

index, products = load_faiss_index()

# --- User Query Section ---
st.header("Ask about products")
query = st.text_input("Enter your question about products or inventory:")

if query:
    top_products = semantic_search(query, index, products)
    answer = ask_gpt(query, top_products)
    st.markdown("### AI Answer:")
    st.write(answer)

    st.markdown("### Top matching products:")
    for p in top_products:
        st.write(f"{p['product_name']} - ${p['price']} - Stock: {p['quantity']} - Discount: {p.get('discount_percent', 'None')}")

# --- Admin Dashboard ---
st.sidebar.header("Admin Dashboard")

with st.sidebar.expander("Add New Product"):
    name = st.text_input("Product Name", key="prod_name")
    category = st.text_input("Category", key="prod_cat")
    price = st.number_input("Price", min_value=0.01, key="prod_price")
    if st.button("Add Product"):
        add_product(name, category, price)
        st.success(f"Product '{name}' added! Please restart app to update index.")

with st.sidebar.expander("Update Stock"):
    prod_id = st.number_input("Product ID", min_value=1, step=1, key="stock_id")
    quantity = st.number_input("Quantity", min_value=0, step=1, key="stock_qty")
    if st.button("Update Stock"):
        update_stock(prod_id, quantity)
        st.success(f"Stock updated for product ID {prod_id}.")

with st.sidebar.expander("Add Discount"):
    prod_id_d = st.number_input("Product ID", min_value=1, step=1, key="disc_id")
    discount = st.number_input("Discount Percent", min_value=0.0, max_value=100.0, step=0.1, key="disc_percent")
    start_date = st.date_input("Start Date", key="disc_start")
    end_date = st.date_input("End Date", key="disc_end")
    if st.button("Add Discount"):
        update_discount(prod_id_d, discount, start_date, end_date)
        st.success(f"Discount added for product ID {prod_id_d}.")
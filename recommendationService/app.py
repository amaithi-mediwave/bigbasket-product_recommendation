import streamlit as st
import pandas as pd 


df = pd.read_csv('recommendationService/recommend.csv')

product_indices = pd.Series(df.index, index=df['product'])



# Sample product data
products = [
    {"name": "vinoth", "description": "Description of Product 1"},
    {"name": "magizh", "description": "Description of Product 2"},
    {"name": "arun", "description": "Description of Product 3"},
    # Add more products as needed
]

# Function to search for products based on a query
def search_products(query):
    return df[df["product"].str.lower().str.contains(query.lower())]

# Streamlit app
def main():
    st.title("Big Basket")

    # Real-time search input
    search_query = st.text_input("Search for products:", key="search")

    # Display products based on search
    if search_query:
        search_results = search_products(search_query)
        if not search_results:
            st.warning("No products found.")
        else:
            st.subheader("Search Results:")
            for product in search_results:
                # Button for each search result
                if st.button(f"View Details for {product['name']}"):
                    st.subheader("Product Details:")
                    st.write(f"**{product['name']}** - {product['description']}")
    else:
        # Display all products if no search query
        st.subheader("All Products:")
        for product in products:
            # Button for each product
            if st.button(f"View Details for {product['name']}"):
                st.subheader("Product Details:")
                st.write(f"**{product['name']}** - {product['description']}")

if __name__ == "__main__":
    main()

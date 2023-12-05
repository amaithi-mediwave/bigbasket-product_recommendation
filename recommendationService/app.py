import streamlit as st

# Sample product data
products = [
    {"name": "vinoth", "description": "Description of Product 1"},
    {"name": "magizh", "description": "Description of Product 2"},
    {"name": "arun", "description": "Description of Product 3"},
    # Add more products as needed
]

# Function to search for products based on a query
def search_products(query):
    return [product for product in products if query.lower() in product["name"].lower()]

# Streamlit app
def main():
    st.title("Big Basket")

    # Search bar
    search_query = st.text_input("Search for products:")
    
    # Display products based on search
    if search_query:
        search_results = search_products(search_query)
        if not search_results:
            st.warning("No products found.")
        else:
            st.subheader("Search Results:")
            for product in search_results:
                st.write(f"**{product['name']}** - {product['description']}")
    else:
        # Display all products if no search query
        st.subheader("All Products:")
        for product in products:
            st.write(f"**{product['name']}** - {product['description']}")

if __name__ == "__main__":
    main()

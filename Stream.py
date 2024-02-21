import streamlit as st
from dotenv import load_dotenv
import os

# Return the result of the SQL query from sql_retrieve.
from sql_retriever import sql_retrieve

def main():
    st.title('SQL Information Retrieval Dashboard')

    # Text input for query
    query_text = st.text_area("Enter your query about the orders")

    if st.button("Retrieve Information"):
        if query_text:  # Ensure the query is not empty
            # Call the modified sql_retrieve function with the user's query
            try:
                response = sql_retrieve(query_text)
                if response:
                    st.write(response)
                else:
                    st.write("No information found for the given query.")
            except Exception as e:
                st.write(f"An error occurred: {e}")
        else:
            st.write("Please enter a query to retrieve information.")

if __name__ == "__main__":
    main()

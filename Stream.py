import streamlit as st
from dotenv import load_dotenv
import os

# Return the result of the SQL query from sql_retrieve.
from sql_retriever import sql_retrieve

# st.set_page_config(page_title="SQL Information Retrieval Dashboard", layout="wide")

# st.title("SQL Information Retrieval Dashboard")

# with st.form(key='query_form'):
#     query_input = st.text_input("Enter your query about the orders", help="Type your SQL query or use common phrases for data retrieval.")
#     submit_button = st.form_submit_button(label="Retrieve Information")

# if submit_button:
#     with st.spinner('Retrieving data...'):
#         # Your code to handle the query and retrieve information
#         output_data = "There are 4632 unique stock codes in the data."
#         st.success("Query successful!")
#         st.json({"input": query_input, "output": output_data})
# else:
#     st.info("Enter a query to retrieve information.")

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
                    # Change 'response' from dictionary with 'input' and 'output' keys
                    st.write("Query:", response.get("input"))
                    st.write("Result:", response.get("output"))
                else:
                    st.write("No information found for the given query.")
            except Exception as e:
                st.write(f"An error occurred: {e}")
        else:
            st.write("Please enter a query to retrieve information.")

if __name__ == "__main__":
    main()

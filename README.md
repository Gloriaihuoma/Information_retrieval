# SQL Information Retrieval Dashboard

## Overview

This project is designed to empower frontline employees by enabling them to retrieve information directly from customer databases using simple English queries. This system eliminates the need for technical SQL knowledge, streamlining customer service processes and reducing dependency on IT departments for data retrieval tasks.

## Features

- **User-Friendly Interface**: A simple and intuitive dashboard allows users to enter queries in natural language.
- **Real-Time Data Retrieval**: Directly fetches data from the database, offering immediate responses to queries.
- **Secure Access**: Ensures data security and access control, allowing only authorized personnel to view or retrieve customer information.

## Installation
To install the necessary dependencies for the SQL Information Retrieval Dashboard, you can use the following command in your terminal:

``` bash
Copy code
pip install -r requirements.txt
```
Make sure that the requirements.txt file is in your current directory and contains all the necessary package names and versions required for the project. This will ensure a streamlined setup and help you avoid manually entering each package.


## Usage

After installation, you can start the dashboard by running the following command in your terminal:

```bash
streamlit run app.py
```

This will launch the SQL Information Retrieval Dashboard in your default web browser. Simply enter your query about the orders or other customer data in the provided text area and click "Retrieve Information" to get the desired results.

## Technical Details

- **Language Models**: Utilizes OpenAI's GPT models to process natural language queries and convert them into executable SQL commands.
- **Database Integration**: Connects seamlessly to SQL databases using SQLAlchemy for diverse database management systems support.
- **Vector Storage**: FAISS for efficient similarity search in high-dimensional spaces, ensuring accurate retrieval of information related to the query.


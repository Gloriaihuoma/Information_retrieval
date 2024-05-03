# SQL Information Retrieval Dashboard

## Overview

This project is designed to empower frontline employees by enabling them to retrieve information directly from customer databases using simple English queries. This system eliminates the need for technical SQL knowledge, streamlining customer service processes and reducing dependency on IT departments for data retrieval tasks.

## Features

- **User-Friendly Interface**: A simple and intuitive dashboard allows users to enter queries in natural language.
- **Real-Time Data Retrieval**: Directly fetches data from the database, offering immediate responses to queries.
- **Secure Access**: Ensures data security and access control, allowing only authorized personnel to view or retrieve customer information.

## Installation

To set up the SQL Information Retrieval Dashboard, ensure that the following dependencies are installed:

```bash
pip install aiohttp aiosignal annotated-types anyio async-timeout attrs certifi charset-normalizer colorama dataclasses-json distro exceptiongroup faiss-cpu frozenlist greenlet h11 httpcore httpx idna jsonpatch jsonpointer langchain langchain-community langchain-core langchain-openai langsmith marshmallow multidict mypy-extensions numpy openai packaging pandas pydantic pydantic_core PyMySQL python-dateutil python-dotenv pytz PyYAML regex requests six sniffio SQLAlchemy tenacity tiktoken tqdm typing-inspect typing_extensions tzdata urllib3 yarl
```

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


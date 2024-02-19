from langchain.agents import AgentType, create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def sql_retrieve():

    few_shots = {
        "List all orders": "SELECT * FROM orders;",
        "Find orders with a specific StockCode (e.g., StockCode '85048')": "SELECT * FROM orders WHERE StockCode = '85048';",
        "List all orders from a specific country (e.g., 'United Kingdom')": "SELECT * FROM orders WHERE Country = 'United Kingdom';",
        "Find orders with a specific Description (e.g., 'PINK CHERRY LIGHTS')": "SELECT * FROM orders WHERE Description = 'PINK CHERRY LIGHTS';",
        "How many orders are there": "SELECT COUNT(*) FROM orders;",
        "List all orders with a specific Quantity (e.g., Quantity 12)": "SELECT * FROM orders WHERE Quantity = 12;",
        "Who are the customers from a specific country (e.g., 'United Kingdom')": "SELECT DISTINCT `Customer ID` FROM orders WHERE Country = 'United Kingdom';",
        "List all orders with a price above a certain value (e.g., Price > 5.00)": "SELECT * FROM orders WHERE Price > 5.00;",
        "Find orders from a specific InvoiceDate (e.g., '12/1/2009 7:45')": "SELECT * FROM orders WHERE InvoiceDate = '12/1/2009 7:45';",
        "Find orders with a description that includes a specific phrase (e.g., Description includes 'LIGHTS')": "SELECT * FROM orders WHERE Description LIKE '%LIGHTS%';",
    }

    embeddings = OpenAIEmbeddings()

  
    few_shot_docs = [
        Document(page_content=question, metadata={"sql_query": few_shots[question]})
        for question in few_shots.keys()
    ]
    vector_db = FAISS.from_documents(few_shot_docs, embeddings)
    retriever = vector_db.as_retriever()

    host = os.getenv("localhost")
    user_name = os.getenv("user_name")
    password = os.getenv("password")
    database = os.getenv("database")

    # Connect to the database
    try:
        db = SQLDatabase.from_uri("sqlite:///mydatabase.db")
    except:
        db = f"mysql+pymysql://{user_name}:{password}@{host}/{database}"
        
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    custom_suffix = """
                        I should first get the similar examples I know.
                        If the examples are enough to construct the query, I can build it.
                        Otherwise, I can then look at the tables in the database to see what I can query.
                        Then I should query the schema of the most relevant tables
                    """

    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        suffix=custom_suffix,
    )
    agent.invoke("How many orders in United Kingdom?")


sql_retrieve()
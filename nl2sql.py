from langchain_community.utilities.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# load the environment variables from .env file
load_dotenv()

# Connect the database 
db = SQLDatabase.from_uri("sqlite:///db/company.sqlite3")

# get the basic info from the database and tables
# print(db.dialect)
# print(db.get_usable_table_names())
# print(db.table_info)

# define llm
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, verbose=True)

# Generate query chain
generate_query = create_sql_query_chain(llm, db)

# invoke the chain to get the query
query = generate_query.invoke({"question": "What is the price of 1968 Ford Mustang like car?"})
print("--- Generated Query ----")
print(query)
print("--------------")

execute_query = QuerySQLDataBaseTool(db=db)
result = execute_query.invoke(query)
print(result)

# chain = generate_query | execute_query
# response = chain.invoke({"question": "What is the price of 1968 Ford Mustang?"})
# print(response)
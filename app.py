from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Response
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory import ChatMessageHistory
from langchain_core.messages import messages_to_dict, messages_from_dict
from langchain_community.utilities import SQLDatabase
import sqlite3
import os
from sqlalchemy import exc as sa_exc
import warnings
import json
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import openai
load_dotenv()
# Initialize FastAPI app
app = FastAPI()
 #Define allowed origins (Adjust as needed)
origins = [
  "http://localhost:3000",  # Assuming React app runs on this port
  # Add other origins as needed
]
 
# Add CORS middleware to the application
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
 
# Set your OpenAI API key

from dotenv import load_dotenv
load_dotenv()

openai.api_key=os.environ["OPENAI_API_KEY"]
# Initialize the database connection
 
 
# Define SQLite database connection
conn = sqlite3.connect('Hotel_Dtabase.db')
cursor = conn.cursor()
 
# Endpoint to receive room number
@app.get("/roomno/{roomno}")
async def fetch_room_details(roomno: int):
    try:
        # Query the SQLite database to get details for the provided room number
        cursor.execute("SELECT Booking_id,firstname FROM Hotel_service WHERE roomno=?", (roomno,))
        result = cursor.fetchone()
        #print(result)
 
        if result:
            # If details are found, construct the response data
            data_to_return = {"roomno": roomno, "Booking_id": result[0], "firstname": result[1]}
            # Serialize the response data to JSON
            serialized_document = json.dumps(data_to_return)
            # Return the serialized document
            return Response(content=serialized_document, media_type="application/json")
        else:
            # If no details found for the provided room number, raise an HTTPException
            raise HTTPException(status_code=404, detail="Room details not found")
 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
class QueryResponse(BaseModel):
    message: str
 #Create the prompt object
  

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=sa_exc.SAWarning)
    # Initialize the database connection
    db = SQLDatabase.from_uri('sqlite:///Hotel_Dtabase.db')
def get_schema(_):
    return db.get_table_info()
 
# Define Pydantic model for request data
class QueryRequest(BaseModel):
    roomno: int
    query: str
 
# Define Pydantic model for response data
class QueryResponse(BaseModel):
    message: str
 
# Define the prompt template
template1 = """
Based on the table schema below, write a SQL query that would answer the user's question.
 
{schema}
{user_memory}
example1:
Question:what is my checkin time my roomno is {roomno} ?
SQL Query : SELECT check_in_time from Hotel_service where {roomno}==roomno;
example2:
Question:can i get extra bed?
SQL Query:SELECT extra_bed from Hotel_resources WHERE extra_bed>0; response we will provide you shortly
Question: {question}
SQL Query:
"""
 
# Create the prompt object
prompt1 = ChatPromptTemplate.from_template(template1)
llm = ChatOpenAI()
 
sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt1
    | llm.bind(stop="\nSQL Result:")
    | StrOutputParser()
)
print(sql_chain)
def get_sql_query(question, roomno, user_memory):
    return sql_chain.invoke({"question": question, "roomno": roomno, "user_memory":user_memory})
template2 = """ Based on the table schema below for room number {roomno}, question and the fetched answer, respond as a friendly assistant : 
{schema} 

Question: {question} 
{user_memory}
Answer: {response} 
"""

prompt2 = ChatPromptTemplate.from_template(template2)
 
# Function to run SQL query
def run_query(query):
    return db.run(query)
def get_response(question, roomno,user_memory):
    sql_query = get_sql_query(question, roomno, user_memory)
    response = run_query(sql_query)
    return response
full_chain = (
    RunnablePassthrough.assign(
        query=lambda vars: get_sql_query(vars["question"], vars["roomno"], vars["user_memory"]),
        schema=get_schema,
        response=lambda vars: get_response(vars["question"], vars["roomno"], vars["user_memory"]),
        roomno=lambda vars: vars["roomno"]
    )
    | prompt2
    | llm
    | StrOutputParser()
)
categorization_prompt_template1 = """ You are an expert in categorizing input into two categories: "user query type" and "general question text type" for a hotel database based on the question and room number provided.

"User query type" refers to questions that involve specific requests or inquiries related to the guest's room or stay at the hotel. Examples include:
- For room number {roomno}, can you extend my check-out date to 15-05-24?
- For room number {roomno}, can you provide me an extra bed?
- For room number {roomno}, do you have extra bedsheets available?
- For room number {roomno}, can I have an extra soap bar?
- For room number {roomno}, can I have the WiFi password?
- For room number {roomno}, what is the reception number?
- For room number {roomno}, can I request a late check-out?
- For room number {roomno}, what is  hotel name?
- For room number {roomno}, what is  hotel address?
- For room number {roomno}, what is  hotel pin?
- For room number {roomno}, what is  hotel email?

"General question text type" refers to questions or statements that are not directly related to a specific guest's room or stay, but rather general inquiries or comments. Examples include:
- What dining options (restaurants, cafes, bars) are available?
- What recreational facilities (swimming pools, fitness centers, sports courts) do you have?
- What entertainment and activities (game rooms, kids' play areas, organized programs) are offered?
- Do you have parking facilities? Any other amenities like a spa or business center?


Input: {input_text}
Room Number: {roomno}

Categorization: """
categorization_prompt1 = PromptTemplate(
    template=categorization_prompt_template1,
    input_variables=["input_text", "roomno"],
)
llm_openai = ChatOpenAI(model='gpt-3.5-turbo')
categorization_chain1 = LLMChain(llm=llm_openai, prompt=categorization_prompt1,verbose=True)
categorization_prompt_template = """
You are an expert in categorizing input into two categories: "yes/no type question" and "providing data question" for a hotel database based on the question and room number provided.
 
"Yes/no type question" refers to questions that can be answered with a simple "yes" or "no" and may involve requests related to the guest's room. Examples include:
- For room number {roomno}, can you extend my check-out date to 15-05-24?
- For room number {roomno}, can you provide me an extra bed?
- For room number {roomno}, do you have extra bedsheets available?
- For room number {roomno}, can I have an extra soap bar?
 
"Providing data question" refers to questions that require providing factual information or data from the hotel database based on the room number. Examples include:
- For room number {roomno}, what is my check-in time?
- For room number {roomno}, what amenities are included in the room?
- For room number {roomno}, can you tell me the names of the guests staying in this room?
- For room number {roomno}, what is my hotel name?
- For room number {roomno}, what is  hotel email?


 
Input: {input_text}
Room Number: {roomno}
 
Categorization:
"""
 
categorization_prompt = PromptTemplate(
    template=categorization_prompt_template,
    input_variables=["input_text", "roomno"],
)
llm_openai = ChatOpenAI(model='gpt-3.5-turbo')
categorization_chain = LLMChain(llm=llm_openai, prompt=categorization_prompt,verbose=True)


keyword_nl_template = """You are an expert in categorizing input into three categories: "normal question", "yes confirm question", and "no don't confirm question" for a hotel database based on the question and room number provided. 

"Normal question" refers to general questions or requests that do not involve confirmation or denial. Examples include: 
- For room number {roomno}, can you provide me an extra bed? 
- For room number {roomno}, what is my check-in time?
- For room number {roomno}, can i get extra bed?

"Yes confirm question" refers to questions or requests that require confirmation from the user. Examples include:
- For room number {roomno}, can you extend my check-out date to 15-05-24?
- For room number {roomno}, do you have extra bedsheets available?

"No don't confirm question" refers to questions or requests where the user explicitly denies or does not want to proceed. Examples include:
- For room number {roomno}, I don't need an extra bed anymore.
- For room number {roomno}, no, I won't be extending my stay.

Input: {input_text}
Room Number: {roomno}

Categorization and 
Response:"""

keyword_nl_prompt = PromptTemplate(template=keyword_nl_template, input_variables=["input_text", "roomno"],)
keyword_nl_chain = LLMChain(llm=llm_openai, prompt=keyword_nl_prompt, verbose=True)
normal_question_prompt = PromptTemplate.from_template(
    """You are an expert in handling normal questions or requests for a hotel database based on the room number provided. 
    Normal questions or requests do not involve confirmation or denial, and they can be general inquiries or requests. 
    Please provide a suitable response to the following request:
    \n\nInput: {input_text}\nRoom Number: {roomno}
    {user_memory}
    \n\nResponse:"""
)

# yes_confirm_question_prompt = PromptTemplate.from_template(
#     """You are an expert in handling requests that require confirmation from the user for a hotel database based on the room number provided. 
#     These requests involve extending stays, requesting additional items or services, etc.
#     Please confirm if you can accommodate the following request:\n\nInput: {input_text}\nRoom Number: {roomno}\n\nConfirmation:"""
# )
# yes_confirm_question_prompt = PromptTemplate.from_template(
#     """You are an expert in handling requests that require confirmation from the user for a Hotel_dtabase based on the room number provided. These requests involve extending stays, requesting additional items or services, updating the check-out date, etc. Please confirm if you can accommodate the following request go and update in hotel_resources table:

# Input: {input_text}
# Room Number: {roomno}

# Confirmation:"""
# )
yes_confirm_question_prompt = PromptTemplate.from_template(
    """You are an expert in handling requests that require confirmation from the user for a Hotel_dtabase based on the room number provided. These requests involve extending stays, requesting additional items or services, updating the check-out date, etc. Please confirm if you can accommodate the following request:
 
Input: {input_text}
Room Number: {roomno}
{user_memory}
Confirmation:"""
)

# no_confirm_question_prompt = PromptTemplate.from_template(
#     """You are an expert in handling situations where the user explicitly denies or does not want to proceed with a request for a hotel database based on the room number provided. 
#     Please acknowledge and provide a suitable response to the following denial:\n\nInput: {input_text}\nRoom Number: {roomno}\n\nResponse:"""
# )
no_confirm_question_prompt = PromptTemplate.from_template(
    """You are an expert in handling situations where the user explicitly denies or does not want to proceed with a request for a hotel database based on the room number provided.
    Please acknowledge and provide a suitable response to the following denial:\n\nInput: {input_text}\nRoom Number: {roomno}
    {user_memory}
    \n\nResponse: Thank you for your response. I understand you do not wish to proceed with the request related to the hotel database and the provided room number. Please feel free to let me know if there are any other services or assistance I can provide."""
)
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

General_question_prompt = """You are the hotel manager responding to the guest's specific inquiry: "{input_text}"

Please provide a concise and relevant response directly addressing the guest's question or comment about the hotel's amenities, facilities, or services. Do not include any additional information beyond what is necessary to answer the specific query.
{user_memory}
Room Number: {roomno}

Response:
"""

# Create a PromptTemplate from the General_question_prompt string
general_question_template = PromptTemplate(
    input_variables=["input_text", "roomno","user_memory"],
    template=General_question_prompt,
)

# Create the LLM instance
llm = OpenAI(temperature=0.9)

# Create the LLMChain instance with the PromptTemplate
general_question_chain = LLMChain(llm=llm, prompt=general_question_template)

# Use the general_question_chain as needed

def handle_request(input_text, roomno,user_memory):
    # Get the categorization from the keyword_nl_chain
    categorization = keyword_nl_chain.run(input_text=input_text, roomno=roomno)["result"].split("\n")[0]

    # Route the input based on the categorization
    if categorization == "normal question":
        return normal_question_prompt.run(input_text=input_text, roomno=roomno,user_memory=user_memory)["result"]
    elif categorization == "yes confirm question":
        return yes_confirm_question_prompt.run(input_text=input_text, roomno=roomno,user_memory=user_memory)["result"]
    elif categorization == "no don't confirm question":
        return no_confirm_question_prompt.run(input_text=input_text, roomno=roomno,user_memory=user_memory)["result"]
    else:
        return "Invalid categorization."
 
def serialize(memory, booking_id: str):
    """
    Serializes the conversation memory into a dictionary and saves it to the database.
    """
    # Load the current conversation history
    messages = memory.load_memory_variables({})["user_memory"]
   
    # Convert messages to a dictionary
    message_dict = messages_to_dict(messages)
   
    # Serialize the dictionary to JSON
    serialized_data = json.dumps(message_dict)
   
    # Store the serialized data in the database
    conn = sqlite3.connect('Hotel_Dtabase.db')
    cursor = conn.cursor()
    #cursor.execute("""CREATE TABLE IF NOT EXISTS user_history (booking_id TEXT PRIMARY KEY, message TEXT)""")
    cursor.execute("""REPLACE INTO user_history (booking_id, message) VALUES (?, ?)""", (booking_id, serialized_data))
    conn.commit()
    conn.close()
memory = ConversationBufferMemory(memory_key="user_memory", return_messages=True)
def deserialize(booking_id: str):
    """
    Deserializes the conversation memory from the database and loads it into the memory.
    """
    # Query the database for the serialized chat history
    conn = sqlite3.connect('Hotel_Dtabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM user_history WHERE booking_id=?", (booking_id,))
    result = cursor.fetchone()
    print("result : ",result)
    conn.close()
 
    if result and result[0]:
        # Deserialize the JSON string back into a dictionary
        message_dict = json.loads(result[0])
       
        # Convert the dictionary back into a list of messages
        messages = messages_from_dict(message_dict)
        print("message history ",messages)
       
        # Load the messages into the conversation memory
        retrieved_chat_history = ChatMessageHistory(messages=messages)
        memory.chat_memory = retrieved_chat_history
        print("Deserialized chat history loaded into memory.")
       
    else:
        print("No chat history found for this booking.")
        
@app.get("/process_query/{text}")
async def process_query(text: str):
    try: # Parse the JSON data
        data = json.loads(text)
        room = data.get('room')
        book_id=data.get('book_id')
        message = data.get('message')
        # Check if room is provided and is a valid integer
        if room is None:
            raise HTTPException(status_code=400, detail="Room number is required.")
        try: room_number = int(room)
        except ValueError: raise HTTPException(status_code=400, detail="Invalid room number.") 
        categorization_result = categorization_chain1.run({"input_text": message, "roomno": room_number})
        print(categorization_result)
        if categorization_result == "User query type":
            categorization_result1 = categorization_chain.run({"input_text": message, "roomno": room_number})
            if categorization_result1 == "Yes/no type question":
                deserialize(book_id)
            # response = keyword_nl_prompt.invoke({"question": message, "roomno": room_number, "user_memory": memory.load_memory_variables({})["user_memory"]})
                #
                response = handle_request(message,room_number,memory.load_memory_variables({})["user_memory"])
                memory.save_context(inputs={"input": message}, outputs={"output": response})
                serialize(memory, book_id)
                return response
            # memory.save_context(inputs={"input": message}, outputs={"output": response})
            # serialize(memory, book_id)
            else:
                deserialize(book_id)
                response = full_chain.invoke({"question": message, "roomno": room_number, "user_memory":memory.load_memory_variables({})["user_memory"]})
                memory.save_context(inputs={"input": message}, outputs={"output": response})
                serialize(memory, book_id)
                return QueryResponse(message=response)
        else:
            deserialize(book_id)
            response = general_question_chain.run(input_text=message, roomno=room_number,user_memory= memory.load_memory_variables({})["user_memory"])
            memory.save_context(inputs={"input": message}, outputs={"output": response})
            serialize(memory, book_id)
            return {"message": response}
            
             
            # Invoke the full_chain to get the final response
        # response = full_chain.invoke({"question": message, "roomno": room_number}) # Return the response
        
    except Exception as e: raise HTTPException(status_code=500, detail=str(e)) # Other endpoints":
            # "Yes/no type question" case
           

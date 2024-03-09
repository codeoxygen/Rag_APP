
import os
from helper_functions import pipeline
from chat_model import BuildConversationChain
from dotenv import load_dotenv
from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain


load_dotenv()
LLAMA_API_KEY = os.environ.get("LLAMA_API_KEY")
LLAMA = LlamaAPI(LLAMA_API_KEY)

chat_llm = ChatLlamaAPI(client=LLAMA)


vectorstore = pipeline("./Data/Lahiru Jayakodi CV.pdf")



conversation_chain = BuildConversationChain(vectorstore , chat_llm)

print(conversation_chain.run("What are the skills related about Lahiru"))

import os
import openai
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain




def BuildConversationChain(vectorstore , chat_llm):
    memory = ConversationBufferMemory(
                                    memory_key='chat_history', 
                                    return_messages=True,
                                    max_history_length=2
                                    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
                                                            llm=chat_llm,
                                                            retriever=vectorstore.as_retriever(),
                                                            memory=memory,
                                                            )
    return conversation_chain



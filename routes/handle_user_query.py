import os
from flask import Blueprint, request, jsonify
from Services.helper_functions import pipeline
from Services.chat_model import BuildConversationChain
from flask import current_app
from flask import session
from flask_caching import Cache  
from langchain_experimental.llms import ChatLlamaAPI



user_query_bp = Blueprint("user_query", __name__)

@user_query_bp.route("/message", methods=["POST"])
def handle_user_query():
    chat_llm = current_app.chat_llm
    cache = current_app.cache
    pdf_text = session.get("pdf_text")

    if pdf_text is None :
        return jsonify({"error": "No PDF text provided"}), 400
    
    conversation_chain = cache.get('conversation_chain')
    if conversation_chain is None :
        print("Running again")
        vectorstore = pipeline(pdf_text)
        conversation_chain = BuildConversationChain(vectorstore , chat_llm)
        cache.set('conversation_chain', conversation_chain)
    
    user_message = request.json.get('message')
    print("Without initializing")
    if user_message is None:
        return jsonify({"error": "No message provided"}), 400

    rag_response = conversation_chain.run(user_message)
    return jsonify({"message": rag_response}), 200
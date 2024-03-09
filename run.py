from flask import Flask
import os
from routes.upload_pdf import upload_pdf_bp
from routes.handle_user_query import user_query_bp
#from routes import handle_user_query
from dotenv import load_dotenv
from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI
from flask_caching import Cache  

app = Flask(__name__)
app.secret_key = '1234' 

load_dotenv()
LLAMA_API_KEY = os.environ.get("LLAMA_API_KEY")
LLAMA = LlamaAPI(LLAMA_API_KEY)
cache = Cache(app, config={"CACHE_TYPE" : 'simple'})

app.cache = cache
app.chat_llm = ChatLlamaAPI(client=LLAMA)



app.register_blueprint(upload_pdf_bp)
app.register_blueprint(user_query_bp)

if __name__ == "__main__":
    app.run(debug = True)

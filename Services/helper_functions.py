from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS
from PyPDF2 import PdfReader
import io



llm_embeddings = HuggingFaceBgeEmbeddings(
                                        model_name = "BAAI/bge-small-en",
                                        model_kwargs = {'device': 'mps'},
                                        encode_kwargs = {'normalize_embeddings': False}
                                        )


def PdfUtils(file):
    pdf_to_io = io.BytesIO(file.read())
    pdf_reader = PdfReader(pdf_to_io)
    text = ""
    pages= pdf_reader.pages
    for page in pages :
        text += page.extract_text()
    
    return text

def GetChunks(text : str):
    text_splitter = CharacterTextSplitter(
                                    separator="\n",
                                    chunk_size=200,
                                    chunk_overlap=50,
                                    length_function=len
                                        )
    chunks = text_splitter.split_text(text)
    return chunks



def VectorStoring(llm_embeddings, text_chunks):
    vectorstore = FAISS.from_texts(
                        texts = text_chunks ,
                        embedding = llm_embeddings
                        )
    return vectorstore
    
def pipeline(text):
    text_chunks = GetChunks(text)
    vector_store = VectorStoring(llm_embeddings , text_chunks)
    return vector_store


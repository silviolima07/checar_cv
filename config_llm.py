# config.py
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()



# Obter a chave da API GROQ
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

llama = ChatGroq(
            api_key=GROQ_API_KEY,
            model= "llama3-70b-8192",
            timeout=180
        )
        
mixtral = ChatGroq(
            api_key=GROQ_API_KEY,
            model= "mixtral-8x7b-32768",
            timeout=180
        )

gemma = ChatGroq(
            api_key=GROQ_API_KEY,
            model= "gemma-7b-it",
            timeout=180
        )        

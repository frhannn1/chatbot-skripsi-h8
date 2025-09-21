import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load API key dari .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# 1. Definisikan LLM
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3
)

# 2. Buat memory untuk simpan konteks percakapan
memory = ConversationBufferMemory(return_messages=True)

# 3. Prompt template dengan placeholder untuk history
prompt = ChatPromptTemplate.from_messages([
    ("system", "Kamu adalah asisten panduan skripsi mahasiswa. "
               "Jawablah dengan jelas, sistematis, dan sesuai aturan panduan skripsi. "
               "Gunakan bahasa Indonesia formal."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# 4. Chain percakapan
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)

# 5. Fungsi chatbot
def ask_bot(query: str):
    result = conversation.invoke({"input": query})
    return result["response"]

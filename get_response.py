from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm=ChatGroq(model="llama-3.1-8b-instant",
             temperature=0,
             max_tokens=None,
             max_retries=2
)

def get_answer(question):
    answer=llm.invoke(question)
    answer=answer.content
    return answer


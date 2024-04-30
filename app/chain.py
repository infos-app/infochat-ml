import os

import dotenv
from langchain import hub
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

model = ChatOpenAI(base_url=os.getenv("OPENAI_URL"), streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI Assistant. Your name is '테디'. You must answer in Korean.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


def retrieve_answer(question):
    return {"question": question, "context": "France is in Europe."}


chain = prompt | model | StrOutputParser()

from secret_stuff import OPENAI_API_KEY

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
)
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


human_input = input("Ask: ")
chat = ChatOpenAI(streaming=True, 
                  callbacks=[StreamingStdOutCallbackHandler()], 
                  temperature=0, openai_api_key=OPENAI_API_KEY)
resp = chat([HumanMessage(content=human_input)])
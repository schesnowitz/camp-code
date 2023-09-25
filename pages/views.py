from django.shortcuts import render
from django.http import HttpResponse

from django.http.response import StreamingHttpResponse
from secret_stuff import OPENAI_API_KEY

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
)
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def index(request):
    return render(request=request, template_name="pages/index.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")

def chat(request):

    chat = ChatOpenAI(streaming=True, 
                  callbacks=[StreamingStdOutCallbackHandler()], 
                  temperature=0, openai_api_key=OPENAI_API_KEY)
    
    if request.method == "POST":
        human_input = request.POST.get('human-input')
        print(human_input)
        ai_response = chat([HumanMessage(content=human_input)])
        response = StreamingHttpResponse(chat, status=200, content_type='text/event-stream')





        return render(request, "pages/chat.html", context={"human_input" : human_input,
                                                     "ai_response" : response})
import streamlit as st
import random
import time
from dotenv import load_dotenv
import os 
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from langchain_ibm import WatsonxLLM
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()



api_key = os.getenv('WATSONX_API_KEY')

credentials = Credentials(
    url="https://eu-de.ml.cloud.ibm.com",
    api_key=api_key,
)

project_id = os.environ["WATSONX_PROJECT_ID"]


# app config
st.title("HeroKimit Egyptian AI Assistant المساعد الرقمي هيروكيميت𓀛")

# Authentication check
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("Unauthorized access. Please log in first.")
    st.stop()

def get_response(user_query, chat_history):

    template = """
جاوب السؤال بدقه: 
    السؤال: {user_question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    parameters = {
    GenParams.DECODING_METHOD: DecodingMethods.SAMPLE.value,
    GenParams.MAX_NEW_TOKENS: 900,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.TEMPERATURE: 0.5,
    GenParams.TOP_K: 50,
    GenParams.TOP_P: 1
}

    model_id_1 = "meta-llama/llama-3-3-70b-instruct"

    llm = WatsonxLLM(
        model_id=model_id_1,
        url=credentials["url"],
        apikey=credentials["apikey"],
        project_id=project_id,
        params=parameters
        )
        
    chain = prompt | llm 
    
    return llm.stream(user_query)

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content=" مرحبا انا هيروكيميت المساعد الذكي كيف أستطيع مساعدتك "),
    ]

    
# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = get_response(user_query, st.session_state.chat_history)
        st.write(response)

    st.session_state.chat_history.append(AIMessage(content=response))

    # Optionally limit chat history to the last few exchanges to prevent overflow
    if len(st.session_state.chat_history) > 10:  # Limit history to the last 5 interactions
        st.session_state.chat_history = st.session_state.chat_history[-10:]
from langchain_ollama import ChatOllama
import streamlit as st

st.header("LLM MODEL🤖")
st.write("ask anything!!")

# setting Form
with st.form("LLM-FORM"):
    text = st.text_area("Enter Prompt")
    submit = st.form_submit_button("Submit")

def response_generation(input_text):
    # Inistialise our model here
    model = ChatOllama(model='llama3.2:latest')
    response = model.invoke(input_text)
    return response.content

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [ ]

if submit and text.strip():  # Ensure input is not empty
    with st.spinner('Processing...'):
        response = response_generation(text)
        st.session_state["chat_history"].append({"User":text,"Ollama":response})
        st.write(response)

st.write("**CHAT HISTORY**")
for i in st.session_state['chat_history']:
    st.write(f"**User**:{i['User']}")
    st.write(f"**Ollama**:{i['Ollama']}")

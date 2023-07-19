import streamlit as st

from text2sql.components.sidebar import sidebar
from langchain import SQLDatabase
from langchain.chat_models import ChatOpenAI
from langchain.chains import SQLDatabaseSequentialChain
from pathlib import Path
  
def generate_response(sql_chain, input_text):    
  try:
      output = sql_chain(input_text)
  except Exception as e:
       st.error(f"{e.__class__.__name__}: {e}")  
       return

  input_str = output['intermediate_steps'][0]['input']

  # Split by '\nSQLQuery:' and then by '\nSQLResult:'
  query = input_str.split('\nSQLQuery:')[1].split('\nSQLResult:')[0].strip()
  answer = output['result']
  
  st.code(query)
  st.info(answer)
  
  st.session_state.query = query
  st.session_state.answer = answer
    

def main():    
    st.set_page_config(page_title="Text2SQL", page_icon="🔍", layout="wide")
    st.header("📚🔍 Text2SQL")

    sidebar()
    
    with st.expander("GETTING STARTED"):
       st.write((Path(__file__).parent/"README.md").read_text())
   
        
    openai_api_key = st.session_state.get("OPENAI_API_KEY")
    if not openai_api_key:
        st.warning(
            "Enter your OpenAI API key in the sidebar. You can obtain your API key by visiting this link:"
            " https://platform.openai.com/account/api-keys."
        )
    
    llm = ChatOpenAI(temperature=0.0, openai_api_key=openai_api_key, verbose=True)
    
    db = SQLDatabase.from_uri(
        ("sqlite:///data/movie.sqlite")    
    )

    sql_chain = SQLDatabaseSequentialChain.from_llm(llm, db,  verbose=True, return_intermediate_steps=True)
    
    if 'query' not in st.session_state:
        st.session_state.query = ''

    if 'answer' not in st.session_state:
        st.session_state.answer = ''
        
    
    text = st.text_area('Enter text:', 'List the top 10 popular movies.')
    submitted = st.button('Submit')

    if submitted:
        generate_response(sql_chain, text)                  
        
    else:
        if st.session_state.query:
            st.code(st.session_state.query)
        
        if st.session_state.answer:
            st.info(st.session_state.answer)
    
if __name__ == "__main__":
    main()

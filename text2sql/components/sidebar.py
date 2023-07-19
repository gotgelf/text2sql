import streamlit as st
import os

def sidebar():
    with st.sidebar:
        st.markdown(
            "## Credentials\n"            
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can obtain your API key by visiting this link https://platform.openai.com/account/api-keys.",  
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# About Text2SQL")
        st.markdown(
            "Text2SQL is an open-source project that converts "
            "natural language into SQL queries using "
            "the LangChain framework. "
            "It can work with any SQL dialect supported by "
            "SQLAlchemy and is flexible for many database systems."                    
        )
        st.markdown(
            "This project is under active development. "
            "Your input is invaluable to us. Share your ideas and feedback on our [GitHub](https://github.com/gotgelf/text2sql) 🚀."            
        )       
        st.markdown("---")


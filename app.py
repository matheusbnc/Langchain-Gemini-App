from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o modelo de linguagem
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
prompt = ChatPromptTemplate.from_template("Faça um resumo sobre as informações contidas na seguinte página da wikipedia: {input}")
model = prompt | llm

# Define o título e configurações da página
st.set_page_config(page_title='Gerador de Resumos', page_icon=":gem:", layout='wide')
st.title('Resumo Básico')
st.sidebar.title('URL')
entrada = st.sidebar.text_input(label='Informe uma página da Wikipedia para obter um resumo sobre ela:')
btn = st.sidebar.button(label='Enviar')

# Interação
if btn:
    with st.spinner('Aguarde, estamos processando sua solicitação...'):
        # Chama o modelo para gerar o resumo
        res = model.invoke({'input': entrada})
        # Exibe o resumo
        st.write(res.content)


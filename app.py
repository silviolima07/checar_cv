import pandas as pd
import streamlit as st
from crewai import Crew, Process
from my_agents import criar_agente_recrutador
from my_tasks import criar_task_analise
from my_tools import save_uploaded_pdf
from config_llm import llama
import pdfplumber
import os
from config_modelo import selecionar_modelo
from PIL import Image


# Função para ler o PDF e extrair o texto
def extract_text_from_pdf(uploaded_file):
    text_content = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text_content += page.extract_text() + "\n"
    return text_content

# Função para salvar o conteúdo extraído em um arquivo txt
def save_to_txt(text_content, output_filename="output.txt"):
    with open(output_filename, "w", encoding="utf-8") as text_file:
        text_file.write(text_content)

# Função para ler o conteúdo de um arquivo markdown
def read_markdown_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    else:
        raise FileNotFoundError(f"Arquivo {file_path} não encontrado.")

html_page_title = """
     <div style="background-color:black;padding=60px">
         <p style='text-align:center;font-size:50px;font-weight:bold'>Revisão de Currículo</p>
     </div>
               """               
st.markdown(html_page_title, unsafe_allow_html=True)

# Configuração Crew

# # Configuração da crew com o agente recrutador
# recrutador = criar_recrutador()

# crew = Crew(
    # agents=[recrutador],
    # tasks=[analise],
    # process=Process.sequential,  # Processamento sequencial das tarefas
    # verbose=True
# )

robo = Image.open("img/robo3.jpg")
st.sidebar.image(robo,caption="",use_column_width=False)

st.sidebar.markdown("# Menu")
option = st.sidebar.selectbox("Menu", ["CV", 'About'], label_visibility='hidden')

if option == 'CV':
    st.markdown("## Upload CV")
    uploaded_file = st.file_uploader("Envie o seu currículo em PDF", type=["pdf"])
    if uploaded_file is not None:
        # Salvar PDF e extrair texto
        save_uploaded_pdf(uploaded_file, 'cv.pdf')  # save pdf
        
        # Extrair texto do PDF
        text_content = extract_text_from_pdf(uploaded_file)
        save_to_txt(text_content, 'cv.txt')  # save txt
        #st.markdown("##### Criados cv.pdf e cv.txt")
        #st.markdown("##### Arquivo cv.txt será lido pelo modelo para avaliação")
        
        st.markdown("## Informe o cargo para o qual vai se candidatar:")
        
        cargo = st.text_input("Cargo da vaga:")
        size = len(cargo)
        #st.markdown("### " + cargo)
        
        # if len(cargo)!=0:
            # st.markdown("### Vaga: " + cargo)
            
        
            # st.markdown("## Selecione um modelo:")
            # opcao = selecionar_modelo()
            # if opcao == 'llama':
                # modelo = llama
            # elif opcao == 'mixtral':
                # modelo = mixtral
            # else:
                # modelo = gemma            
        
        modelo = llama                
        
        if cargo:
        
            # Configuração da crew com o agente recrutador
            recrutador = criar_agente_recrutador(modelo)
            # Cria a task usando o agente criado
            analise = criar_task_analise(recrutador)
        
            st.markdown("## Analisar CV, Revisar e Recomendar")    
            
            
            crew = Crew(
                agents=[recrutador],
                tasks=[analise],
                process=Process.sequential,  # Processamento sequencial das tarefas
                verbose=True
             )


            st.markdown("## Modelo: llama")
        

            if st.button("INICIAR"):
                inputs = {'cargo': cargo,
                      'cv': 'cv.txt',
                      'sugestao': 'sugestao.md'}
                with st.spinner('Wait for it...'):
                    # Executa o CrewAI
                    try:
                        result = crew.kickoff(inputs=inputs)
                
                    # Exibir resultado - ajuste para o tipo de dado CrewOutput
                    #if hasattr(result, 'raw'):
                    #    st.write("Resposta do agente:", result.raw)
                    #else:
                    #    st.write("Resposta do agente:", result)  # Exibir resultado diretamente
                
                        # Caminho para o arquivo Markdown
                        markdown_file_path = "sugestao.md"
                
                        # Verificar se o arquivo Markdown existe e exibir
                        try:
                            markdown_content = read_markdown_file(markdown_file_path)
                            st.markdown(markdown_content, unsafe_allow_html=True)
                    
                            # Adicionar botão de download para o arquivo Markdown
                            with open(markdown_file_path, "r", encoding="utf-8") as file:
                                st.download_button(
                                    label="Baixar Sugestão em Markdown",
                                    data=file,
                                    file_name="sugestao.md",
                                    mime="text/markdown"
                                )
                        
                            st.markdown("## Boa sorte.")  
                                               
                        
                        except FileNotFoundError:
                            st.error(f"O arquivo Markdown {markdown_file_path} não foi encontrado.")
                    except Exception as e:
                        st.error(f"Erro ao executar o CrewAI: {str(e)}")
    else:
            st.markdown("##### Formato PDF")        

if option == 'About':
    st.markdown("# About:")
    st.markdown("### Este aplicativo faz a leitura de um curriculo em pdf.")
    st.markdown("### Um agente recrutador faz a leitura e recomenda melhorias.")
    st.markdown("### Modelos acessados via Groq.")      

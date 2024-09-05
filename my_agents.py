from crewai import Agent
from crewai_tools import FileReadTool
#from app import modelo
import streamlit as st




# Ferramenta para leitura de arquivo cv.txt
reader_tool = FileReadTool()

# Configuração do agente

def criar_agente_recrutador(modelo):
    
    recrutador = Agent(
        role="recrutador",
        goal="Ler o arquivo {cv} com a ferramenta de leitura. Recomendar melhorias no texto do curriculo do usuario para o cargo de {cargo}",
        backstory=
            "Você é um experiente recrutador atualizado com os critérios de busca feitos pelos recrutadores. "
            "Você trabalha numa grande empresa de recrutamento e sabe os critérios usados na seleção de candidatos a vagas."
            "Você sugere palavras chaves que devem ser inseridas no texto do curriculo para o cargo desejado."
            "Você orienta melhorias que o usuário deve fazer no curriculo para que seja chamado pelos recrutadores para participar de processos de contratação."
        ,
        llm=modelo,
        verbose=True,
        memory=True,
        tools=[reader_tool]
    )
    st.write("Agente recrutador sua mente sera o "+ str(modelo.model_name))
    return recrutador    
 

#recrutador = criar_agente_recrutador(modelo) 
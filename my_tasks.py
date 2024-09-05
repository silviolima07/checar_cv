from crewai import Task
import streamlit as st
#from my_agents import criar_agente_recrutador

# Configuração da crew com o agente recrutador
#recrutador = criar_agente_recrutador(modelo)
# Configuração da task

# Definindo as tarefas

# my_tasks.py

def criar_task_analise(recrutador):
    analise = Task(
        description=(
             "Usar a ferramenta de leitura para ler o arquivo {cv}."
             "Numa escala de 0 a 10, onde 0 é a menor importância e 10 a maior importância."            
             "Analisar o texto do curriculo do usuário  e recomende melhorias escala de importância de valor 9."
             "Recomendar as melhores palavras chaves e melhorias no texto do curriculo lido."
             "Faça comentários em Português do Brasil"
             "Revisar a acentuação do texto, garanta que esta correta."
             "Salvar as recomendações num arquivo chamado {sugestao}") ,
        expected_output=
             "Arquivo markdown(.md), um texto claro, em Português do Brasil."
         ,
         agent=recrutador,
         output_file='sugestao.md'
     )
    st.write("Tasks analise criada.")
    st.write("Objetivo: " + str(recrutador.goal))
    return analise


# analise = Task(
        # description=(
            # "Usar a ferramenta de leitura para ler o arquivo {cv}."
            # "Numa escala de 0 a 10, onde 0 é a menor importância e 10 a maior importância."            
            # "Analisar o texto do curriculo do usuário  e recomende melhorias escala de importância de valor 9."
            # "Recomendar as melhores palavras chaves e melhorias no texto do curriculo lido."
            # "Faça comentários em Português do Brasil"
            # "Revisar a acentuação do texto, garanta que esta correta."
            # "Salvar as recomendações num arquivo chamado {sugestao}") ,
        # expected_output=
            # "Arquivo markdown(.md), um texto claro, em Português do Brasil."
        # ,
        # agent=recrutador,
        # output_file='sugestao.md'
    # )
    

   

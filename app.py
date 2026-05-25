import streamlit as st
import telebot
import random
import time
import pandas as pd

# Configuração da página do Streamlit
st.set_page_config(page_title="Vision Trade PRO - Painel de Marketing", page_icon="🤖")
st.title("🤖 Vision Trade PRO V3 - Central de Transmissão")

# Inicialização do Bot Oficial (Substitua pelo seu Token real gerado no BotFather)
# Recomenda-se usar st.secrets para produção
TOKEN = st.text_input("Insira o Token do seu Bot Oficial:", type="password")

# Simulação de Banco de Dados de Usuários (ID dos clientes que iniciaram o bot)
# Na prática, você conectaria isso a um banco de dados (SQLite, PostgreSQL, etc.)
st.subheader("1. Base de Clientes (Usuários que já usam o Bot)")
u_data = {
    "user_id": [123456789, 987654321, 555444333],
    "nome": ["Carlos Trader", "Ana Investimentos", "Marcos FX"]
}
df_usuarios = pd.DataFrame(u_data)
st.dataframe(df_usuarios)

# Área para configuração das Mensagens Rotativas
st.subheader("2. Configuração de Mensagens Rotativas")
msg1 = st.text_area("Mensagem A:", "Resultados do Vision Trade PRO V3 de hoje! 🚀 Entre no canal para ver.")
msg2 = st.text_area("Mensagem B:", "Gráfico rodando e metas batidas. 📊 Venha conhecer nossa inteligência artificial.")
msg3 = st.text_area("Mensagem C:", "Vagas limitadas para a sala VIP do Vision Trade. 🤖 Clique e confira.")

mensagens = [msg1, msg2, msg3]

# Configuração de Intervalos
st.subheader("3. Parâmetros de Envio Seguro")
intervalo_min = st.number_input("Intervalo Mínimo (segundos):", min_value=1, value=5)
intervalo_max = st.number_input("Intervalo Máximo (segundos):", min_value=2, value=15)

# Botão de Disparo
if st.button("Iniciar Transmissão para Clientes"):
    if not TOKEN:
        st.error("Por favor, insira o Token do Bot.")
    else:
        try:
            bot = telebot.TeleBot(TOKEN)
            status_list = []
            
            progress_bar = st.progress(0)
            total_usuarios = len(df_usuarios)
            
            for index, row in df_usuarios.iterrows():
                # Escolha aleatória da mensagem cadastrada
                msg_escolhida = random.choice(mensagens)
                user_id = row['user_id']
                
                try:
                    # Envia para o usuário que já iniciou o bot anteriormente
                    bot.send_message(user_id, msg_escolhida)
                    st.success(f"Enviado para {row['nome']} ({user_id})")
                except Exception as e:
                    st.error(f"Erro ao enviar para {user_id}: {e}")
                
                # Intervalo dinâmico para simular comportamento humano
                tempo_espera = random.randint(intervalo_min, intervalo_max)
                time.sleep(tempo_espera)
                
                # Atualiza barra de progresso
                progress_bar.progress((index + 1) / total_usuarios)
                
            st.balloons()
            st.success("Transmissão concluída com sucesso!")
            
        except Exception as api_error:
            st.error(f"Erro ao inicializar o Bot: {api_error}")

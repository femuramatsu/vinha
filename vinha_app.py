import streamlit as st

# Configuração da página
st.set_page_config(page_title="Vinha", layout="wide")

# Menu lateral
st.sidebar.title("🍇 Vinha")
menu = st.sidebar.radio("Navegação", ["Início", "Teste de Dons", "Cosmovisão (em breve)", "Painel da Igreja (em breve)"])

# Login simulado
st.sidebar.markdown("---")
user_email = st.sidebar.text_input("Digite seu e-mail para começar", "")
if user_email:
    st.sidebar.success(f"Bem-vindo(a), {user_email}!")

# Página inicial
if menu == "Início":
    st.title("🌿 Bem-vindo à Vinha")
    st.markdown("""
        **Vinha** é uma plataforma de ferramentas cristãs para discipulado, formação espiritual e autoconhecimento no Corpo de Cristo.

        Aqui você poderá:
        - Fazer testes como o de **Dons Espirituais**
        - Explorar sua **Cosmovisão Cristã** (em breve)
        - Receber relatórios personalizados
        - Se desejar, **vincular-se à sua igreja local** e contribuir com seu crescimento

        Tudo de forma **segura**, **anônima** e voltada ao Reino de Deus.
    """)

# Teste de Dons Espirituais (versão inicial)
elif menu == "Teste de Dons":
    st.title("🕊️ Teste de Dons Espirituais")
    st.write("Responda com sinceridade. Não há respostas certas ou erradas.")

    questions = [
        "Gosto de ensinar a Bíblia de forma clara para outros.",
        "Sinto-me motivado a ajudar os necessitados, mesmo em tarefas pequenas.",
        "Tenho facilidade em liderar grupos e inspirar pessoas.",
        "Sinto quando algo espiritual está errado, mesmo sem explicação lógica.",
        "Sou generoso com meus recursos financeiros, mesmo sem retorno esperado.",
    ]

    scores = []
    for q in questions:
        score = st.slider(q, 0, 4, 2, label_visibility="visible")
        scores.append(score)

    if st.button("Ver Resultado"):
        total = sum(scores)
        st.subheader("✨ Seu Resultado:")
        if total >= 16:
            st.success("Você pode ter dons ligados à liderança, ensino e generosidade.")
        elif total >= 10:
            st.info("Você pode ter dons voltados ao serviço, ajuda e sabedoria.")
        else:
            st.warning("Seus dons podem estar mais voltados à sensibilidade espiritual e intercessão.")

# Páginas em construção
else:
    st.title("🔧 Em breve")
    st.markdown("Esta funcionalidade está sendo construída com carinho. Em breve, estará disponível para você.")

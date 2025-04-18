
import streamlit as st

st.set_page_config(page_title="Vinha - Teste de Ministérios", layout="wide")

st.sidebar.title("🍇 Vinha")
menu = st.sidebar.radio("Navegação", ["Início", "Teste dos 5 Ministérios", "Em breve"])

st.sidebar.markdown("---")
user_email = st.sidebar.text_input("Digite seu e-mail para começar", "")
if user_email:
    st.sidebar.success(f"Bem-vindo(a), {user_email}!")

if menu == "Início":
    st.title("🌿 Bem-vindo à Vinha")
    st.markdown("""
        Este é o Teste dos 5 Ministérios de Efésios 4:11.  
        Descubra em qual ministério você mais se identifica:

        **Apóstolo • Profeta • Evangelista • Pastor • Mestre**

        Responda com sinceridade. Não existem respostas certas ou erradas.
    """)

elif menu == "Teste dos 5 Ministérios":
    st.title("🕊️ Teste dos 5 Ministérios de Efésios 4:11")

    perguntas = {
        "Apóstolo": [
            "Gosto de iniciar projetos e reunir pessoas com um propósito.",
            "Tenho facilidade em enxergar o todo e traçar estratégias.",
            "Me sinto chamado a edificar ou estruturar algo maior que eu.",
            "Tenho iniciativa para liderar novas frentes ou ministérios.",
            "Sinto que minha missão é abrir caminhos para outros seguirem."
        ],
        "Profeta": [
            "Tenho forte sensibilidade espiritual sobre pessoas e ambientes.",
            "Sinto necessidade de falar a verdade mesmo quando é desconfortável.",
            "Percebo quando algo está errado, mesmo que ninguém diga nada.",
            "Tenho zelo pela santidade e pureza no meio cristão.",
            "Frequentemente sou movido por convicções profundas, mesmo contra a maioria."
        ],
        "Evangelista": [
            "Falar de Jesus para outras pessoas me empolga.",
            "Consigo explicar o evangelho com clareza e simplicidade.",
            "Tenho facilidade de me conectar com pessoas que não são da igreja.",
            "Me sinto motivado quando alguém entrega a vida a Cristo.",
            "Acredito que alcançar pessoas é minha principal missão."
        ],
        "Pastor": [
            "As pessoas costumam me procurar para pedir conselhos.",
            "Sinto prazer em cuidar das necessidades dos outros.",
            "Tenho compaixão por quem está sofrendo ou perdido.",
            "Gosto de caminhar com as pessoas a longo prazo.",
            "Preocupo-me com o bem-estar e crescimento dos irmãos da fé."
        ],
        "Mestre": [
            "Gosto de ensinar a Palavra com profundidade e clareza.",
            "Tenho facilidade de organizar ideias e preparar estudos bíblicos.",
            "Sinto alegria em ver as pessoas aprendendo e crescendo no conhecimento.",
            "Tenho sede por estudar a Bíblia e entender suas verdades.",
            "Busco transmitir a verdade com exatidão, sem distorções."
        ]
    }

    st.write("Responda cada afirmação com sinceridade:")

    pontuacoes = {"Apóstolo": 0, "Profeta": 0, "Evangelista": 0, "Pastor": 0, "Mestre": 0}

    for ministerio, qs in perguntas.items():
        st.subheader(ministerio)
        for q in qs:
            resposta = st.slider(q, 0, 4, 2, key=q)
            pontuacoes[ministerio] += resposta

    if st.button("Ver Resultado"):
        ordenado = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)
        st.subheader("✨ Seu Perfil Ministerial")
        for i, (minist, pontos) in enumerate(ordenado[:2]):
            st.markdown(f"**{minist}** – {pontos} pontos")
            if minist == "Apóstolo":
                st.info("Chamado para fundar, liderar, abrir caminhos e estruturar o Corpo de Cristo.")
            elif minist == "Profeta":
                st.warning("Sensível à voz de Deus, comprometido com a verdade e com o zelo espiritual da igreja.")
            elif minist == "Evangelista":
                st.success("Apaixonado por alcançar vidas com o evangelho, claro e direto na mensagem de salvação.")
            elif minist == "Pastor":
                st.info("Cuidador do rebanho, com compaixão, escuta ativa e amor pelas pessoas.")
            elif minist == "Mestre":
                st.success("Responsável por ensinar com profundidade e exatidão, formando discípulos maduros.")

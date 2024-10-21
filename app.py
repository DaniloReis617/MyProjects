import streamlit as st
from utils.file_utils import initialize_data_files

# Inicializar arquivos de dados
initialize_data_files()

# Configuração da página
st.set_page_config(page_title="My Projects App", page_icon="", layout="wide")

# Verificar se o usuário está logado
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Inicializar current_page no session_state
if "current_page" not in st.session_state:
    # Se o usuário está logado, redireciona para o Dashboard, caso contrário para o Login
    st.session_state.current_page = "dashboard" if st.session_state.logged_in else "login"

# Função para carregar a página dinamicamente
def load_page(page_name):
    module = __import__(f'pages.{page_name}', fromlist=['app'])
    return module.app

# Sidebar com título e exibição do usuário logado
st.sidebar.title("My Projects")

# Exibir o login do usuário, caso ele esteja logado
if st.session_state.logged_in and "user_email" in st.session_state:
    st.sidebar.markdown(f"**Usuário:** {st.session_state['user_email']}")
else:
    st.sidebar.markdown("**Não autenticado**")

# Definir as seções e páginas com ícones
if st.session_state.logged_in:
    sections = {
        "My Projects": {
            "Dashboard": "dashboard",
            "Projetos": "projetos_crud",  # Nova página para categorias
            "Perfil": "profile"
        }
    }
else:
    sections = {
        "Autenticação": {
            "Login": "login",
            "Cadastro": "register"
        }
    }

# Sidebar Navegação
with st.sidebar:
    st.logo("./assets/dks_branco.png")
    st.markdown("### Navegação")
    
    # Exibe as opções de navegação por seção
    for section, pages in sections.items():
        st.markdown(f"#### {section}")
        page_selected = st.radio(
            "", list(pages.keys()), 
            index=list(pages.values()).index(st.session_state.current_page) if st.session_state.current_page in pages.values() else 0,
            key=f"{section}_radio", label_visibility="collapsed"
        )
        # Atualiza a página atual ao selecionar uma nova
        if pages[page_selected] != st.session_state.current_page:
            st.session_state.current_page = pages[page_selected]
            st.rerun()  # Recarregar imediatamente após a seleção

# Carregar e exibir a página selecionada
if st.session_state.current_page:
    page_app = load_page(st.session_state.current_page)
    
    # Passar as informações do usuário para a página carregada
    if hasattr(page_app, 'set_user_info'):
        page_app.set_user_info(st.session_state.get('user_id'), st.session_state.get('user_email'))
    
    page_app()

# Mensagem padrão caso nenhuma página esteja selecionada
else:
    st.write("Bem-vindo ao My Projects App! Selecione uma página no menu.")

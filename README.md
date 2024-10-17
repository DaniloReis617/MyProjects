projeto_gestao/
│
├── app.py                      # Arquivo principal do Streamlit
├── database.py                 # Funções de manipulação de dados (CRUD) e parquet
├── dashboard.py                # Funções e gráficos do Dashboard
├── auth.py                     # Autenticação de usuários
├── pages/                      # Arquivos das diferentes páginas
│   ├── home.py                 # Página inicial
│   └── projetos_crud.py        # Página CRUD dos projetos
│
├── assets/                     # Arquivos estáticos (CSS, imagens, etc.)
│   └── style.css               # Customizações de estilo (opcional)
│
└── data/                       # Diretório para armazenar os arquivos Parquet
    └── projetos.parquet        # Arquivo Parquet com os dados do sistema

Explicação dos Arquivos
app.py: Arquivo principal que controla a navegação e configura o layout geral da aplicação.
database.py: Todas as operações de manipulação de dados (CRUD), e as funções para carregar e salvar dados em formato Parquet.
dashboard.py: Funções para a visualização dos gráficos e indicadores (KPIs) no dashboard.
auth.py: Funções de autenticação (login/logout).
pages/: Diretório que contém as diferentes páginas do app, como a página inicial e a página CRUD dos projetos.
assets/: Para armazenar arquivos estáticos, como arquivos CSS para customização do estilo.
data/: Onde o arquivo Parquet será armazenado.
Bibliotecas Necessárias
Aqui está a lista das bibliotecas que você precisará instalar:

Streamlit: Para a criação da interface web.
Pandas: Para manipulação dos dados em formato Parquet.
PyArrow ou Fastparquet: Para leitura e escrita de arquivos Parquet.
Matplotlib ou Plotly: Para gerar os gráficos do dashboard.
Instalação das Bibliotecas
Crie um arquivo requirements.txt para facilitar a instalação de todas as bibliotecas de uma vez:

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run app.py
   ```

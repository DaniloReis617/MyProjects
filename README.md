## Estrutura do Projeto

project_management_app/
│
├── app.py
├── pages/
│   ├── login.py
│   ├── register.py
│   ├── dashboard.py
│   ├── kanban.py
│   ├── table.py
│   ├── create.py
│   ├── edit.py
│   └── delete.py
├── utils/
│    ├── auth.py
│    └── db.py
│
└── Data/

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run app.py
   ```

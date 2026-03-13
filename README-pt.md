# SMARTWALLET
# US English version available here: [README.md](README.md)

Smartwallet é um sistema de controle financeiro pessoal desenvolvido em **Python** que permite aos usuários registrar, analisar e acompanhar suas finanças.
O projeto foi criado com foco em **organização financeira, análise de dados e boas práticas de desenvolvimento backend**
---

# FUNCIONALIDADES
### Usuários
- Cadastro de usuários
- Login com autenticação segura
- Senhas armazenadas com **hash SHA-256**
---

### Gestão de Gastos
- Adicionar gastos
- Editar gastos
- Remover gastos
- Listar gastos
- Classificação por **categorias**
---

### Gestão de Receitas
- Registrar receitas
- Listar receitas
---

### Dashboard Financeiro
- Resumo financeiro do mês
- Distribuição de gastos por categorias
- Gráfico de evolução financeira
- Visualização de saldo
- Integração com metas financeiras
---

### Metas Financeiras
- Criar metas financeiras
- Visualizar progresso das metas
- Atualizar progresso
---

### Relatórios
- Detalhamento mensal de gastos
- Gastos por categoria
- Exportação de relatórios em **CSV**
- Exportação de relatórios em **PDF**
- Geração automática de **gráficos financeiros**

---

# TECNOLOGIAS UTILIZADAS
- Python
- SQLite
- Matplotlib
- ReportLab
- Hashlib 
- CSV 

---

# ESTRUTURA DO PROJETO

SmartWallet Project/
- config/
    - config.py
- database
    - __init__.py
    - categorias_db.py
    - connection.py
    - dashboard_db.py
    - gastos_db.py
    - metas_db.py
    - receitas_db.py
    - relatorios_db.py
    - schema.py
    - usuarios_db.py
- menus/
    - menu_principal.py
    - menu_gastos.py
    - menu_receitas.py
    - menu_dashboard.py
    - menu_relatorios.py
    - menu_metas.py
- utils/
    - __init__.py
    - exportar_utils.py
    - auth_utils.py
    - date_utils.py
    - grafico_utils.py
    - input_utils.py
    - logger_utils.py
    - pdf_utils.py
    - setup_utils.py
- services/
    - services.py
- relatorios/
    - csv/
    - pdf/
    - graficos/
- main.py
- requirements.txt
- README.md

---

# COMO EXECUTAR O PROJETO

1 - Clone o repositório - git clone https://github.com/FernandoFernandes2005/smartwallet.git

2 - Entre na pasta do projeto - cd smartwallet

3 - Instale as dependências - pip install -r requirements.txt

4 - Execute o sistema - python main.py

---

# BANCO DE DADOS

O projeto utiliza **SQLite** como banco de dados local.
As tabelas são criadas automaticamente na primeira execução do sistma.
As principais tabelas são:
- 'usuarios' -> Armazena informações dos usuários
- 'gastos' -> Despesas registradas pelos usuários
- 'categorias' -> Categorias de despesas
- 'Receitas' -> Receitas registradas pelos usuários
- 'Metas' -> Metas financeiras registradas pelo usuário

---

# SEGURANÇA

- Senhas são criptografadas usando **SHA-256**
- Dados são armazenados localmente usando **SQLite**

---

# ÚLTIMAS ATUALIZAÇÕES

### Versão Atual
- Dashboard financeiro com resumo mensal
- Gráfico de evolução financeira
- Distribuição de gastos por categoria
- Sistema de metas financeiras
- Exportação de relatórios em **CSV**
- Exportação de relatórios em **PDF**
- Geração automática de **gráficos financeiros**
- Estrutura modular do projeto
- Sistema de logs
- Arquivo de configuração centralizado
- Refatoração da arquitetura do projeto
- Organização em módulos ('menus', 'utils', 'database', 'services')
- Implementação de gráficos usando **Matplotlib**
- Implementação de relatórios PDF usando **ReportLab**

### Novidades desta versão:
### Arquitetura do Projeto (Refatoração)
- Modularização das responsabilidades da camada de banco de dados
- Separação das responsabilidades em múltiplos módulos:
    - usuarios_db
    - gastos_db
    - receitas_db
    - categorias_db
    - metas_db
    - relatorios_db
    - dashboard_db
- Criação de arquivos '__init__.py' para simplificação de imports
- Migração da exportação CSV para 'utils'
- Simplificação da camada 'services'
- Remoção da camada 'models' que não era utilizada
- Melhor organização da arquitetura do projeto


---

# MELHORIAS FUTURAS

- API REST com **FastAPI**
- Autenticação com **JWT**
- Interfacce Web
- Testes automatizados com **Pytest**
- Dashboard interativo

---

# AUTOR

Projeto desenvolvido por **Fernando Fernandes Silva**.



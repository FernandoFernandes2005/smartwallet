# SMARTWALLET

Smartwallet é um sistema de controle financeiro desenvolvido em Python que permite o usuário registrar, organizar e analisar seus gastos e receitas pessoais.
O projeto possui autenticação de usuários, registros financeiros e dashboard de análise de despesas, utilizando SQLite como banco de dados.

---

# FUNCIONALIDADES
- Cadastro de usuários
- Login com senha criptografada (SHA-256)
- Registro e Listagem de gastos
- Edição e remoção de gastos
- Registro e Listagem de receitas
- Sistema de categorias de despesas
- Relatório mensal de despesas
- Resumo automático de gastos por mês
- Dashboard financeiro com "gráfico de distribuição"
- Exportação de relatórios em CSV

---

# TECNOLOGIAS UTILIZADAS
- Python
- SQLite
- Hashlib (criptografia de senha)
- CSV (exportação de relatórios)

---

# ESTRUTURA DO PROJETO

SmartWallet Project
- main.py
- database/
    - database.py
- services/
    - services.py
- models/
    - models.py
- smartwallet.db
- requirements.txt
- .gitignore
- README.MD

---

# COMO EXECUTAR O PROJETO

1 - Clone o repositório
(coloque o repositório aqui depois)
2 - Entre na pasta do projeto - cd smartwallet
3 - Execute o programa - python main.py

---

# BANCO DE DADOS

O projeto utiliza **SQLite**, criando automaticamente o arquivo "smartwallet.db".
As principais tabelas são:
- 'usuarios' -> Armazena informações dos usuários
- 'gastos' -> Despesas registradas pelos usuários
- 'categorias' -> Categorias de despesas
- 'Receitas' -> Receitas registradas pelos usuários

Os gastos usam **chave estrangeira para categorias**, garantindo melhor organização e integridade de dados.

---

# SEGURANÇA

As senhas dos usuários são armazenadas utilizando **hash SHA256**, realizando sua criptografia e garantindo maior segurança no armazenamento.

---

# ÚLTIMA ATUALIZAÇÃO (v1.1)

Novidades desta versão:
- Implementação de categorias de despesas com banco relacional;
- Relatório de gastos por categoria;
- Dashboard financeiro com distribuição de gastos
- Exportação de relatórios em CSV
- Melhorias na estrutura do banco de dados

---

# MELHORIAS FUTURAS

- Transformar o sistema em uma **API REST com FASTAPI**
- Implementar autenticação com **JWT**
- Criar interface web
- Adicionar testes automatizados

---

# AUTOR

Projeto desenvolvido por **Fernando Fernandes**.



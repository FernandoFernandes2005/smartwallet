# SMARTWALLET

# BR Portuguese version available here: [README-pt.md](README-pt.md)

SmartWallet is a personal financial management system developed in **Python** that allows users to register, analyze, and track their finances.
The project was created with a focus on **financial organization, data analysis, and backend development best practices.**

---

# FEATURES
### Users
- User registration
- Secure login authentication
- Passwords stored using **SHA-256 hashing**
---

### Expense Management
- Add expenses
- Edit expenses
- Remove expenses
- List expenses
- Classification by **categories**
---

### Income Management
- Register income
- List income
---

### Financial Dashboard
- Monthly financial summary
- Expense distribution by category
- Financial evolution chart
- Balance visualization
- Integration with financial goals
---

### Financial Goals
- Create financial goals
- View goal progress
- Update goal progress
---

### Reports
- Monthly expense breakdown
- Expenses by category
- Export reports in CSV
- Export reports in PDF
- Automatic generation of financial charts
---

# TECHNOLOGIES USED
- Python
- SQLite
- Matplotlib
- ReportLab
- Hashlib
- CSV

---

# PROJECT STRUCTURE
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
    - serices.py
- relatorios/
    - csv/
    - pdf/
    - graficos/
- main.py
- requirements.txt
- README.md

---

# HOW TO RUN THE PROJECT
1 - Clone the repository -  git clone https://github.com/FernandoFernandes2005/smartwallet.git

2 - Enter the project folder - cd smartwallet

3 - Install the dependencies - pip install -r requirements.txt

4 - Run the system - python main.py

---

# DATABASE
The project uses SQLite as a local database.
The tables are automatically created on the first execution of the system.

The main tables are:
- 'usuarios' -> Stores user information
- 'gastos' -> Expenses recorded by users
- 'categorias' -> Expense categories
- 'receitas' -> Income recorded by users
- 'metas' -> Financial goals defined by the user

---

# SECURITY
- Passwords are encrypted using **SHA-256**
- Data is stored locally using **SQLite**

---

# LATEST UPDATES
- Current Version
- Financial dashboard with monthly summary
- Financial evolution chart
- Expense distribution by category
- Financial goals system
- Export reports in **CSV**
- Export reports in **PDF**
- Automatic generation of financial charts
- Modular project structure
- Logging system
- Centralized configuration file
- Project architecture refactoring
- Modular organization (menus, utils, database, services)
- Implementation of charts using **Matplotlib**
- Implementation of PDF reports using **ReportLab**

### NEW IN THIS VERSION
### Project Architecture (Refactor)

- Complete modularization of the database layer
- Separation of responsibilities into multiple modules:
  - usuarios_db
  - gastos_db
  - receitas_db
  - categorias_db
  - metas_db
  - relatorios_db
  - dashboard_db
- Creation of `__init__.py` files to simplify imports
- Migration of CSV export functionality to the `utils` module
- Simplification of the `services` layer
- Removal of the unused `models` layer
- Improved overall organization of the project architecture

---

# FUTURE IMPROVEMENTS

- REST API with **FastAPI**
- Authentication using **JWT**
- Web Interface
- Automated tests using **Pytest**
- Interactive dashboard

---

# AUTHOR

Project developed by **Fernando Fernandes Silva.**

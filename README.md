# 🧰 Parquet Tools — Convert \& Visualize
🇵🇹 Ferramentas para converter e visualizar ficheiros \*\*Parquet\*\*  
🇺🇸 Tools to convert and visualize \*\*Parquet files\*\*

---

## 🚀 Features / Funcionalidades
| Ferramenta (PT-PT)                                                | Tool (EN)                                                | Ficheiro              |
|-------------------------------------------------------------------|----------------------------------------------------------|------------------------|
| Converter `.parquet` → `.xlsx` (Excel)                            | Convert `.parquet` → `.xlsx`                             | `parquet_to_excel.py` |
| Converter `.parquet` → `.csv`                                     | Convert `.parquet` → `.csv`                              | `parquet_to_csv.py`   |
| Visualizar `.parquet` / `.csv`, executar SQL e exportar resultados | View `.parquet` / `.csv`, execute SQL and export results | `parquet_sql_viewer.py` |


---

## 📁 Estrutura do Repositório / Repository Structure

```
/

├── src/

│   └── parquet\_to\_excel.py # Convert .parquet → Excel

|   └── parquet\_to\_csv.py # Convert .parquet → CSV

│   └── parquet\_sql\_viewer.py # Streamlit app: SQL + visualization

├── README.md

└── requirements.txt
```

---

## 📦 Instalação / Installation

```
pip install -r requirements.txt
```

## 🧑‍💻 Como usar / How to Use from Command Line

### 1️ - Converter `.parquet` → Excel (`.xlsx`)

**PT-PT**
```sh
python src/parquet_to_excel.py
```
- O script pede o caminho para o ficheiro `.parquet`
- Gera automaticamente um `.xlsx` com o mesmo nome

**EN**
```sh
python src/parquet_to_excel.py
```
- Script asks for `.parquet` input path
- Generates `.xlsx` automatically

---

### 2️ - Converter `.parquet` → CSV

**PT-PT**
```sh
python src/parquet_to_csv.py
```
- Será pedido:
  - Caminho do ficheiro `.parquet`
  - Caminho + nome do `.csv` de saída

**EN**
```sh
python src/parquet_to_csv.py
```
- Prompts for:
  - Input `.parquet` file path
  - Output `.csv` filename

---

### 3️ - Visualizar, consultar com SQL e exportar resultados

**PT-PT**
```sh
streamlit run src/parquet_sql_viewer.py
```
- Abre interface web para:
  - Visualizar dados `.parquet` ou `.csv`
  - Pesquisar colunas
  - Executar SQL (`SELECT * FROM data LIMIT 10`)
  - Exportar para CSV ou Parquet

**EN**
```sh
streamlit run src/parquet_sql_viewer.py
```
- Opens web UI to:
  - View `.parquet` or `.csv`
  - Search columns
  - Run SQL (`SELECT * FROM data LIMIT 10`)
  - Export to CSV or Parquet

---

## 📄 Licença / License

**MIT License**
```
You are free to use this project for personal or commercial purposes.

```

## 📚 Como citar este repositório / How to cite this repository

Se utilizar este repositório em trabalhos académicos, publicações ou projetos, por favor cite da seguinte forma:

### 🇵🇹 Citação (PT-PT)

```
Mendes, Nuno A.G. (2025). Parquet Tools — Convert, Query & Explore.
Repositório GitHub. Disponível em: https://github.com/NunoAGM/Parquet_Tools
```

### 🇺🇸 Citation (EN)

```
Mendes, Nuno A.G. (2025). Parquet Tools — Convert, Query & Explore.
GitHub repository. Available at: [https://github.com/NunoAGM/Parquet_Tools
```

Se quiser usar em BibTeX (LaTeX):

```bibtex
@software{mendes_parquet_tools_2025,
  author       = {Nuno A. G. Mendes},
  title        = {Parquet Tools — Convert, Query \& Explore},
  year         = {2025},
  publisher    = {GitHub},
  url          = {https://github.com/NunoAGM/Parquet_Tools},
}
```

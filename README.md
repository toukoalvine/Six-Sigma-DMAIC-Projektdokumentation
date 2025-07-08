# Six-Sigma-DMAIC-Projektdokumentation
interactive web app with all the key Six Sigma tools and automated report generation
# 📊 Streamlit Data Analysis and Reporting App

This is a Streamlit-based web application for interactive data analysis and automated report generation. It allows users to visualize data using Plotly and Matplotlib, export dynamic reports as PDFs, and optionally bundle results into a downloadable ZIP archive.

---

## 🚀 Features

- Upload and process CSV data files
- Interactive visualizations with:
  - Plotly Express and Graph Objects
  - Matplotlib charts
- Filter and analyze data using Pandas and NumPy
- Generate professional PDF reports with ReportLab
- Export reports and plots as downloadable files
- Bundle multiple outputs into a ZIP archive

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Web app framework for data apps
- [Pandas](https://pandas.pydata.org/) – Data manipulation
- [NumPy](https://numpy.org/) – Numerical computing
- [Plotly](https://plotly.com/python/) – Interactive visualizations
- [Matplotlib](https://matplotlib.org/) – Static plotting
- [ReportLab](https://www.reportlab.com/) – PDF generation
- Standard Python Libraries: `datetime`, `json`, `io`, `base64`, `zipfile`

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/toukoalvine/Six-Sigma-DMAIC-Projektdokumentation.git
   cd Six-Sigma-DMAIC-Projektdokumentation
source /home/adminuser/venv/bin/activate
pip install plotly
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

streamlit run streamlit_app.py


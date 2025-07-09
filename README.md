# Six Sigma DMAIC Projekt-Dokumentationspaket

Ein umfassendes Streamlit-Dashboard für Six Sigma DMAIC-Projekte mit vollständiger Dokumentation und Berichterstellung.

## 📋 Übersicht

Diese Anwendung bietet eine vollständige Lösung für die Dokumentation und Verwaltung von Six Sigma DMAIC-Projekten. Sie führt Sie durch alle fünf Phasen des DMAIC-Prozesses und generiert professionelle Berichte.

## 🎯 Features

### Kernfunktionen
- **Vollständige DMAIC-Phasen-Unterstützung**: Define, Measure, Analyze, Improve, Control
- **Interaktive Dashboards**: Moderne, benutzerfreundliche Oberfläche
- **Automatische Berechnungen**: Sigma-Level, DPMO, Prozessfähigkeit
- **Visualisierungen**: Pareto-Diagramme, Kontrollkarten, Histogramme
- **PDF-Report-Generator**: Professionelle Projektberichte
- **Datenexport**: JSON-Export für Projektdaten

### Phase-spezifische Tools

#### Define Phase
- Projekt-Grunddaten-Erfassung
- Problem Statement Definition
- SIPOC-Diagramm-Erstellung
- CTQ Tree (Critical to Quality)
- Projektscope und Business Case

#### Measure Phase
- Metriken-Definition
- Baseline-Messung
- DPMO-Berechnung
- Sigma-Level-Bestimmung
- Prozessfähigkeits-Assessment

#### Analyze Phase
- Ursache-Wirkungs-Analyse
- Fischgräten-Diagramm
- Pareto-Analyse
- Hypothesentests
- Statistische Analysen

#### Improve Phase
- Lösungsidentifikation
- Implementierungsplanung
- Pilotprojekt-Tracking
- Kosten-Nutzen-Analyse

#### Control Phase
- Kontrollpläne
- Monitoring-Systeme
- Kontrollkarten
- Nachhaltigkeit-Sicherung

## 🚀 Installation

### Für Streamlit Cloud (Empfohlen)
1. **Repository in Streamlit Cloud deployen**
   - Gehen Sie zu [share.streamlit.io](https://share.streamlit.io)
   - Verbinden Sie Ihr GitHub-Repository
   - Stellen Sie sicher, dass `requirements.txt` im Root-Verzeichnis liegt
   - Die App wird automatisch deployed

2. **Wichtige Dateien für Streamlit Cloud**
   ```
   your-repo/
   ├── streamlit_app.py      # Haupt-App-Datei
   ├── requirements.txt      # Dependencies
   └── README.md            # Diese Datei
   ```

### Für lokale Entwicklung

#### Voraussetzungen
- Python 3.8 oder höher
- pip (Python Package Manager)

#### Schritt-für-Schritt Installation

1. **Repository klonen oder Code herunterladen**
   ```bash
   git clone https://github.com/toukoalvine/Six-Sigma-DMAIC-Projektdokumentation
   cd Six-Sigma-DMAIC-Projektdokumentation

   ```

2. **Virtuelle Umgebung erstellen (empfohlen)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Dependencies installieren**
   ```bash
   pip install plotly
   pip install -r requirements.txt
   ```

4. **Anwendung starten**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Browser öffnen**
   Die Anwendung läuft standardmäßig auf `http://localhost:8501`

## 📊 Verwendung

### Navigation
- Verwenden Sie die Sidebar zur Navigation zwischen den verschiedenen DMAIC-Phasen
- Jede Phase baut auf den vorherigen auf
- Daten werden automatisch in der Session gespeichert

### Projekt starten
1. Gehen Sie zur "Projektübersicht"
2. Klicken Sie auf "Neues Projekt starten"
3. Beginnen Sie mit der Define-Phase

### Daten eingeben
- Füllen Sie alle relevanten Felder in jeder Phase aus
- Verwenden Sie die interaktiven Widgets für Berechnungen
- Laden Sie bei Bedarf Daten über File-Upload hoch

### Berichte generieren
- Nutzen Sie den "Report Generator" für PDF-Berichte
- Exportieren Sie Projektdaten als JSON
- Drucken Sie Diagramme und Analysen

## 🔧 Konfiguration

### Anpassung der Benutzeroberfläche
Die Anwendung verwendet Custom CSS für das Styling. Anpassungen können in der `st.markdown()` Sektion vorgenommen werden.

### Datenpersistenz
- Daten werden in der Streamlit Session gespeichert
- Für permanente Speicherung nutzen Sie die Export-Funktionen
- Projekte können als JSON-Dateien gespeichert und geladen werden

## 📈 Berechnungen und Formeln

### Sigma Level Berechnung
```python
def calculate_sigma_level(dpmo):
    # Approximation basierend auf Normalverteilung
    # Berücksichtigt Standard-Sigma-Level-Tabellen
```

### DPMO (Defects Per Million Opportunities)
```
DPMO = (Anzahl Defekte / (Anzahl Einheiten × Anzahl Opportunities)) × 1,000,000
```

### Prozessfähigkeit
- **Cp**: Prozessfähigkeit (Process Capability)
- **Cpk**: Prozessfähigkeitsindex (Process Capability Index)

## 🎨 Diagramme und Visualisierungen

### Verfügbare Diagrammtypen
- **Pareto-Diagramme**: Für Prioritätensetzung
- **Kontrollkarten**: Für Prozessüberwachung
- **Histogramme**: Für Datenverteilung
- **Fischgräten-Diagramme**: Für Ursache-Wirkungs-Analyse
- **Box-Plots**: Für statistische Analyse

### Technische Grundlage
- **Plotly**: Für interaktive Diagramme
- **Matplotlib**: Für statische Visualisierungen
- **Seaborn**: Für statistische Plots

## 📄 Berichterstellung

### PDF-Berichte
- Automatische Generierung professioneller Berichte
- Einbindung aller Projektdaten
- Strukturierte Darstellung nach DMAIC-Phasen

### Export-Optionen
- **JSON**: Vollständige Projektdaten
- **PDF**: Formatierte Berichte
- **CSV**: Datenexport für weitere Analyse

## 🔒 Sicherheit und Datenschutz

- Alle Daten werden lokal in der Browser-Session gespeichert
- Keine Datenübertragung an externe Server
- Sichere Handhabung von Uploads und Downloads

## 🛠️ Entwicklung

### Projektstruktur
```
six-sigma-dmaic-app/
├── app.py                 # Hauptanwendung
├── requirements.txt       # Python-Dependencies
├── README.md             # Diese Datei
└── utils/                # Hilfsfunktionen (optional)
```

### Erweiterungen
Die Anwendung ist modular aufgebaut und kann leicht erweitert werden:
- Neue Phasen hinzufügen
- Zusätzliche Diagrammtypen integrieren
- Erweiterte statistische Analysen
- Datenbankintegration

## 🐛 Troubleshooting

### Häufige Probleme

**Problem**: `ModuleNotFoundError: No module named 'plotly'` in Streamlit Cloud
- **Lösung**: 
  1. Stellen Sie sicher, dass `requirements.txt` im Root-Verzeichnis liegt
  2. Überprüfen Sie den Inhalt von `requirements.txt`:
     ```
     streamlit
     pandas
     numpy
     plotly
     matplotlib
     seaborn
     scipy
     reportlab
     openpyxl
     pillow
     python-dateutil
     ```
  3. Reboot der App in Streamlit Cloud (Hamburger-Menü → Reboot)
  4. Bei persistenten Problemen: GitHub-Repository synchronisieren

**Problem**: `ModuleNotFoundError: No module named 'plotly'` lokal
- **Lösung**: Installieren Sie die fehlenden Dependencies:
  ```bash
  pip install plotly>=5.15.0
  # oder alle Requirements auf einmal:
  pip install -r requirements.txt
  ```

**Problem**: Anwendung startet nicht
- **Lösung**: 
  1. Überprüfen Sie die Python-Version (3.8+)
  2. Installieren Sie alle Requirements: `pip install -r requirements.txt`
  3. Aktivieren Sie die virtuelle Umgebung falls verwendet

**Problem**: Diagramme werden nicht angezeigt
- **Lösung**: Stellen Sie sicher, dass Plotly korrekt installiert ist:
  ```bash
  pip install plotly matplotlib seaborn
  ```

**Problem**: PDF-Export funktioniert nicht
- **Lösung**: Überprüfen Sie die ReportLab-Installation:
  ```bash
  pip install reportlab>=4.0.0
  ```

**Problem**: Import-Fehler bei anderen Modulen
- **Lösung**: Installieren Sie alle Requirements neu:
  ```bash
  pip uninstall -r requirements.txt -y
  pip install -r requirements.txt
  ```

### Schnelle Lösung für Streamlit Cloud/Deployment
Falls Sie die App in Streamlit Cloud deployen:
1. Stellen Sie sicher, dass `requirements.txt` im Root-Verzeichnis liegt
2. Überprüfen Sie, dass alle Paketnamen korrekt geschrieben sind
3. Verwenden Sie die neueste Python-Version (3.8+)

### Logs und Debugging
```bash
streamlit run app.py --logger.level debug
```

### Virtuelle Umgebung neu erstellen
```bash
# Alte Umgebung löschen
rm -rf venv

# Neue Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder
venv\Scripts\activate     # Windows

# Requirements installieren
pip install -r requirements.txt
```

## 📞 Support

Bei Problemen oder Fragen:
1. Überprüfen Sie die Dokumentation
2. Prüfen Sie die Requirements
3. Konsultieren Sie die Streamlit-Dokumentation
4. Erstellen Sie ein Issue im Repository

## 🚧 Roadmap

### Geplante Features
- [ ] Datenbank-Integration
- [ ] Multi-User-Support
- [ ] Erweiterte Statistiken
- [ ] Mobile Optimierung
- [ ] Template-System
- [ ] API-Integration

### Version History
- **v1.0.0**: Initiale Version mit allen DMAIC-Phasen
- **v1.1.0**: Erweiterte Visualisierungen
- **v1.2.0**: PDF-Report-Generator

## 📜 Lizenz

Diese Anwendung ist für den internen Gebrauch bestimmt. Bitte beachten Sie die Lizenzbestimmungen der verwendeten Bibliotheken.

## 🙏 Danksagung

Entwickelt mit modernen Python-Technologien:
- Streamlit für die Web-Anwendung
- Plotly für interaktive Visualisierungen
- ReportLab für PDF-Generierung
- Pandas für Datenmanipulation

---

**Hinweis**: Diese Anwendung ist ein Werkzeug zur Unterstützung von Six Sigma Projekten. Für professionelle Zertifizierungen sollten offizielle Six Sigma Ressourcen konsultiert werden.

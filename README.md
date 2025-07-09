# Six-Sigma-DMAIC-Projektdokumentation
interactive web app with all the key Six Sigma tools and automated report generation
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

### Voraussetzungen
- Python 3.8 oder höher
- pip (Python Package Manager)

### Schritt-für-Schritt Installation

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
   pip install -r requirements.txt
   ```

4. **Anwendung starten**
   ```bash
   streamlit run app.py
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

**Problem**: Anwendung startet nicht
- **Lösung**: Überprüfen Sie die Python-Version und installierte Packages

**Problem**: Diagramme werden nicht angezeigt
- **Lösung**: Stellen Sie sicher, dass Plotly korrekt installiert ist

**Problem**: PDF-Export funktioniert nicht
- **Lösung**: Überprüfen Sie die ReportLab-Installation

### Logs und Debugging
```bash
streamlit run app.py --logger.level debug
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

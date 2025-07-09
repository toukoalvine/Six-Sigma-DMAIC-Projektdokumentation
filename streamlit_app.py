import streamlit as st
import pandas as pd
import numpy as np
import plotly
#import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from datetime import datetime, date
import io
import base64
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import zipfile
import json
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Six Sigma DMAIC Projekt-Dokumentationspaket",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        text-align: center;
    }
    
    .phase-header {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    
    .metric-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 1rem 0;
    }
    
    .success-metric {
        background: #d4edda;
        border-left-color: #28a745;
    }
    
    .warning-metric {
        background: #fff3cd;
        border-left-color: #ffc107;
    }
    
    .danger-metric {
        background: #f8d7da;
        border-left-color: #dc3545;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(52, 152, 219, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'project_data' not in st.session_state:
    st.session_state.project_data = {}

# Sidebar navigation
st.sidebar.title("🎯 Six Sigma DMAIC")
st.sidebar.markdown("---")

# Phase selection
phase = st.sidebar.radio(
    "Wählen Sie eine Phase:",
    ["📋 Projektübersicht", "🎯 Define", "📏 Measure", "🔍 Analyze", "💡 Improve", "🎛️ Control", "📊 Report Generator"]
)

# Main header
st.markdown('<div class="main-header"><h1>Six Sigma DMAIC Projekt-Dokumentationspaket</h1></div>', unsafe_allow_html=True)

# Helper functions
def calculate_sigma_level(dpmo):
    """Calculate Sigma Level from DPMO"""
    if dpmo <= 0:
        return 6.0
    elif dpmo >= 933193:
        return 0.0
    else:
        # Approximate calculation using normal distribution
        sigma_levels = {
            3.4: 6.0, 233: 5.0, 6210: 4.0, 66807: 3.0,
            158655: 2.0, 308538: 1.0, 500000: 0.0
        }
        
        # Find closest match
        closest_dpmo = min(sigma_levels.keys(), key=lambda x: abs(x - dpmo))
        return sigma_levels[closest_dpmo]

def create_sipoc_table(data):
    """Create SIPOC table"""
    df = pd.DataFrame(data)
    return df

def create_fishbone_chart():
    """Create fishbone diagram using plotly"""
    fig = go.Figure()
    
    # Main spine
    fig.add_trace(go.Scatter(
        x=[0, 10], y=[5, 5],
        mode='lines',
        line=dict(color='#2c3e50', width=4),
        showlegend=False
    ))
    
    # Categories
    categories = ['Mensch', 'Maschine', 'Material', 'Methode', 'Milieu', 'Messung']
    positions = [(2, 7), (2, 3), (4, 7), (4, 3), (6, 7), (6, 3)]
    
    for i, (cat, pos) in enumerate(zip(categories, positions)):
        # Category lines
        fig.add_trace(go.Scatter(
            x=[pos[0], pos[0]-1], y=[5, pos[1]],
            mode='lines',
            line=dict(color='#3498db', width=2),
            showlegend=False
        ))
        
        # Category labels
        fig.add_annotation(
            x=pos[0]-1.5, y=pos[1],
            text=cat,
            showarrow=False,
            font=dict(size=12, color='#2c3e50')
        )
    
    # Problem box
    fig.add_shape(
        type="rect",
        x0=9.5, y0=4.5, x1=11, y1=5.5,
        line=dict(color="#e74c3c", width=2),
        fillcolor="#e74c3c"
    )
    
    fig.add_annotation(
        x=10.25, y=5,
        text="Problem",
        showarrow=False,
        font=dict(size=12, color='white')
    )
    
    fig.update_layout(
        title="Ursache-Wirkungs-Diagramm (Fischgrätendiagramm)",
        xaxis=dict(range=[-2, 12], showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(range=[0, 10], showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white',
        height=400
    )
    
    return fig

def create_pareto_chart(categories, frequencies):
    """Create Pareto chart"""
    if not categories or not frequencies:
        return None
    
    # Create DataFrame and sort by frequency
    df = pd.DataFrame({'Category': categories, 'Frequency': frequencies})
    df = df.sort_values('Frequency', ascending=False)
    
    # Calculate cumulative percentage
    df['Cumulative'] = df['Frequency'].cumsum()
    df['Cumulative_Pct'] = (df['Cumulative'] / df['Frequency'].sum()) * 100
    
    # Create subplot
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Bar chart
    fig.add_trace(
        go.Bar(
            x=df['Category'],
            y=df['Frequency'],
            name='Häufigkeit',
            marker_color='#3498db'
        ),
        secondary_y=False,
    )
    
    # Line chart for cumulative percentage
    fig.add_trace(
        go.Scatter(
            x=df['Category'],
            y=df['Cumulative_Pct'],
            mode='lines+markers',
            name='Kumulativ %',
            line=dict(color='#e74c3c', width=3),
            marker=dict(size=8)
        ),
        secondary_y=True,
    )
    
    # Add 80% line
    fig.add_hline(
        y=80,
        line_dash="dash",
        line_color="red",
        annotation_text="80% Grenze",
        secondary_y=True
    )
    
    # Update layout
    fig.update_xaxes(title_text="Kategorien")
    fig.update_yaxes(title_text="Häufigkeit", secondary_y=False)
    fig.update_yaxes(title_text="Kumulativ %", secondary_y=True)
    fig.update_layout(title="Pareto-Analyse", height=500)
    
    return fig

def create_histogram(data, column):
    """Create histogram with normal distribution overlay"""
    fig = px.histogram(data, x=column, nbins=30, title=f"Histogram: {column}")
    
    # Add normal distribution curve
    mean = data[column].mean()
    std = data[column].std()
    x_range = np.linspace(data[column].min(), data[column].max(), 100)
    y_normal = stats.norm.pdf(x_range, mean, std)
    y_normal = y_normal * len(data) * (data[column].max() - data[column].min()) / 30
    
    fig.add_trace(go.Scatter(
        x=x_range,
        y=y_normal,
        mode='lines',
        name='Normalverteilung',
        line=dict(color='red', width=2)
    ))
    
    return fig

def create_control_chart(data, column):
    """Create control chart"""
    mean = data[column].mean()
    std = data[column].std()
    ucl = mean + 3 * std
    lcl = mean - 3 * std
    
    fig = go.Figure()
    
    # Data points
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data[column],
        mode='lines+markers',
        name='Messwerte',
        line=dict(color='blue')
    ))
    
    # Control limits
    fig.add_hline(y=mean, line_dash="solid", line_color="green", annotation_text="Mittelwert")
    fig.add_hline(y=ucl, line_dash="dash", line_color="red", annotation_text="UCL")
    fig.add_hline(y=lcl, line_dash="dash", line_color="red", annotation_text="LCL")
    
    fig.update_layout(
        title=f"Kontrollkarte: {column}",
        xaxis_title="Stichprobe",
        yaxis_title="Wert",
        height=400
    )
    
    return fig

def generate_report():
    """Generate comprehensive project report"""
    buffer = io.BytesIO()
    
    # Create PDF document
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.HexColor('#2c3e50'),
        alignment=1  # Center alignment
    )
    
    story.append(Paragraph("Six Sigma DMAIC Projekt Report", title_style))
    story.append(Spacer(1, 20))
    
    # Project basics
    if 'project_name' in st.session_state.project_data:
        project_info = [
            ['Projektname:', st.session_state.project_data.get('project_name', 'N/A')],
            ['Champion:', st.session_state.project_data.get('champion', 'N/A')],
            ['Belt:', st.session_state.project_data.get('belt', 'N/A')],
            ['Startdatum:', str(st.session_state.project_data.get('start_date', 'N/A'))],
            ['Enddatum:', str(st.session_state.project_data.get('end_date', 'N/A'))],
            ['Sigma Level:', f"{st.session_state.project_data.get('sigma_level', 'N/A')}"],
            ['DPMO:', f"{st.session_state.project_data.get('dpmo', 'N/A')}"]
        ]
        
        table = Table(project_info, colWidths=[2*inch, 3*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(table)
        story.append(Spacer(1, 20))
    
    # Add sections for each phase
    phases = ['Define', 'Measure', 'Analyze', 'Improve', 'Control']
    phase_data = {
        'Define': ['problem_statement', 'objective', 'scope', 'business_case'],
        'Measure': ['primary_metric', 'secondary_metrics', 'dpmo', 'sigma_level'],
        'Analyze': ['root_causes', 'hypotheses'],
        'Improve': ['solutions', 'implementation_plan'],
        'Control': ['control_plan', 'monitoring_plan']
    }
    
    for phase in phases:
        story.append(Paragraph(f"{phase} Phase", styles['Heading2']))
        
        # Add relevant data for each phase
        if phase.lower() in [key.lower() for key in phase_data.keys()]:
            for key in phase_data[phase]:
                if key in st.session_state.project_data:
                    story.append(Paragraph(f"{key.replace('_', ' ').title()}: {st.session_state.project_data[key]}", styles['Normal']))
        
        story.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    
    return buffer

# Main content based on selected phase
if phase == "📋 Projektübersicht":
    st.markdown('<div class="phase-header"><h2>Projektübersicht</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="metric-card"><h3>📊 Projekt Status</h3></div>', unsafe_allow_html=True)
        
        # Progress tracking
        phases_completed = st.slider("Abgeschlossene Phasen", 0, 5, 0)
        progress = phases_completed / 5
        st.progress(progress)
        st.write(f"Fortschritt: {progress*100:.0f}%")
        
        # Project timeline
        if 'start_date' in st.session_state.project_data and 'end_date' in st.session_state.project_data:
            start_date = st.session_state.project_data['start_date']
            end_date = st.session_state.project_data['end_date']
            today = date.today()
            
            if start_date <= today <= end_date:
                days_elapsed = (today - start_date).days
                total_days = (end_date - start_date).days
                time_progress = days_elapsed / total_days if total_days > 0 else 0
                st.metric("Zeitfortschritt", f"{time_progress*100:.1f}%")
    
    with col2:
        st.markdown('<div class="metric-card"><h3>🎯 Schnellzugriff</h3></div>', unsafe_allow_html=True)
        
        if st.button("🎯 Neues Projekt starten"):
            st.session_state.project_data = {}
            st.success("Neues Projekt initialisiert!")
        
        if st.button("💾 Projekt speichern"):
            if st.session_state.project_data:
                project_json = json.dumps(st.session_state.project_data, indent=2, default=str)
                st.download_button(
                    label="Download Projekt",
                    data=project_json,
                    file_name=f"six_sigma_project_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
    
    # Project summary cards
    if st.session_state.project_data:
        st.markdown("---")
        st.subheader("📋 Projekt-Zusammenfassung")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            project_name = st.session_state.project_data.get('project_name', 'Nicht definiert')
            st.metric("Projektname", project_name)
        
        with col2:
            sigma_level = st.session_state.project_data.get('sigma_level', 'N/A')
            st.metric("Sigma Level", f"{sigma_level}")
        
        with col3:
            dpmo = st.session_state.project_data.get('dpmo', 'N/A')
            st.metric("DPMO", f"{dpmo}")
        
        with col4:
            champion = st.session_state.project_data.get('champion', 'Nicht definiert')
            st.metric("Champion", champion)

elif phase == "🎯 Define":
    st.markdown('<div class="phase-header"><h2>Define Phase</h2></div>', unsafe_allow_html=True)
    
    # Project basics
    st.subheader("Projekt-Grunddaten")
    col1, col2 = st.columns(2)
    
    with col1:
        project_name = st.text_input("Projektname", value=st.session_state.project_data.get('project_name', ''))
        champion = st.text_input("Champion", value=st.session_state.project_data.get('champion', ''))
        belt = st.selectbox("Belt", ["", "Green Belt", "Black Belt", "Master Black Belt"], 
                           index=0 if st.session_state.project_data.get('belt', '') == '' else 
                           ["", "Green Belt", "Black Belt", "Master Black Belt"].index(st.session_state.project_data.get('belt', '')))
    
    with col2:
        start_date = st.date_input("Startdatum", value=st.session_state.project_data.get('start_date', date.today()))
        end_date = st.date_input("Geplantes Enddatum", value=st.session_state.project_data.get('end_date', date.today()))
        
        # Calculate project duration
        if start_date and end_date:
            duration = (end_date - start_date).days
            st.metric("Projektdauer", f"{duration} Tage")
    
    # Save project basics
    st.session_state.project_data.update({
        'project_name': project_name,
        'champion': champion,
        'belt': belt,
        'start_date': start_date,
        'end_date': end_date
    })
    
    st.markdown("---")
    
    # Problem Statement
    st.subheader("Problem Statement")
    col1, col2 = st.columns(2)
    
    with col1:
        problem_statement = st.text_area(
            "Problembeschreibung",
            value=st.session_state.project_data.get('problem_statement', ''),
            height=100,
            help="Beschreiben Sie das Problem (Was, Wann, Wo, Wie viel)"
        )
        
        objective = st.text_area(
            "Zielsetzung",
            value=st.session_state.project_data.get('objective', ''),
            height=100,
            help="Messbare Ziele definieren"
        )
    
    with col2:
        scope = st.text_area(
            "Projektscope",
            value=st.session_state.project_data.get('scope', ''),
            height=100,
            help="Was ist eingeschlossen/ausgeschlossen"
        )
        
        business_case = st.text_area(
            "Business Case",
            value=st.session_state.project_data.get('business_case', ''),
            height=100,
            help="Geschäftlicher Nutzen und erwartete Einsparungen"
        )
    
    # Save problem statement data
    st.session_state.project_data.update({
        'problem_statement': problem_statement,
        'objective': objective,
        'scope': scope,
        'business_case': business_case
    })
    
    st.markdown("---")
    
    # SIPOC Diagram
    st.subheader("SIPOC Diagramm")
    
    # Initialize SIPOC data if not exists
    if 'sipoc_data' not in st.session_state.project_data:
        st.session_state.project_data['sipoc_data'] = {
            'suppliers': [''],
            'inputs': [''],
            'process': [''],
            'outputs': [''],
            'customers': ['']
        }
    
    sipoc_data = st.session_state.project_data['sipoc_data']
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.write("**Suppliers**")
        suppliers = []
        for i in range(len(sipoc_data['suppliers'])):
            supplier = st.text_input(f"Supplier {i+1}", value=sipoc_data['suppliers'][i], key=f"supplier_{i}")
            suppliers.append(supplier)
        
        if st.button("+ Supplier hinzufügen"):
            sipoc_data['suppliers'].append('')
    
    with col2:
        st.write("**Inputs**")
        inputs = []
        for i in range(len(sipoc_data['inputs'])):
            input_val = st.text_input(f"Input {i+1}", value=sipoc_data['inputs'][i], key=f"input_{i}")
            inputs.append(input_val)
        
        if st.button("+ Input hinzufügen"):
            sipoc_data['inputs'].append('')
    
    with col3:
        st.write("**Process**")
        processes = []
        for i in range(len(sipoc_data['process'])):
            process = st.text_input(f"Process {i+1}", value=sipoc_data['process'][i], key=f"process_{i}")
            processes.append(process)
        
        if st.button("+ Process hinzufügen"):
            sipoc_data['process'].append('')
    
    with col4:
        st.write("**Outputs**")
        outputs = []
        for i in range(len(sipoc_data['outputs'])):
            output = st.text_input(f"Output {i+1}", value=sipoc_data['outputs'][i], key=f"output_{i}")
            outputs.append(output)
        
        if st.button("+ Output hinzufügen"):
            sipoc_data['outputs'].append('')
    
    with col5:
        st.write("**Customers**")
        customers = []
        for i in range(len(sipoc_data['customers'])):
            customer = st.text_input(f"Customer {i+1}", value=sipoc_data['customers'][i], key=f"customer_{i}")
            customers.append(customer)
        
        if st.button("+ Customer hinzufügen"):
            sipoc_data['customers'].append('')
    
    # Update SIPOC data
    st.session_state.project_data['sipoc_data'] = {
        'suppliers': suppliers,
        'inputs': inputs,
        'process': processes,
        'outputs': outputs,
        'customers': customers
    }
    
    st.markdown("---")
    
    # CTQ Tree
    st.subheader("CTQ Tree (Critical to Quality)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Kundenbedürfnis**")
        customer_need = st.text_input("Primäres Bedürfnis", value=st.session_state.project_data.get('customer_need', ''))
    
    with col2:
        st.write("**Treiber**")
        driver1 = st.text_input("Treiber 1", value=st.session_state.project_data.get('driver1', ''))
        driver2 = st.text_input("Treiber 2", value=st.session_state.project_data.get('driver2', ''))
    
    with col3:
        st.write("**CTQ Anforderungen**")
        ctq1 = st.text_input("CTQ 1", value=st.session_state.project_data.get('ctq1', ''))
        ctq2 = st.text_input("CTQ 2", value=st.session_state.project_data.get('ctq2', ''))
        ctq3 = st.text_input("CTQ 3", value=st.session_state.project_data.get('ctq3', ''))
    
    # Save CTQ data
    st.session_state.project_data.update({
        'customer_need': customer_need,
        'driver1': driver1,
        'driver2': driver2,
        'ctq1': ctq1,
        'ctq2': ctq2,
        'ctq3': ctq3
    })

elif phase == "📏 Measure":
    st.markdown('<div class="phase-header"><h2>Measure Phase</h2></div>', unsafe_allow_html=True)
    
    # Metrics Definition
    st.subheader("Metriken Definition")
    col1, col2 = st.columns(2)
    
    with col1:
        primary_metric = st.text_input("Primäre Metrik (Y)", value=st.session_state.project_data.get('primary_metric', ''))
        secondary_metrics = st.text_area("Sekundäre Metriken", value=st.session_state.project_data.get('secondary_metrics', ''))
        data_source = st.text_input("Datenquelle", value=st.session_state.project_data.get('data_source', ''))
    
    with col2:
        sample_size = st.number_input("Stichprobengröße", min_value=1, value=st.session_state.project_data.get('sample_size', 30))
        collection_period = st.text_input("Sammlungsperiode", value=st.session_state.project_data.get('collection_period', ''))
        collection_frequency = st.selectbox("Sammlungsfrequenz", 
                                          ["Stündlich", "Täglich", "Wöchentlich", "Monatlich"],
                                          index=0 if st.session_state.project_data.get('collection_frequency', '') == '' else 
                                          ["Stündlich", "Täglich", "Wöchentlich", "Monatlich"].index(st.session_state.project_data.get('collection_frequency', 'Täglich')))
    
    # Save measure data
    st.session_state.project_data.update({
        'primary_metric': primary_metric,
        'secondary_metrics': secondary_metrics,
        'data_source': data_source,
        'sample_size': sample_size,
        'collection_period': collection_period,
        'collection_frequency': collection_frequency
    })
    
    st.markdown("---")
    
    # Baseline Measurement
    st.subheader("Baseline Messung")
    col1, col2 = st.columns(2)
    
    with col1:
        dpmo = st.number_input("DPMO (Defects Per Million Opportunities)", min_value=0, value=st.session_state.project_data.get('dpmo', 66807))
        cp = st.number_input("Prozessleistung (Cp)", min_value=0.0, value=st.session_state.project_data.get('cp', 1.0), step=0.01)
        cpk = st.number_input("Prozessleistung (Cpk)", min_value=0.0, value=st.session_state.project_data.get('cpk', 1.0), step=0.01)
        
        # Calculate Sigma Level
        sigma_level = calculate_sigma_level(dpmo)
        st.metric("Aktueller Sigma Level", f"{sigma_level:.1f}")
    
    with col2:
        st.markdown('<div class="metric-card"><h4>Prozess-Bewertung</h4></div>', unsafe_allow_html=True)
        
        # Process capability assessment
        if cpk >= 1.33:
            st.markdown('<div class="metric-card success-metric">✅ Prozess ist fähig (Cpk ≥ 1.33)</div>', unsafe_allow_html=True)
        elif cpk >= 1.0:
            st.markdown('<div class="metric-card warning-metric">⚠️ Prozess ist marginal (1.0 ≤ Cpk < 1.33)</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="metric-card danger-metric">❌ Prozess ist nicht fähig (Cpk < 1.0)</div>', unsafe_allow_html=True)
        
        # Sigma level assessment
        if sigma_level >= 4.0:
            st.success(f"Exzellenter Sigma Level ({sigma_level:.1f})")
        elif sigma_level >= 3.0:
            st.warning(f"Guter Sigma Level ({sigma_level:.1f})")
        else:
            st.error(f"Verbesserungsbedarf ({sigma_level:.1f})")
    
    # Save baseline data
    st.session_state.project_data

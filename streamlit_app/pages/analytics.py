import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.ab_testing import ab_testing

st.set_page_config(page_title="Analytics & Insights", page_icon="📈", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');

:root {
    --primary: #00ff7f;
    --secondary: #ff00ff;
    --bg-dark: #050508;
    --bg-glass: rgba(15, 15, 15, 0.7);
}

.stApp {
    background: linear-gradient(180deg, #050508 0%, #0a0a15 50%, #050508 100%) !important;
    font-family: 'Rajdhani', sans-serif !important;
    color: #ffffff !important;
}

.scanline-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 9999;
    pointer-events: none;
    background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0, 0, 0, 0.03) 2px, rgba(0, 0, 0, 0.03) 4px);
}

.bg-grid {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background-image: 
        linear-gradient(rgba(0, 255, 127, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 255, 127, 0.02) 1px, transparent 1px);
    background-size: 60px 60px;
    animation: gridScroll 30s linear infinite;
}

@keyframes gridScroll {
    0% { transform: translate(0, 0); }
    100% { transform: translate(60px, 60px); }
}

h1, h2, h3 {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    color: #00ff7f !important;
}

h1 { font-size: 1.8rem !important; }

/* Futuristic Cards */
.futuristic-card {
    background: linear-gradient(135deg, rgba(20, 20, 35, 0.9) 0%, rgba(10, 10, 20, 0.95) 100%) !important;
    border: none !important;
    border-radius: 0px !important;
    padding: 25px !important;
    position: relative;
    transition: all 0.3s ease !important;
}

.futuristic-card:hover {
    border: 1px solid rgba(0, 255, 127, 0.3) !important;
    box-shadow: 0 10px 40px rgba(0, 255, 127, 0.15) !important;
}

/* Stat Cards */
.stat-card {
    background: linear-gradient(135deg, rgba(0, 255, 127, 0.1) 0%, rgba(15, 15, 25, 0.95) 100%) !important;
    border: 1px solid rgba(0, 255, 127, 0.3) !important;
    border-radius: 0px !important;
    padding: 25px !important;
    text-align: center;
    position: relative;
}

.stat-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00ff7f, transparent);
}

.stat-value {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 2.5rem !important;
    font-weight: 700 !important;
    color: #00ff7f !important;
    text-shadow: 0 0 20px rgba(0, 255, 127, 0.5) !important;
}

.stat-label {
    color: rgba(255, 255, 255, 0.5) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 2px !important;
}

/* Pulse Animation */
.pulse-dot {
    display: inline-block;
    width: 10px;
    height: 10px;
    background: #00ff7f;
    border-radius: 50%;
    animation: pulse 2s ease-in-out infinite;
    margin-left: 8px;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.2); }
}

/* Terminal Window */
.terminal-window {
    background: rgba(0, 0, 0, 0.9) !important;
    border: 1px solid rgba(0, 255, 127, 0.3) !important;
    border-radius: 0px !important;
    padding: 20px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.8rem !important;
    max-height: 400px;
    overflow-y: auto;
}

.terminal-line {
    color: #00ff7f !important;
    margin: 5px 0;
    display: flex;
    align-items: center;
}

.terminal-line::before {
    content: '>';
    color: #00ff7f;
    margin-right: 10px;
}

.terminal-line .timestamp {
    color: rgba(0, 255, 127, 0.5);
    margin-left: 10px;
    font-size: 0.7rem;
}

/* Conversion Funnel - Tapered Shape */
.funnel-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
}

.funnel-step {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 15px;
    color: #fff;
    font-family: 'JetBrains Mono', monospace;
    text-align: center;
    position: relative;
}

.funnel-step::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 50%;
    transform: translateX(-50%);
    border-left: 30px solid transparent;
    border-right: 30px solid transparent;
    border-top: 5px solid transparent;
}

.insight-box {
    background: linear-gradient(135deg, rgba(0,255,127,0.1) 0%, rgba(15,15,25,0.95) 100%);
    padding: 15px;
    border-radius: 0px;
    border-left: 3px solid #00ff7f;
    margin: 10px 0;
    font-family: 'JetBrains Mono', monospace;
}

::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #00ff7f; border-radius: 2px; }
</style>

<div class="scanline-overlay"></div>
<div class="bg-grid"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 40px 20px 30px;">
    <h1>Analytics & Insights</h1>
    <p style="color: rgba(255,255,255,0.4); font-size: 1rem; letter-spacing: 4px; margin-top: 10px; font-family: 'JetBrains Mono', monospace;">
        A/B TEST RESULTS // USAGE STATISTICS
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("### A/B TEST RESULTS")

stats = ab_testing.get_experiment_stats('prediction_ui')

if stats and stats.get('events'):
    col1, col2, col3, col4 = st.columns(4)
    
    total_events = len(stats['events'])
    unique_users = len(set([e['user_id'] for e in stats['events']]))
    
    variant_counts = {}
    for event in stats['events']:
        v = event.get('variant', 'unknown')
        variant_counts[v] = variant_counts.get(v, 0) + 1
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <p class="stat-value">{total_events}</p>
            <p class="stat-label">TOTAL EVENTS</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <p class="stat-value">{unique_users}<span class="pulse-dot"></span></p>
            <p class="stat-label">UNIQUE USERS</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        variant_a = variant_counts.get('A', 0)
        st.markdown(f"""
        <div class="stat-card">
            <p class="stat-value" style="color: #00ffd5 !important;">{variant_a}</p>
            <p class="stat-label">VARIANT A</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        variant_b = variant_counts.get('B', 0)
        st.markdown(f"""
        <div class="stat-card">
            <p class="stat-value" style="color: #ff00ff !important; text-shadow: 0 0 20px rgba(255,0,255,0.5) !important;">{variant_b}</p>
            <p class="stat-label">VARIANT B</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        event_types = {}
        for event in stats['events']:
            e = event.get('event', 'unknown')
            event_types[e] = event_types.get(e, 0) + 1
        
        fig_events = go.Figure(data=[
            go.Pie(labels=list(event_types.keys()), values=list(event_types.values()),
                   hole=0.5, marker_colors=['#00ff7f', '#00ffd5', '#ff00ff', '#ffa502'])
        ])
        fig_events.update_layout(
            title=dict(text='EVENT DISTRIBUTION', font=dict(family='JetBrains Mono', size=12, color='#00ff7f'), x=0.5),
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='JetBrains Mono', color='#fff')
        )
        st.plotly_chart(fig_events, use_container_width=True)
    
    with col_chart2:
        variant_event_types = {'A': {}, 'B': {}}
        for event in stats['events']:
            v = event.get('variant', 'unknown')
            e = event.get('event', 'unknown')
            if v in variant_event_types:
                variant_event_types[v][e] = variant_event_types[v].get(e, 0) + 1
        
        events = list(set([e['event'] for e in stats['events']]))
        
        fig_compare = go.Figure()
        for variant in ['A', 'B']:
            values = [variant_event_types[variant].get(e, 0) for e in events]
            fig_compare.add_trace(go.Bar(
                name=f'Variant {variant}',
                x=events,
                y=values,
                marker_color='#00ff7f' if variant == 'A' else '#ff00ff'
            ))
        
        fig_compare.update_layout(
            title=dict(text='EVENTS BY VARIANT', font=dict(family='JetBrains Mono', size=12, color='#00ff7f'), x=0.5),
            barmode='group',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='JetBrains Mono', color='#fff'),
            legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#fff', family='JetBrains Mono'))
        )
        st.plotly_chart(fig_compare, use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("### CONVERSION FUNNEL")
    
    funnel_data = {}
    for event in stats['events']:
        e = event.get('event', 'unknown')
        v = event.get('variant', 'unknown')
        if v not in funnel_data:
            funnel_data[v] = {}
        funnel_data[v][e] = funnel_data[v].get(e, 0) + 1
    
    for variant in ['A', 'B']:
        st.markdown(f"**// VARIANT {variant}**")
        if variant in funnel_data:
            funnel_widths = [100, 80, 60, 40]
            for i, (event_name, count) in enumerate(sorted(funnel_data[variant].items(), key=lambda x: x[1], reverse=True)[:4]):
                width = funnel_widths[i] if i < len(funnel_widths) else 30
                st.markdown(f"""
                <div class="insight-box" style="width: {width}%; margin: 5px auto;">
                    <strong style="color: #00ff7f;">{event_name}</strong> : {count}
                </div>
                """, unsafe_allow_html=True)
    
else:
    st.info("// No A/B test data yet. Tracking is ready!")

st.markdown("---")

st.markdown("### USER FEEDBACK")

feedback = ab_testing.get_feedback_stats()

if feedback:
    col_fb1, col_fb2 = st.columns(2)
    
    with col_fb1:
        feedback_types = {}
        for f in feedback:
            ft = f.get('feedback_type', 'unknown')
            feedback_types[ft] = feedback_types.get(ft, 0) + 1
        
        fig_fb = go.Figure(data=[
            go.Bar(x=list(feedback_types.keys()), y=list(feedback_types.values()),
                   marker_color='#00ff7f')
        ])
        fig_fb.update_layout(
            title=dict(text='FEEDBACK DISTRIBUTION', font=dict(family='JetBrains Mono', size=12, color='#00ff7f'), x=0.5),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='JetBrains Mono', color='#fff')
        )
        st.plotly_chart(fig_fb, use_container_width=True)
    
    with col_fb2:
        positive = len([f for f in feedback if f.get('feedback_type') == 'positive'])
        negative = len([f for f in feedback if f.get('feedback_type') == 'negative'])
        neutral = len([f for f in feedback if f.get('feedback_type') == 'neutral'])
        
        sentiment_data = go.Figure(data=[
            go.Pie(labels=['Positive', 'Negative', 'Neutral'], 
                   values=[positive, negative, neutral],
                   hole=0.5,
                   marker_colors=['#00ff7f', '#ff00ff', '#ffa502'])
        ])
        sentiment_data.update_layout(
            title=dict(text='SENTIMENT ANALYSIS', font=dict(family='JetBrains Mono', size=12, color='#00ff7f'), x=0.5),
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='JetBrains Mono', color='#fff')
        )
        st.plotly_chart(sentiment_data, use_container_width=True)
    
    with st.expander("VIEW ALL FEEDBACK"):
        feedback_df = pd.DataFrame(feedback)
        st.dataframe(feedback_df, use_container_width=True)
        
        csv = feedback_df.to_csv(index=False)
        st.download_button("DOWNLOAD CSV", csv, "feedback.csv", "text/csv")

else:
    st.info("// No feedback yet.")

st.markdown("---")

st.markdown("### TRACKED EVENTS // TERMINAL")

if stats and stats.get('events'):
    st.markdown("""
    <div class="terminal-window">
    """, unsafe_allow_html=True)
    
    recent_events = sorted(stats['events'], key=lambda x: x.get('timestamp', ''), reverse=True)[:20]
    for event in recent_events:
        ts = event.get('timestamp', '')[-8:] if event.get('timestamp') else ''
        st.markdown(f"""
        <div class="terminal-line">
            {event.get('event', 'unknown')} | {event.get('variant', 'unknown')} | {event.get('metadata', {}).get('model', 'N/A')}
            <span class="timestamp">{ts}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="terminal-window">
        <p style="color: rgba(0,255,127,0.5);">// Waiting for events...</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("// Data stored locally in data/ab_test_experiments.json // JetBrains Mono")
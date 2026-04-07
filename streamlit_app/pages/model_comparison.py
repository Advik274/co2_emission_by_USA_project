import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import utils

st.set_page_config(page_title="Model Comparison", page_icon="📊")

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

.glow-orb {
    position: fixed;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255, 0, 255, 0.04) 0%, transparent 70%);
    bottom: -100px;
    left: -100px;
    animation: orbFloat 25s ease-in-out infinite reverse;
    z-index: -1;
}

@keyframes orbFloat {
    0%, 100% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(30px, 30px) scale(1.1); }
}

h1, h2, h3 {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    color: #00ff7f !important;
}

h1 { font-size: 2rem !important; }

/* Futuristic Cards with Corner Brackets */
.futuristic-card {
    background: linear-gradient(135deg, rgba(20, 20, 35, 0.9) 0%, rgba(10, 10, 20, 0.95) 100%) !important;
    border: none !important;
    border-radius: 0px !important;
    padding: 30px !important;
    position: relative;
    transition: all 0.4s ease !important;
}

.futuristic-card::before,
.futuristic-card::after {
    content: '';
    position: absolute;
    width: 15px;
    height: 15px;
    border-color: #00ff7f;
    border-style: solid;
}

.futuristic-card::before {
    top: -1px;
    left: -1px;
    border-width: 2px 0 0 2px;
}

.futuristic-card::after {
    bottom: -1px;
    right: -1px;
    border-width: 0 2px 2px 0;
}

.futuristic-card:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 15px 50px rgba(0, 255, 127, 0.15) !important;
}

.best-model {
    border: 2px solid #00ff7f !important;
    box-shadow: 0 0 60px rgba(0, 255, 127, 0.3), inset 0 0 30px rgba(0, 255, 127, 0.05) !important;
}

/* R² Gauge */
.r2-gauge {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: conic-gradient(#00ff7f 0deg, #00ff7f var(--r2-deg, 0deg), transparent var(--r2-deg, 0deg));
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
    position: relative;
}

.r2-gauge::before {
    content: '';
    position: absolute;
    width: 90px;
    height: 90px;
    border-radius: 50%;
    background: rgba(15, 15, 25, 0.95);
}

.r2-value {
    position: relative;
    z-index: 1;
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.2rem;
    font-weight: 700;
    color: #00ff7f;
}

/* Metric Badge */
.metric-badge {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 0px;
    background: rgba(0, 255, 127, 0.1);
    border: 1px solid rgba(0, 255, 127, 0.4);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #00ff7f;
    margin: 5px;
}

/* Recommended Badge */
.recommended-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(255, 165, 0, 0.2));
    border: 1px solid #ffd700;
    border-radius: 0px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #ffd700;
    margin-left: 10px;
}

.stSelectbox > div > div:first-child {
    background: rgba(15, 15, 25, 0.9) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(0, 255, 127, 0.3) !important;
    border-radius: 0px !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border: 1px solid rgba(0, 255, 127, 0.15) !important;
    border-radius: 0px !important;
    color: rgba(255,255,255,0.5) !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.stTabs [aria-selected="true"] {
    background: rgba(0, 255, 127, 0.1) !important;
    border: 1px solid #00ff7f !important;
    color: #00ff7f !important;
}

::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #00ff7f; border-radius: 2px; }
</style>

<div class="scanline-overlay"></div>
<div class="bg-grid"></div>
<div class="glow-orb"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 40px 20px 30px;">
    <h1>Model Performance</h1>
    <p style="color: rgba(255,255,255,0.4); font-size: 1rem; letter-spacing: 4px; margin-top: 10px; font-family: 'JetBrains Mono', monospace;">
        TRAINED ML MODELS COMPARISON
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

metrics = utils.get_model_metrics()
ann_models = utils.get_ann_model_info()

st.markdown("### PERFORMANCE METRICS")

selected_model = st.selectbox("SELECT MODEL", list(metrics.keys()) + ann_models)

if selected_model in metrics:
    model_data = metrics[selected_model]
    is_best = model_data.get('R2', 0) > 0.98
    r2_val = model_data.get('R2', 0)
    r2_deg = r2_val * 360
    
    st.markdown(f"""
    <div class="futuristic-card {'best-model' if is_best else ''}" style="margin: 20px 0;">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <h3 style="color: #00ff7f !important; margin: 0; font-size: 1.1rem !important;">
                {selected_model}
                {f'<span class="recommended-badge">★ AI VERIFIED</span>' if is_best else ''}
            </h3>
            <div class="r2-gauge" style="--r2-deg: {r2_deg}deg;">
                <span class="r2-value">{r2_val:.4f}</span>
            </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 20px 0;">
            <span class="metric-badge">MSE: {model_data.get('MSE', 'N/A')}</span>
            <span class="metric-badge">R²: {model_data.get('R2', 'N/A')}</span>
            <span class="metric-badge">MSE (Log): {model_data.get('MSE_log', 'N/A')}</span>
            <span class="metric-badge">R² (Log): {model_data.get('R2_log', 'N/A')}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="futuristic-card" style="margin: 20px 0;">
        <h3 style="color: #ff00ff !important; margin: 0 0 15px 0;">{selected_model}</h3>
        <p style="color: #888; font-family: 'JetBrains Mono', monospace;">Neural network for predictions</p>
        <p style="color: #00ff7f; margin-top: 10px; font-family: 'JetBrains Mono', monospace;">Architecture: Deep Learning (TensorFlow)</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("### COMPARISON CHARTS")

comparison_data = []
for model_name, data in metrics.items():
    comparison_data.append({
        'Model': model_name,
        'MSE (Original)': data.get('MSE'),
        'R² (Original)': data.get('R2'),
        'MSE (Log)': data.get('MSE_log'),
        'R² (Log)': data.get('R2_log')
    })

comparison_df = pd.DataFrame(comparison_data)

tab1, tab2 = st.tabs(["R² SCORE COMPARISON", "MSE COMPARISON"])

with tab1:
    colors = ['#00ff7f' if r2 > 0.98 else '#00ffd5' for r2 in comparison_df['R² (Original)']]
    fig_r2 = go.Figure()
    fig_r2.add_trace(go.Bar(
        name='R² (Original Scale)',
        x=comparison_df['Model'],
        y=comparison_df['R² (Original)'],
        marker_color=colors,
        text=[f"{r:.4f}" for r in comparison_df['R² (Original)']],
        textposition='auto',
        textfont=dict(family='JetBrains Mono', color='#050508')
    ))
    fig_r2.add_trace(go.Bar(
        name='R² (Log Scale)',
        x=comparison_df['Model'],
        y=comparison_df['R² (Log)'],
        marker_color='#ff00ff'
    ))
    fig_r2.update_layout(
        title=dict(text='R² SCORE (HIGHER = BETTER)', font=dict(family='JetBrains Mono', size=14, color='#00ff7f'), x=0.5),
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='JetBrains Mono', color='#fff'),
        xaxis=dict(gridcolor='rgba(0,255,127,0.1)', tickfont=dict(color='#fff')),
        yaxis=dict(gridcolor='rgba(0,255,127,0.1)', tickfont=dict(color='#fff'), range=[0, 1.1]),
        legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#fff', family='JetBrains Mono'))
    )
    st.plotly_chart(fig_r2, use_container_width=True)

with tab2:
    fig_mse = go.Figure()
    fig_mse.add_trace(go.Bar(
        name='MSE (Original)',
        x=comparison_df['Model'],
        y=comparison_df['MSE (Original)'],
        marker_color='#ff00ff'
    ))
    fig_mse.add_trace(go.Bar(
        name='MSE (Log)',
        x=comparison_df['Model'],
        y=comparison_df['MSE (Log)'],
        marker_color='#ffa502'
    ))
    fig_mse.update_layout(
        title=dict(text='MSE (LOWER = BETTER)', font=dict(family='JetBrains Mono', size=14, color='#ff00ff'), x=0.5),
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='JetBrains Mono', color='#fff'),
        xaxis=dict(gridcolor='rgba(0,255,127,0.1)', tickfont=dict(color='#fff')),
        yaxis=dict(gridcolor='rgba(0,255,127,0.1)', tickfont=dict(color='#fff')),
        legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#fff', family='JetBrains Mono'))
    )
    st.plotly_chart(fig_mse, use_container_width=True)

st.markdown("---")

st.markdown("### RECOMMENDATIONS")

col_rec1, col_rec2 = st.columns(2)

with col_rec1:
    st.markdown("""
    <div class="futuristic-card">
        <h4 style="color: #00ff7f !important; margin: 0 0 15px 0; font-family: 'JetBrains Mono', monospace;">// BEST BY METRIC</h4>
        <table style="width: 100%; color: #fff; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;">
            <tr style="border-bottom: 1px solid rgba(0,255,127,0.2);"><td style="padding: 10px;">🥇 R² (Original)</td><td style="padding: 10px; color: #00ff7f;">Random Forest: 0.9917</td></tr>
            <tr style="border-bottom: 1px solid rgba(0,255,127,0.2);"><td style="padding: 10px;">🥇 MSE (Original)</td><td style="padding: 10px; color: #00ff7f;">Random Forest: 367.51</td></tr>
            <tr><td style="padding: 10px;">🥇 R² (Log)</td><td style="padding: 10px; color: #00ff7f;">Random Forest: 0.9831</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col_rec2:
    st.markdown("""
    <div class="futuristic-card">
        <h4 style="color: #ff00ff !important; margin: 0 0 15px 0; font-family: 'JetBrains Mono', monospace;">// USE CASE</h4>
        <table style="width: 100%; color: #fff; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;">
            <tr style="border-bottom: 1px solid rgba(255,0,255,0.2);"><td style="padding: 10px;">Production</td><td style="padding: 10px; color: #00ff7f;">Random Forest</td><td style="padding: 10px; color: #888;">Best accuracy</td></tr>
            <tr style="border-bottom: 1px solid rgba(255,0,255,0.2);"><td style="padding: 10px;">Speed</td><td style="padding: 10px; color: #00ff7f;">XGBoost</td><td style="padding: 10px; color: #888;">Fast inference</td></tr>
            <tr><td style="padding: 10px;">Deep Learning</td><td style="padding: 10px; color: #00ff7f;">Simple ANN</td><td style="padding: 10px; color: #888;">Lightweight</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("### FEATURE COMPARISON")

feature_df = pd.DataFrame({
    'Model': ['Random Forest', 'XGBoost', 'ANN'],
    'Type': ['Ensemble', 'Boosting', 'Neural Net'],
    'Speed': ['Fast', 'Fast', 'Medium'],
    'Accuracy': ['Highest', 'High', 'High'],
    'Interpretability': ['High', 'Medium', 'Low']
})
st.dataframe(feature_df, hide_index=True, use_container_width=True)

st.markdown("---")
st.caption("Metrics based on research paper evaluation // JetBrains Mono")
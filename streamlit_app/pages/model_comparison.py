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
    .stApp { background-color: #0e1117; }
    h1, h2, h3 { color: #00d4aa !important; }
    .model-card {
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #00d4aa33;
    }
    .best-model {
        border: 2px solid #00d4aa;
        box-shadow: 0 0 20px rgba(0, 212, 170, 0.3);
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Model Performance Comparison")
st.markdown("Compare the performance of different trained machine learning models")

metrics = utils.get_model_metrics()
ann_models = utils.get_ann_model_info()

st.markdown("### 🎯 Performance Metrics")

col1, col2, col3 = st.columns(3)

model_names = list(metrics.keys()) + ann_models
selected_model = st.selectbox("Select Model to View Details", model_names)

if selected_model in metrics:
    model_data = metrics[selected_model]
    st.markdown(f"""
    <div class="model-card {'best-model' if model_data.get('R2', 0) > 0.98 else ''}">
        <h3>{selected_model}</h3>
        <p><strong>MSE (Original Scale):</strong> {model_data.get('MSE', 'N/A')}</p>
        <p><strong>R² (Original Scale):</strong> {model_data.get('R2', 'N/A')}</p>
        <p><strong>MSE (Log Scale):</strong> {model_data.get('MSE_log', 'N/A')}</p>
        <p><strong>R² (Log Scale):</strong> {model_data.get('R2_log', 'N/A')}</p>
        {f"<p><em>{model_data.get('note', '')}</em></p>" if 'note' in model_data else ""}
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="model-card">
        <h3>{selected_model}</h3>
        <p><em>Neural network model available for predictions</em></p>
        <p>Architecture: Deep Learning (TensorFlow/Keras)</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 📈 Model Comparison Charts")

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

fig_r2 = go.Figure()
fig_r2.add_trace(go.Bar(
    name='R² (Original Scale)',
    x=comparison_df['Model'],
    y=comparison_df['R² (Original)'],
    marker_color='#00d4aa'
))
fig_r2.add_trace(go.Bar(
    name='R² (Log Scale)',
    x=comparison_df['Model'],
    y=comparison_df['R² (Log)'],
    marker_color='#4ecdc4'
))

fig_r2.update_layout(
    title='R² Score Comparison',
    xaxis_title='Model',
    yaxis_title='R² Score',
    barmode='group',
    paper_bgcolor='transparent',
    plot_bgcolor='transparent',
    font_color='#fff',
    legend=dict(bgcolor='rgba(0,0,0,0)')
)
st.plotly_chart(fig_r2, use_container_width=True)

fig_mse = go.Figure()
fig_mse.add_trace(go.Bar(
    name='MSE (Original Scale)',
    x=comparison_df['Model'],
    y=comparison_df['MSE (Original)'],
    marker_color='#ff6b6b'
))
fig_mse.add_trace(go.Bar(
    name='MSE (Log Scale)',
    x=comparison_df['Model'],
    y=comparison_df['MSE (Log)'],
    marker_color='#ffa502'
))

fig_mse.update_layout(
    title='MSE Comparison (Lower is Better)',
    xaxis_title='Model',
    yaxis_title='Mean Squared Error',
    barmode='group',
    paper_bgcolor='transparent',
    plot_bgcolor='transparent',
    font_color='#fff',
    legend=dict(bgcolor='rgba(0,0,0,0)')
)
st.plotly_chart(fig_mse, use_container_width=True)

st.markdown("---")

st.markdown("### 🏆 Model Recommendations")

st.markdown("""
| Use Case | Recommended Model | Reason |
|----------|-------------------|--------|
| Best Overall | Random Forest | Highest R² (0.9917), Lowest MSE (367.51) |
| Fast Predictions | XGBoost | Good balance of accuracy and speed |
| Deep Learning | Simple ANN | Lightweight neural network |
| Complex Patterns | Deeper ANN | More layers for complex relationships |
""")

st.markdown("---")
st.markdown("*Metrics based on research paper evaluation results*")
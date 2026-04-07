# USA Carbon Emissions Analysis & Prediction

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13%2B-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0%2B-green)

A comprehensive research-based project analyzing carbon dioxide emissions across the United States, featuring interactive dashboards, future predictions, and comparison of multiple machine learning models.

## 📋 Project Overview

This project explores historical CO2 emission data from the U.S. Energy Information Administration (EIA) and builds predictive models to forecast future emissions. The research analyzes emissions across different states, sectors (Commercial, Electric Power, Industrial, Residential, Transportation), and fuel types (Coal, Natural Gas, Petroleum).

### Research Paper
- **Title**: Future Carbon Emission Horizons of USA
- **Data Source**: EIA API (U.S. Energy Information Administration)
- **Analysis Period**: Multiple years of historical data

## 🎯 Features

### 1. Dashboard (Home)
- Interactive visualizations of CO2 emissions over time
- Breakdown by sector, fuel type, and state
- Key metrics and statistics
- Filterable by state, sector, and fuel type

### 2. Future Predictions
- **Single Prediction**: Predict CO2 emissions for a specific future year
- **Multi-Year Forecast**: Generate predictions for a range of years
- Model selection: Random Forest, XGBoost, or various ANN architectures
- Confidence intervals for predictions
- Historical trend visualization with predictions

### 3. Model Comparison
- Performance metrics for all trained models
- R² and MSE comparisons
- Model recommendations for different use cases

## 🤖 Trained Models

| Model | R² Score | MSE | Best For |
|-------|----------|-----|----------|
| Random Forest | 0.9917 | 367.51 | Best overall accuracy |
| XGBoost | 0.9806 | 857.62 | Balance of speed & accuracy |
| Simple ANN | - | - | Lightweight inference |
| Deeper ANN | - | - | Complex patterns |
| Wider ANN | - | - | Feature-rich data |
| ANN with Dropout | - | - | Regularized training |
| ANN with L2 | - | - | Preventing overfitting |

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Interactive Web UI)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib
- **ML Models**: 
  - Scikit-learn (Random Forest)
  - XGBoost
  - TensorFlow/Keras (Neural Networks)
- **Deployment**: Streamlit Cloud / Heroku

## 📁 Project Structure

```
project/
├── data/
│   ├── raw/                    # Original CO2 emission data
│   └── processed/             # Train/test splits
├── notebooks/                  # Research Jupyter notebooks
├── models/
│   ├── rf/                     # Random Forest (if available)
│   ├── xgboost/               # Trained XGBoost model
│   └── ann/                   # ANN model files (.keras)
├── src/
│   └── utils.py               # Data loading & utilities
├── streamlit_app/
│   ├── app.py                 # Main dashboard
│   ├── pages/
│   │   ├── predictions.py     # Future predictions
│   │   └── model_comparison.py # Model comparison
├── .env.example               # Environment variables template
├── .gitignore
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd project
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
cd streamlit_app
streamlit run app.py
```

The application will open at `http://localhost:8501`

### 5. Environment Variables (Optional)
```bash
# Copy .env.example to .env and configure
cp .env.example .env
```

## 📊 Usage Guide

### Dashboard Page
1. Use sidebar filters to select state, sector, and fuel type
2. View aggregate metrics (total, average, min, max emissions)
3. Explore tabs for different visualization types

### Predictions Page
1. Select state, sector, and fuel type from dropdowns
2. Choose prediction year (preset or custom)
3. Select model type
4. Click "Generate Prediction" to see results
5. Use Multi-Year Forecast section for range predictions

### Model Comparison Page
1. View detailed performance metrics
2. Compare R² and MSE across models
3. Get recommendations for model selection

## 🔬 Research Summary

### Data Preprocessing
- Log transformation of emission values
- 1-year lag feature engineering
- 3-year rolling mean calculation
- One-hot encoding for categorical variables

### Model Training
- 80/20 train/test split
- Random Forest achieved best performance (R² = 0.9917)
- XGBoost trained as alternative (R² = 0.9806)
- Multiple ANN architectures tested

### Key Findings
- Transportation sector is the largest emitter
- Petroleum is the dominant fuel source
- Significant variation across states
- Strong temporal patterns in emissions data

## 📝 License

This project is for educational and research purposes.

## 🙏 Acknowledgments

- U.S. Energy Information Administration for data
- Research methodology based on machine learning best practices

---

**Author**: Research Team  
**Last Updated**: April 2026
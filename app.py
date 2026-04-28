import streamlit as st
import os
import json
from run import generate_demo_results
import pandas as pd

st.set_page_config(page_title="ML Audit Dashboard", layout="wide")

st.title("📊 ML Audit Dashboard")

results_file = 'results/audit_results.json'

# generate if not exists
if not os.path.exists(results_file):
    os.makedirs('results', exist_ok=True)
    results = generate_demo_results()
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)

# load data
with open(results_file) as f:
    data = json.load(f)

# 🔥 TOP METRICS
col1, col2, col3 = st.columns(3)

col1.metric("Accuracy", data["model_performance"]["accuracy"])
col2.metric("Fraud Detected", data["audit_summary"]["fraud_flagged"])
col3.metric("Fairness", data["audit_summary"]["fairness_score"])

# 🔥 SUMMARY
st.subheader("📌 Summary")
st.write(data["metadata"])

# 🔥 TABLE (only top 10)
st.subheader("🚨 Top Suspicious Transactions")
df = pd.DataFrame(data["node_audits"][:10])
st.dataframe(df)

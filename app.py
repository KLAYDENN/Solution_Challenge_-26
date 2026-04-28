import streamlit as st
import os
import json
from run import generate_demo_results

# Page config
st.set_page_config(page_title="ML Audit Dashboard", layout="wide")

# Title
st.title("📊 ML Audit Dashboard")

# File path
results_file = 'results/audit_results.json'

# Generate results if not present
if not os.path.exists(results_file):
    os.makedirs('results', exist_ok=True)
    results = generate_demo_results()
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)

# Load results
with open(results_file) as f:
    data = json.load(f)

# Display
st.subheader("📌 Audit Results")
st.json(data)

# Optional: Pretty view
if isinstance(data, dict):
    st.subheader("📈 Summary")
    for key, value in data.items():
        st.write(f"**{key}** : {value}")

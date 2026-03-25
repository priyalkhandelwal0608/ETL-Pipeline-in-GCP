import streamlit as st
import pandas as pd
import subprocess
import os

st.set_page_config(page_title="NYC Airbnb AI", layout="wide")

st.title("🏙️ NYC Airbnb AI Insights")

# Sidebar
st.sidebar.header("Pipeline Controls")
input_path = 'data/AB_NYC_2019.csv'

if not os.path.exists(input_path):
    st.sidebar.error(f"File not found: {input_path}")
else:
    st.sidebar.success("✅ Input Data Detected")

if st.sidebar.button("🚀 Run AI Pipeline"):
    with st.spinner("Processing 20 sample rows..."):
        # Run as a module so imports work correctly
        result = subprocess.run(["python", "-m", "src.pipeline"], capture_output=True, text=True)
        
        if result.returncode == 0:
            st.sidebar.success("Pipeline Finished!")
        else:
            st.sidebar.error("Pipeline Failed")
            st.sidebar.code(result.stderr)

# Content
out_file = 'data/processed_results.csv'
if os.path.exists(out_file):
    df = pd.read_csv(out_file)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Sampled", len(df))
        st.subheader("Data Preview")
        st.dataframe(df, use_container_width=True)
    
    with col2:
        st.subheader("Borough Distribution")
        st.bar_chart(df['neighbourhood_group'].value_counts())
else:
    st.info("Click 'Run AI Pipeline' to generate results.")
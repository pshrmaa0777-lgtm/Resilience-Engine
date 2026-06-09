import streamlit as st
import pandas as pd

st.title("Resilience Engine Pro")

uploaded_file = st.file_uploader
("Upload Excel file", type=["xlsx", "csv"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file, header=1)
    else:
        df = pd.read_excel(uploaded_file,header=1)

    st.write("Data Preview:",df)

    if st.button("Analyze All"):
        df['Score'] = df['Cash'] / df['Debt']

        def color_score(val):
            color = 'green' if val >= 1 else 'red'
            return f'background-color: {color}'

        styled_df = df.style.map(color_score, subset=['Score'])
        st.dataframe(styled_df)

        st.bar_chart(df.set_index('Company Name')['Score'])
       

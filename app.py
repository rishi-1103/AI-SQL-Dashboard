import streamlit as st
import pandas as pd
from agent.sql_agent import generate_sql, execute_sql

st.set_page_config(
    page_title="AI SQL Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI SQL Dashboard")
st.write("Ask questions about your retail sales database.")

question = st.text_input(
    "Ask a question",
    placeholder="Example: What is the total revenue?"
)

if st.button("Generate Answer"):

    if question:

        with st.spinner("Generating SQL..."):

            sql = generate_sql(question)

            st.subheader("Generated SQL")
            st.code(sql, language="sql")

            columns, rows = execute_sql(sql)

            if columns:

                df = pd.DataFrame(rows, columns=columns)

                st.subheader("Results")
                st.dataframe(df, use_container_width=True)

            else:
                st.success(rows)
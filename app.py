import streamlit as st
import asyncio
import pandas as pd

from graph import build_graph
from utils import reviews_to_dataframe
from memory import init_db, save_approval, fetch_all

st.set_page_config(layout="wide")

graph = build_graph()

# Init DB
asyncio.run(init_db())

# ---- NAV ----
tab1, tab2 = st.tabs([" Run Analysis", "📊 Analytics"])

# ---------------- RUN TAB ----------------
with tab1:
    st.title("Approval AI System")

    user_input = st.text_area("Enter marketing content")

    if st.button("Run"):

        result = asyncio.run(graph.ainvoke({"raw_input": user_input}))
        final = result["final"]

        st.success(f"Decision: {final.overall_decision}")

        df = reviews_to_dataframe(
            final.marketing,
            final.brand,
            final.compliance
        )

        st.dataframe(df)

        # Save to DB
        asyncio.run(save_approval(user_input, final.dict()))

# ---------------- ANALYTICS TAB ----------------
with tab2:
    st.title("📊 Approval Analytics")

    data = asyncio.run(fetch_all())

    if data:
        df = pd.DataFrame(data, columns=[
            "id", "input", "output", "decision", "timestamp"
        ])

        st.subheader("Decision Distribution")
        st.bar_chart(df["decision"].value_counts())

        st.subheader("Recent Approvals")
        st.dataframe(df.tail(10))
    else:
        st.info("No data yet")

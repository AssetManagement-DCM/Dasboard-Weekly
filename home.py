import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Asset Management", page_icon="👷‍♂️", layout="wide")
st.title("👷‍♂️ Asset Management Weekly Activity")

url = f"https://docs.google.com/spreadsheets/d/1UCyov9SZzwCzruemj7eUCFpc_ONV9du3fio00K_JHtI/edit?gid=467533562#gid=467533562"

@st.chace_data
def load_data():
    return pd.read_csv(url)

df = load_data()
st.dataframe(df)

st.sidebar.header("🔎 Filter Data")

weeks = sorted(df["Week"].unique())
week_filter = st.sidebar.multiselect("Pilih Week:", weeks, default=weeks)

bus = sorted(df["BU"].unique())
bu_filter = st.sidebar.multiselect("Pilih BU:", bus, default=bus)

# Apply filters
filtered_df = df[
    df["Week"].isin(week_filter) &
    df["BU"].isin(bu_filter)
]

# =========================
# PREVIEW DATA
# =========================
st.subheader("📋 Data Kegiatan (Filtered)")
st.dataframe(filtered_df, height=400)

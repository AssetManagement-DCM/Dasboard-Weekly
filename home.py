import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Asset Management", page_icon="👷‍♂️", layout="wide")
st.title("👷‍♂️ Asset Management Weekly Activity")

# Load data pakai sheet name
SHEET_ID = "1UCyov9SZzwCzruemj7eUCFpc_ONV9du3fio00K_JHtI"
SHEET_NAME = "Data"

url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

@st.cache_data
def load_data():
    return pd.read_csv(url)

df = load_data()
data = df[,3:6]
# ======================================
# FILTERS
# ======================================
st.sidebar.header("🔎 Filter Data")

weeks = sorted(data["Week"].dropna().unique())
week_filter = st.sidebar.multiselect("Pilih Week:", weeks, default=weeks)

bus = sorted(data["BU"].dropna().unique())
bu_filter = st.sidebar.multiselect("Pilih BU:", bus, default=bus)

filtered_df = data[
    data["Week"].isin(week_filter) &
    data["BU"].isin(bu_filter)
]

# ======================================
# DATA TABLE
# ======================================
st.subheader("📋 Data Kegiatan (Filtered)")
st.dataframe(filtered_df, height=400)

# ======================================
# SUMMARY
# ======================================
st.subheader("📊 Ringkasan")

col1, col2, col3 = st.columns(3)
col1.metric("Total Baris Data", len(filtered_df))
col2.metric("Total BU Terpilih", filtered_df["BU"].nunique())
col3.metric("Total Jenis Kegiatan", filtered_df["Kegiatan"].nunique())

# ======================================
# OVERVIEW PER KEGIATAN
# ======================================
st.subheader("📈 Overview Jumlah per Kegiatan")

sum_kegiatan = (
    filtered_df.groupby("Kegiatan")["Jumlah"]
    .sum()
    .reset_index()
    .sort_values("Jumlah", ascending=False)
)

st.dataframe(sum_kegiatan)

st.bar_chart(sum_kegiatan.set_index("Kegiatan"))

st.success("Dashboard tersambung menggunakan sheet name! 🚀")

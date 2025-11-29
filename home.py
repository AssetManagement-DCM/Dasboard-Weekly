import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Asset Management", page_icon="👷‍♂️", layout="wide")
st.title("👷‍♂️ Asset Management Weekly Activity")

# Load data dari Google Sheets
SHEET_ID = "1UCyov9SZzwCzruemj7eUCFpc_ONV9du3fio00K_JHtI"
GID = "467533562"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"

@st.cache_data
def load_data():
    return pd.read_csv(url)

df = load_data()

# =========================
# FILTER SECTION
# =========================
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

# =========================
# SUMMARY (Top Metrics)
# =========================
st.subheader("📊 Ringkasan")

col1, col2, col3 = st.columns(3)
col1.metric("Total Baris Data", len(filtered_df))
col2.metric("Total BU Terpilih", filtered_df["BU"].nunique())
col3.metric("Total Jenis Kegiatan", filtered_df["Kegiatan"].nunique())

# =========================
# OVERVIEW JUMLAH PER KEGIATAN
# =========================
st.subheader("📈 Overview Jumlah per Kegiatan")

sum_kegiatan = (
    filtered_df.groupby("Kegiatan")["Jumlah"]
    .sum()
    .reset_index()
    .sort_values("Jumlah", ascending=False)
)

st.dataframe(sum_kegiatan)

st.bar_chart(sum_kegiatan.set_index("Kegiatan"))

st.success("Dashboard tersambung ke Google Sheets terbaru! 🚀")

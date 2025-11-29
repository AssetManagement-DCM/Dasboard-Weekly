import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Safety", page_icon="🛡️", layout="wide")

st.title("🛡️ Safety Activity Dashboard")
st.write("Data Realtime dari Google Sheets")

# Load data dari Google Sheets
SHEET_ID = "1R1UYHVGMFNNWaalVO5RQwVJbMPYigr23Pl6R9A4-VrE"
GID = "944388157"  # sesuai sheet yang kamu kirim
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"

@st.cache_data
def load_data():
    return pd.read_csv(url)

df = load_data()

# Preview data
st.subheader("📋 Data Kegiatan")
st.dataframe(df)

# Summary Section
st.subheader("📊 Ringkasan")
col1, col2, col3 = st.columns(3)

col1.metric("Jumlah Kegiatan", len(df))
if "BU" in df.columns:
    col2.metric("Jumlah BU", df["BU"].nunique())
else:
    col2.metric("Jumlah BU", "-")

if "Departemen" in df.columns:
    col3.metric("Jumlah Departemen", df["Departemen"].nunique())
else:
    col3.metric("Jumlah Departemen", "-")

st.success("Dashboard tersambung ke Google Sheets! 🚀")

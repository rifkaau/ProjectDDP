# app.py
import streamlit as st
from dashboard import show_dashboard
from tambah_kendaraan import add_vehicle
from penjualan_kendaraan import process_sale
from keuntungan_kendaraan import calculate_profit
from grafik_kendaraan import show_graph

# Menambahkan CSS untuk background
st.markdown(
    """
    <style>
    body {
        background-color: #F5F5DC;
    }
    .stApp {
        background-color: #F5F5DC;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Inisialisasi data kendaraan
if 'vehicles' not in st.session_state:
    st.session_state.vehicles = []
    
# Navbar untuk memilih opsi
st.sidebar.image("sidebar.png", caption="", use_container_width=True)
menu = ["Dashboard", "🆕 Tambah Kendaraan", "💰 Proses Penjualan", "📈 Hitung Keuntungan", "📊 Tampilkan Grafik"]
choice = st.sidebar.selectbox("Pilih Opsi", menu, help="Pilih fitur yang ingin Anda gunakan.")

if choice == "Dashboard":
    show_dashboard()
elif choice == "🆕 Tambah Kendaraan":
    add_vehicle()
elif choice == "💰 Proses Penjualan":
    process_sale()
elif choice == "📈 Hitung Keuntungan":
    calculate_profit()
elif choice == "📊 Tampilkan Grafik":
    show_graph()
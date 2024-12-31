# tambah_kendaraan.py
import streamlit as st
import pandas as pd
from vehicle import Vehicle

def add_vehicle():
    st.markdown('<h2 class="header">Tambah Kendaraan</h2>', unsafe_allow_html=True)
    
    # Menambahkan form input untuk jumlah unit
    with st.form(key='vehicle_form'):
        make = st.text_input("Merek")
        model = st.text_input("Model")
        year = st.number_input("Tahun", min_value=1900, max_value=2024)
        purchase_price = st.number_input("Harga Beli per Unit", min_value=0)  # Harga beli per unit
        units = st.number_input("Jumlah Unit", min_value=1, step=1)  # Input untuk jumlah unit
        submit_button = st.form_submit_button("Tambah Kendaraan")

        if submit_button:
            # Menyimpan kendaraan dan harga per unit
            vehicle = Vehicle(make, model, year, purchase_price)
            vehicle.units = units  # Menyimpan jumlah unit
            vehicle.total_price = purchase_price * units  # Menghitung harga total per unit * jumlah unit
            st.session_state.vehicles.append(vehicle)
            st.success("✅ Kendaraan berhasil ditambahkan!")

    if st.session_state.vehicles:
        st.subheader("Daftar Kendaraan")
        
        # Membuat data untuk tabel
        data = []
        for v in st.session_state.vehicles:
            data.append({
                'Merek': v.make,
                'Model': v.model,
                'Tahun': v.year,
                'Harga Beli per Unit': v.purchase_price,  # Menampilkan harga per unit
                'Jumlah Unit': v.units,
                'Harga Total': v.total_price  # Menampilkan harga total yang sudah dihitung
            })

        # Menampilkan tabel menggunakan st.dataframe
        df = pd.DataFrame(data)
        
        # Menampilkan data dengan ukuran yang lebih responsif
        st.dataframe(df, use_container_width=True)
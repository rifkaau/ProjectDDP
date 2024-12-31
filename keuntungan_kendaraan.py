# keuntungan_kendaraan.py
import streamlit as st
import pandas as pd
from vehicle import Vehicle

def calculate_profit():
    st.markdown('<h2 class="header">Hitung Keuntungan Penjualan</h2>', unsafe_allow_html=True)
    
    # Menampilkan tabel keuntungan
    if 'sales' in st.session_state and st.session_state.sales:
        st.subheader("Tabel Keuntungan Penjualan")
        
        # Membuat DataFrame untuk keuntungan
        data = []
        for sale in st.session_state.sales:
            profit = sale['Harga Jual'] - sale['Harga Beli per Unit']  # Menghitung keuntungan
            data.append({
                'Merek': sale['Merek'],
                'Model': sale['Model'],
                'Tahun': sale['Tahun'],
                'Jumlah Unit': sale['Jumlah Unit'],
                'Harga Beli per Unit': sale['Harga Beli per Unit'],
                'Harga Jual': sale['Harga Jual'],
                'Keuntungan penjualan per unit': profit
            })

        df_profit = pd.DataFrame(data)
        
        # Menampilkan data dengan ukuran yang lebih responsif
        st.dataframe(df_profit, use_container_width=True)

    else:
        st.write("🚫 Tidak ada kendaraan yang tersedia untuk menghitung keuntungan.")
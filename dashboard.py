import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def show_dashboard():
    # Judul aplikasi
    st.markdown('<h2 class="title">🚗Aplikasi Penjualan Kendaraan Mobil</h2>', unsafe_allow_html=True)
    st.write("----------------------------------------")
    
    # Daftar Anggota Kelompok 1
    st.subheader("Daftar Kelompok 1")
    st.image("kelompok.jpg", caption="", use_container_width=True )
    st.image("dashboard.jpg", caption="", use_container_width=True )
    
    # Deskripsi
    st.write("Kami membuat aplikasi bertemakan “Penjualan Kendaraan” yang bertujuan untuk mengetahui keuntungan dari perolehan menjual kendaraan. Aplikasi ini dapat memudahkan perusahaan untuk menghitung keuntungan dengan mudah dan cepat. Kami membuat project aplikasi ini juga untuk memenuhi nilai project uas dalam mata kuliah DDP (Dasar-Dasar Pemograman) .")

    # Menampilkan Data Penjualan
    st.subheader("Data Penjualan")
    
    if 'sales' in st.session_state and st.session_state.sales:
        # Membuat DataFrame untuk keuntungan
        data = []
        for sale in st.session_state.sales:
            # Menghitung keuntungan per unit
            profit = sale['Harga Jual'] - sale['Harga Beli per Unit']
            data.append({
                'Merek': sale['Merek'],
                'Model': sale['Model'],
                'Tahun': sale['Tahun'],
                'Jumlah Unit': sale['Jumlah Unit'],
                'Harga Beli per Unit': sale['Harga Beli per Unit'],
                'Harga Jual': sale['Harga Jual'],
                'Keuntungan Penjualan per Unit': profit
            })

        # Membuat DataFrame dari data
        df_profit = pd.DataFrame(data)
        
        # Menampilkan data dengan ukuran yang lebih responsif
        st.dataframe(df_profit, use_container_width=True)
    else:
        st.write("🚫 Tidak ada data yang tersedia untuk ditampilkan.")

    # Menampilkan Grafik Keuntungan Penjualan
    st.subheader("Grafik Keuntungan Penjualan Kendaraan")
    
    if 'sales' in st.session_state and st.session_state.sales:
        # Mengambil keuntungan dan nama kendaraan
        profits = [v['Harga Jual'] - v['Harga Beli per Unit'] for v in st.session_state.sales]
        vehicle_names = [f"{v['Merek']} {v['Model']} ({v['Tahun']})" for v in st.session_state.sales]
        
        if profits:  # Jika ada keuntungan
            # Membuat grafik batang horizontal
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.barh(vehicle_names, profits, color='blue')
            ax.set_xlabel('Keuntungan ($)')
            ax.set_ylabel('Kendaraan')
            ax.set_title('Keuntungan dari Penjualan Kendaraan')

            # Menambahkan angka pada batang
            for index, value in enumerate(profits):
                ax.text(value, index, f'$ {value:,.0f}', va='center', color='white')

            st.pyplot(fig)  # Menampilkan grafik di Streamlit
            
            # Menampilkan Tabel Keuntungan
            st.subheader("Tabel Keuntungan Penjualan")
            df_profit = pd.DataFrame({
                'Kendaraan': vehicle_names,
                'Keuntungan per Unit': profits
            })
            st.dataframe(df_profit, use_container_width=True)
        else:
            st.write("🚫 Tidak ada keuntungan yang tersedia untuk ditampilkan.")
    else:
        st.write("🚫 Tidak ada keuntungan yang tersedia untuk ditampilkan.")
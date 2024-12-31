# grafik_keuntungan.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def show_graph():
    st.header("Grafik Keuntungan Penjualan Kendaraan")
    
    if 'sales' in st.session_state and st.session_state.sales:
        profits = [v['Harga Jual'] - v['Harga Beli per Unit'] for v in st.session_state.sales]
        vehicle_names = [f"{v['Merek']} {v['Model']} ({v['Tahun']})" for v in st.session_state.sales]
        
        if profits:
            # Membuat grafik batang
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.barh(vehicle_names, profits, color='blue')
            ax.set_xlabel('Keuntungan ($)')
            ax.set_ylabel('Kendaraan')
            ax.set_title('Keuntungan dari Penjualan Kendaraan')

            for index, value in enumerate(profits):
                ax.text(value, index, f'$ {value:,.0f}', va='center', color='white')

            st.pyplot(fig)  # Menampilkan grafik di Streamlit
            
            # Menampilkan Tabel Keuntungan
            st.subheader("Tabel Keuntungan Penjualan")
            df_profit = pd.DataFrame({
                'Kendaraan': vehicle_names,
                'Keuntungan per unit': profits
            })
            st.dataframe(df_profit, use_container_width=True)
        else:
            st.write("🚫 Tidak ada keuntungan yang tersedia untuk ditampilkan.")
    else:
        st.write("🚫 Tidak ada keuntungan yang tersedia untuk ditampilkan.")
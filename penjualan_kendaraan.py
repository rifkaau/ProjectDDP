# penjualan_kendaraan.py
import streamlit as st
import pandas as pd
from vehicle import Vehicle

def process_sale():
    st.markdown('<h2 class="header">Proses Penjualan Kendaraan</h2>', unsafe_allow_html=True)
    
    if st.session_state.vehicles:
        selected_vehicle = st.selectbox("Pilih Kendaraan", [v.description() for v in st.session_state.vehicles])
        selling_price = st.number_input("Harga Jual", min_value=0)

        if st.button("Proses Penjualan"):
            # Mencari kendaraan yang dipilih
            vehicle = next(v for v in st.session_state.vehicles if v.description() == selected_vehicle)
            vehicle.set_selling_price(selling_price)
            
            # Menyimpan data penjualan dalam session_state
            sale_data = {
                'Merek': vehicle.make,
                'Model': vehicle.model,
                'Tahun': vehicle.year,
                'Jumlah Unit': vehicle.units,
                'Harga Beli per Unit': vehicle.purchase_price,
                'Harga Jual': selling_price,
                'Harga Total': vehicle.purchase_price * vehicle.units  # Harga Total
            }
            
            # Menyimpan data penjualan dalam session_state
            if 'sales' not in st.session_state:
                st.session_state.sales = []
            st.session_state.sales.append(sale_data)
            
            # Menghapus kendaraan yang terjual dari daftar kendaraan
            st.session_state.vehicles.remove(vehicle)
            
            st.success(f"✅ Kendaraan {selected_vehicle} berhasil dijual dengan harga {selling_price}.")
    
    else:
        st.write("🚫 Tidak ada kendaraan yang tersedia untuk dijual.")
    
    # Menampilkan tabel penjualan
    if 'sales' in st.session_state and st.session_state.sales:
        st.subheader("Tabel Penjualan Kendaraan")
        
        # Membuat DataFrame untuk penjualan
        df_sales = pd.DataFrame(st.session_state.sales)
        
        # Menampilkan data dengan ukuran yang lebih responsif
        st.dataframe(df_sales, use_container_width=True)
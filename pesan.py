import streamlit as st

# Membuat list menu
menu_items = {
    "mie tante": 7000,
    "mie telor": 10000,
    "mie dok-dok": 11000,
    "mie dok-dok ayam": 12000,
    "mie dok-dok sosis": 12000,
    "mie dok-dok baso": 12000,
    "mie dok-dok spesial": 14000,
    "mie spesial": 11000,
    "mie spesial ayam": 12000,
    "mie spesial sosis": 12000,
    "mie spesial baso": 12000,
    "omlet": 10000,
    "nasi omlet": 13000,
    "nasi gila": 14000,
    "nasi omlet ayam": 14000,
    "nasi omlet sosis": 14000,
    "nasi omlet baso": 14000,
    "nasi omlet spesial": 15000,
    "nasi sarden": 8000,
    "nasi sarden telor": 11000,
    "nasi telor": 8000,
    "nasi telor ayam": 10000,
    "nasi telor sosis": 10000,
    "nasi telor baso": 10000,
    "nasi goreng": 10000,
    "nasi goreng ayam": 11000,
    "nasi goreng sosis": 11000,
    "nasi goreng baso": 11000,
    "nasi goreng spesial": 13000,
    "magelangan": 11000,
    "magelangan ayam": 12000,
    "magelangan sosis": 12000,
    "magelangan baso": 12000,
    "magelangan spesial": 14000,
    "nasi orak-arik": 9000,
    "nasi orak-arik ayam": 10000,
    "nasi orak-arik sosis": 10000,
    "nasi orak-arik baso": 10000,
    "nasi orak-arik gorengan": 10000,
    "nasi orak-arik spesial": 13000,
    "nasi ayam bali": 11000,
    "nasi ayam bali sosis": 12000,
    "nasi ayam bali baso": 12000,
    "nasi ayam bali spesial": 14000,
    "es teh": 3000,
    "es jeruk": 4000,
    "es campur": 6000
}


# Membuat halaman untuk daftar menu
def menu_page():
    st.header("Pilihan Menu Makanan & Minuman:")
    for item, price in menu_items.items():
        st.write(f"{item.capitalize()}: Rp{price}")

# Membuat halaman untuk pemesanan
def order_page():
    st.header("Pemesanan")
    customer_name = st.text_input("Nama Pemesan:")
    table_number = st.text_input("Nomor Meja:")
    order_date = st.date_input("Tanggal Pesanan:")
    st.write("Pilihan Rincian Pemesanan:")
    selected_items = st.multiselect("Pilih menu yang dipesan:", list(menu_items.keys()))
    order_summary = []
    for item in selected_items:
        price = menu_items[item]
        order_summary.append(f"{item}: Rp{price}")
    st.write(order_summary)
    total_price = sum(menu_items[item] for item in selected_items)
    st.write(f"Total Harga: Rp{total_price}")
    payment_amount = st.number_input("Jumlah Pembayaran:")
    if payment_amount >= total_price:
        change_amount = payment_amount - total_price
        st.write(f"Kembalian: Rp{change_amount}")
    else:
        st.write("Jumlah pembayaran tidak mencukupi.")

# Membuat halaman utama
def main():
    st.title("BURJO MEISYA SEMARANG")
    menu_options = ["Daftar Menu", "Pemesanan"]
    choice = st.sidebar.selectbox("Pilih Menu:", menu_options)
    if choice == "Daftar Menu":
        menu_page()
    elif choice == "Pemesanan":
        order_page()

if __name__ == "__main__":
    main()

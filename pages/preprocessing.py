import streamlit as st
import pandas as pd

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Preprocessing",
    page_icon="🧹",
    layout="wide"
)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    _, center, _ = st.columns([1,3,1])

    with center:
        st.image(
            "assets/logo.jpg",
            width=170
        )

    st.markdown("""
    <h2 style='text-align:center'>
    🤖 MACHINE LEARNING
    </h2>

    <p style='text-align:center'>
    Analisis Sentimen Tokopedia
    </p>
    """, unsafe_allow_html=True)

    st.divider()

# =====================================
# CSS
# =====================================

st.markdown("""
<style>

[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #0f172a,
        #1e293b
    );
}

[data-testid="stSidebar"] *{
    color:white;
}

.header-box{
    background:linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
    );
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="header-box">

<h1>🧹 PREPROCESSING DATA</h1>

<p>
Tahapan Pembersihan Data Ulasan Tokopedia
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# DATA PREPROCESSING
# =====================================

data = {
    "Data Awal": [
        "Barang bagus banget dan pengiriman cepat",
        "Kualitas kaos sangat baik dan nyaman dipakai",
        "Pengiriman lambat dan barang kurang sesuai",
        "Bahan kaos tebal dan jahitan rapi",
        "Ukuran tidak sesuai dengan deskripsi",
        "Produk original dan harga terjangkau",
        "Warna kaos bagus sesuai gambar",
        "Pelayanan toko sangat memuaskan",
        "Barang datang terlambat dan kemasan rusak",
        "Bahan nyaman dipakai sehari hari",
        "Kualitas produk buruk dan mudah rusak",
        "Pengiriman cepat dan respon penjual baik",
        "Produk sesuai ekspektasi saya",
        "Ukuran pas dan bahan berkualitas",
        "Tidak rekomendasi karena kualitas kurang baik"
    ],

    "Case Folding": [
        "barang bagus banget dan pengiriman cepat",
        "kualitas kaos sangat baik dan nyaman dipakai",
        "pengiriman lambat dan barang kurang sesuai",
        "bahan kaos tebal dan jahitan rapi",
        "ukuran tidak sesuai dengan deskripsi",
        "produk original dan harga terjangkau",
        "warna kaos bagus sesuai gambar",
        "pelayanan toko sangat memuaskan",
        "barang datang terlambat dan kemasan rusak",
        "bahan nyaman dipakai sehari hari",
        "kualitas produk buruk dan mudah rusak",
        "pengiriman cepat dan respon penjual baik",
        "produk sesuai ekspektasi saya",
        "ukuran pas dan bahan berkualitas",
        "tidak rekomendasi karena kualitas kurang baik"
    ],

    "Cleaning": [
        "barang bagus banget dan pengiriman cepat",
        "kualitas kaos sangat baik dan nyaman dipakai",
        "pengiriman lambat dan barang kurang sesuai",
        "bahan kaos tebal dan jahitan rapi",
        "ukuran tidak sesuai dengan deskripsi",
        "produk original dan harga terjangkau",
        "warna kaos bagus sesuai gambar",
        "pelayanan toko sangat memuaskan",
        "barang datang terlambat dan kemasan rusak",
        "bahan nyaman dipakai sehari hari",
        "kualitas produk buruk dan mudah rusak",
        "pengiriman cepat dan respon penjual baik",
        "produk sesuai ekspektasi saya",
        "ukuran pas dan bahan berkualitas",
        "tidak rekomendasi karena kualitas kurang baik"
    ],

    "Tokenizing": [
        "['barang','bagus','banget','pengiriman','cepat']",
        "['kualitas','kaos','baik','nyaman','dipakai']",
        "['pengiriman','lambat','barang','kurang','sesuai']",
        "['bahan','kaos','tebal','jahitan','rapi']",
        "['ukuran','tidak','sesuai','deskripsi']",
        "['produk','original','harga','terjangkau']",
        "['warna','kaos','bagus','sesuai','gambar']",
        "['pelayanan','toko','sangat','memuaskan']",
        "['barang','datang','terlambat','kemasan','rusak']",
        "['bahan','nyaman','dipakai','sehari','hari']",
        "['kualitas','produk','buruk','mudah','rusak']",
        "['pengiriman','cepat','respon','penjual','baik']",
        "['produk','sesuai','ekspektasi']",
        "['ukuran','pas','bahan','berkualitas']",
        "['tidak','rekomendasi','kualitas','kurang','baik']"
    ],

    "Stopword Removal": [
        "barang bagus banget pengiriman cepat",
        "kualitas kaos baik nyaman dipakai",
        "pengiriman lambat barang kurang sesuai",
        "bahan kaos tebal jahitan rapi",
        "ukuran sesuai deskripsi",
        "produk original harga terjangkau",
        "warna kaos bagus sesuai gambar",
        "pelayanan toko memuaskan",
        "barang datang terlambat kemasan rusak",
        "bahan nyaman dipakai sehari hari",
        "kualitas produk buruk mudah rusak",
        "pengiriman cepat respon penjual baik",
        "produk sesuai ekspektasi",
        "ukuran pas bahan berkualitas",
        "rekomendasi kualitas kurang baik"
    ],

    "Stemming": [
        "barang bagus banget kirim cepat",
        "kualitas kaos baik nyaman pakai",
        "kirim lambat barang kurang sesuai",
        "bahan kaos tebal jahit rapi",
        "ukur sesuai deskripsi",
        "produk original harga jangkau",
        "warna kaos bagus sesuai gambar",
        "layan toko puas",
        "barang datang lambat kemas rusak",
        "bahan nyaman pakai hari",
        "kualitas produk buruk mudah rusak",
        "kirim cepat respon jual baik",
        "produk sesuai ekspektasi",
        "ukur pas bahan kualitas",
        "rekomendasi kualitas kurang baik"
    ]
}

df = pd.DataFrame(data)

# =====================================
# TABEL PREPROCESSING
# =====================================

st.subheader("📋 Hasil Preprocessing")

st.dataframe(
    df,
    use_container_width=True,
    height=550
)

# =====================================
# INFO
# =====================================

st.success(
    "✅ Ini adalah dataset yang sudah berhasil di Preprocessing dilakukan di google colab link nya : https://colab.research.google.com/drive/1LaSmUl-bUs5DqHlLdqD9_MNlyXVVO1P_?usp=sharing."
)
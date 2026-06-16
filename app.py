import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Analisis Sentimen Tokopedia",
    page_icon="📊",
    layout="wide"
)

# =====================================
# CSS
# =====================================

st.markdown("""
<style>

/* Sidebar */
[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0f172a,#1e293b);
}

/* Semua teks sidebar putih */
[data-testid="stSidebar"] *{
    color:white;
}

/* Main */
.main{
    background-color:#f5f7fa;
}

/* Card */
.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
    text-align:center;
}

/* Header */
.header{
    background:linear-gradient(90deg,#00b14f,#00d563);
    padding:35px;
    border-radius:20px;
    text-align:center;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.markdown("<br>", unsafe_allow_html=True)

    c1,c2,c3 = st.columns([1,3,1])

    with c2:
        st.image(
            "assets/logo.jpg",
            width=180
        )

    st.markdown("""
    <h2 style='text-align:center; color:white;'>
    🤖 Pembelajaran Mesin
    </h2>

    <p style='text-align:center; color:white;'>
    Analisis Sentimen Tokopedia
    </p>
    """, unsafe_allow_html=True)

    st.divider()

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="header">

<h1>📊 ANALISIS SENTIMEN ULASAN TOKOPEDIA</h1>

<h3>Kaos Loco Polo Cartiera Scuba 280 GSM</h3>

<p>
Perbandingan Algoritma Naive Bayes dan Support Vector Machine
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# KPI
# =====================================

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric("📄 Total Ulasan", "155")

with k2:
    st.metric("😊 Positif", "121")

with k3:
    st.metric("😡 Negatif", "34")

with k4:
    st.metric("🏆 Akurasi Terbaik", "92.50%")

st.divider()

# =====================================
# PRODUK + INFORMASI
# =====================================

left,right = st.columns([3,2])

with left:

    st.image(
        "assets/polo_cartiera.png",
        use_container_width=True
    )

with right:

    st.markdown("""
    # 📌 Informasi Penelitian

    ### Objek Penelitian

    Ulasan pelanggan terhadap produk:

    **Kaos Loco Polo Cartiera Scuba 280 GSM**

    pada marketplace Tokopedia.

    ### 🎯 Tujuan

    Mengklasifikasikan sentimen menjadi:

    - 😊 Positif
    - 😡 Negatif

    ### ⚙️ Algoritma

    - Naive Bayes
    - Support Vector Machine (SVM)

    ### 📊 Fitur Sistem

    - Preprocessing Data
    - Klasifikasi Sentimen
    - Confusion Matrix
    - Evaluasi Model
    - Perbandingan Algoritma
    """)

st.divider()

# =====================================
# PERFORMA MODEL
# =====================================

st.subheader("🚀 Performa Model")

c1,c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="card">
        <h3>🔵 Naive Bayes</h3>
        <h1>87.50%</h1>
        <p>Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="card">
        <h3>🟢 Support Vector Machine</h3>
        <h1>92.50%</h1>
        <p>Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

st.success(
    "🏆 Algoritma Terbaik : Support Vector Machine (SVM)"
)

st.divider()

# =====================================
# FOOTER
# =====================================

st.markdown("""
<center>

<hr>

<h3>🤖 MACHINE LEARNING</h3>

<p>
Analisis Sentimen Ulasan Produk Tokopedia
</p>

<p>
Dibuat menggunakan Python • Streamlit • Scikit-Learn
</p>

</center>
""", unsafe_allow_html=True)
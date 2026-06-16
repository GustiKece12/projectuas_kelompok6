import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sentimen",
    page_icon="😊",
    layout="wide"
)

with st.sidebar:

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.image(
            "assets/logo.jpg",
            width=180
        )

    st.markdown("""
    <h3 style='text-align:center'>
    MACHINE LEARNING
    </h3>

    <p style='text-align:center'>
    Analisis Sentimen Tokopedia
    </p>
    """, unsafe_allow_html=True)

    st.divider()

st.markdown("""
<style>

[data-testid="stSidebar"]{
background:linear-gradient(180deg,#0f172a,#1e293b);
}

[data-testid="stSidebar"] *{
color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:linear-gradient(90deg,#10b981,#34d399);
padding:25px;
border-radius:20px;
text-align:center;
color:white;
">

<h1>😊 DATA SENTIMEN</h1>
<p>Hasil Klasifikasi Sentimen Positif dan Negatif</p>

</div>
""", unsafe_allow_html=True)

st.write("")

df = pd.DataFrame({
    "Ulasan":[
        "Barang bagus",
        "Kain tipis",
        "Pengiriman cepat",
        "Kualitas mantap",
        "Jahitan kurang rapi"
    ],
    "Sentimen":[
        "Positif",
        "Negatif",
        "Positif",
        "Positif",
        "Negatif"
    ]
})

st.dataframe(df,use_container_width=True)

st.divider()

st.divider()

st.subheader("📊 Analisis Sentimen")

col1, col2 = st.columns(2)

# Pie Chart
with col1:

    st.markdown("### Distribusi Sentimen")

    fig, ax = plt.subplots(figsize=(5,5))

    ax.pie(
        [121,34],
        labels=["Positif","Negatif"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Distribusi Sentimen")

    st.pyplot(fig)

# WordCloud
with col2:

    st.markdown("### WordCloud Ulasan")

    st.image(
        "assets/wordcloud.png",
        use_container_width=True
    )

st.pyplot(fig)
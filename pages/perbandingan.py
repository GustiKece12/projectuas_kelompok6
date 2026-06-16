import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Perbandingan",
    page_icon="⚖️",
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
background:linear-gradient(90deg,#8b5cf6,#a855f7);
padding:25px;
border-radius:20px;
color:white;
text-align:center;
">

<h1>⚖️ PERBANDINGAN ALGORITMA</h1>

<p>Naive Bayes vs Support Vector Machine</p>

</div>
""", unsafe_allow_html=True)

st.write("")

metric = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score"
]

nb = [87.50,88.24,85.71,86.96]
svm = [92.50,93.10,91.67,92.38]

df = pd.DataFrame({
    "Metric":metric,
    "Naive Bayes":nb,
    "SVM":svm
})

st.dataframe(df,use_container_width=True)

st.divider()

fig, ax = plt.subplots(figsize=(8,5))

x = range(len(metric))

ax.bar(
    [i-0.2 for i in x],
    nb,
    width=0.4,
    label="Naive Bayes"
)

ax.bar(
    [i+0.2 for i in x],
    svm,
    width=0.4,
    label="SVM"
)

ax.set_xticks(list(x))
ax.set_xticklabels(metric)

ax.legend()

st.pyplot(fig)

st.success("🏆 SVM unggul pada seluruh metrik evaluasi")
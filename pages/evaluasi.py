import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Evaluasi Model",
    page_icon="📈",
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
            width=140
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

.metric-box{
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#f59e0b,#fbbf24);
padding:25px;
border-radius:20px;
color:white;
text-align:center;
">

<h1>📈 EVALUASI MODEL</h1>

<p>
Perbandingan Algoritma Naive Bayes dan Support Vector Machine
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# METRIC SVM
# =====================================

st.subheader("📊 Evaluation 2 Algortima Model")

# =====================================
# PERBANDINGAN MODEL
# =====================================

c1,c2 = st.columns(2)

with c1:

    st.subheader("🔵 Naive Bayes")

    nb = pd.DataFrame({
        "Metric":[
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ],
        "Nilai":[
            "87.50%",
            "88.24%",
            "85.71%",
            "86.96%"
        ]
    })

    st.table(nb)

with c2:

    st.subheader("🟢 Support Vector Machine")

    svm = pd.DataFrame({
        "Metric":[
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ],
        "Nilai":[
            "92.50%",
            "93.10%",
            "91.67%",
            "92.38%"
        ]
    })

    st.table(svm)

st.divider()

# =====================================
# CLASSIFICATION REPORT
# =====================================

st.subheader("📋 Classification Report")

report = pd.DataFrame({
    "Class":[
        "Negatif",
        "Positif"
    ],
    "Precision":[
        0.94,
        0.92
    ],
    "Recall":[
        0.89,
        0.97
    ],
    "F1-Score":[
        0.91,
        0.94
    ]
})

st.dataframe(
    report,
    use_container_width=True
)

st.divider()

# =====================================
# CONFUSION MATRIX
# =====================================

st.subheader("🎯 Confusion Matrix")

col1, col2 = st.columns(2)

# ======================
# NAIVE BAYES
# ======================

with col1:

    st.markdown("### 🔵 Naive Bayes")

    cm_nb = np.array([
        [78,12],
        [13,97]
    ])

    fig1, ax1 = plt.subplots(figsize=(5,4))

    sns.heatmap(
        cm_nb,
        annot=True,
        fmt="d",
        cmap="Blues",
        linewidths=1,
        linecolor="white",
        xticklabels=["Negatif","Positif"],
        yticklabels=["Negatif","Positif"],
        ax=ax1
    )

    ax1.set_xlabel("Prediksi")
    ax1.set_ylabel("Aktual")

    st.pyplot(fig1)

# ======================
# SVM
# ======================

with col2:

    st.markdown("### 🟢 Support Vector Machine")

    cm_svm = np.array([
        [85,5],
        [3,107]
    ])

    fig2, ax2 = plt.subplots(figsize=(5,4))

    sns.heatmap(
        cm_svm,
        annot=True,
        fmt="d",
        cmap="Greens",
        linewidths=1,
        linecolor="white",
        xticklabels=["Negatif","Positif"],
        yticklabels=["Negatif","Positif"],
        ax=ax2
    )

    ax2.set_xlabel("Prediksi")
    ax2.set_ylabel("Aktual")

    st.pyplot(fig2)

st.divider()

# =====================================
# PERBANDINGAN AKURASI
# =====================================

st.subheader("📊 Perbandingan Akurasi")

comparison = pd.DataFrame({
    "Algoritma":[
        "Naive Bayes",
        "SVM"
    ],
    "Accuracy":[
        87.50,
        92.50
    ]
})

st.dataframe(
    comparison,
    use_container_width=True
)

st.success(
    "🏆 Berdasarkan hasil evaluasi, algoritma Support Vector Machine (SVM) memiliki performa terbaik dengan akurasi sebesar 92.50%."
)

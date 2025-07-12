import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Simulasi Antrian M/M/1", layout="wide")

# Header dengan styling HTML
st.markdown("""
<style>
.big-font {
    font-size: 30px !important;
    color: #4B8BBE;
    font-weight: bold;
}
.sub-font {
    font-size: 18px !important;
    color: #444444;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">📊 Simulasi Model Antrian M/M/1</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-font">Masukkan parameter untuk melihat performa sistem antrian berdasarkan teori M/M/1.</p>', unsafe_allow_html=True)

# Sidebar Input
st.sidebar.header("🔧 Parameter Input")
lambda_val = st.sidebar.slider("Rata-rata kedatangan (λ)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
mu_val = st.sidebar.slider("Rata-rata layanan (μ)", min_value=0.1, max_value=10.0, value=3.0, step=0.1)

# Layout hasil dan visual
col1, col2 = st.columns(2)

if lambda_val >= mu_val:
    st.error("⚠️ Sistem tidak stabil (λ ≥ μ). Pastikan nilai λ < μ agar sistem stabil.")
else:
    # Perhitungan
    rho = lambda_val / mu_val
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu_val - lambda_val)
    Wq = rho / (mu_val - lambda_val)

    with col1:
        st.subheader("📈 Hasil Perhitungan")
        st.metric(label="ρ (Utilisasi)", value=f"{rho:.2f}")
        st.metric(label="L (Pelanggan dalam sistem)", value=f"{L:.2f}")
        st.metric(label="Lq (Pelanggan dalam antrian)", value=f"{Lq:.2f}")
        st.metric(label="W (Waktu dalam sistem)", value=f"{W:.2f}")
        st.metric(label="Wq (Waktu dalam antrian)", value=f"{Wq:.2f}")

    with col2:
        st.subheader("📉 Visualisasi Probabilitas Pelanggan")
        fig, ax = plt.subplots(figsize=(6, 4))
        n = np.arange(0, 20)
        p_n = (1 - rho) * rho**n
        ax.bar(n, p_n, color="#4B8BBE", edgecolor='black')
        ax.set_xlabel("Jumlah Pelanggan dalam Sistem")
        ax.set_ylabel("Probabilitas")
        ax.set_title("Distribusi Jumlah Pelanggan")
        st.pyplot(fig)

    st.success("✅ Sistem stabil! Simulasi berhasil ditampilkan.")

# Footer
st.markdown("---")
st.markdown("Dibuat dengan ❤️ oleh As Septian | Model: **M/M/1 Queue** | Powered by Streamlit")

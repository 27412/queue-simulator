import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi tampilan
st.set_page_config(page_title="Simulasi Antrian M/M/1", layout="wide")

# Header
st.markdown("""
<style>
.title { font-size: 32px; font-weight: bold; color: #4B8BBE; }
.subtitle { font-size: 18px; color: #333; margin-top: -10px; }
.footer { font-size: 14px; color: #999; text-align: center; margin-top: 40px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📊 Simulasi Model Antrian M/M/1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Model antrian dengan asumsi kedatangan dan pelayanan mengikuti distribusi Poisson</div>', unsafe_allow_html=True)
st.write("")

# Sidebar untuk input parameter
st.sidebar.header("🔧 Input Parameter Antrian")
lambda_val = st.sidebar.slider(
    "λ (Rata-rata kedatangan pelanggan per satuan waktu)", min_value=0.1, max_value=10.0, value=2.0, step=0.1,
    help="Jumlah rata-rata pelanggan yang datang per satuan waktu (misal: per menit)"
)
mu_val = st.sidebar.slider(
    "μ (Rata-rata pelayanan per satuan waktu)", min_value=0.1, max_value=10.0, value=3.0, step=0.1,
    help="Jumlah rata-rata pelanggan yang bisa dilayani per satuan waktu"
)

st.sidebar.caption("📌 Catatan: Pastikan λ < μ agar sistem antrian stabil.")

# Validasi kestabilan sistem
if lambda_val >= mu_val:
    st.error("⚠️ Sistem TIDAK stabil karena λ ≥ μ. Sistem akan terus menumpuk pelanggan.")
else:
    # Hitung parameter M/M/1
    rho = lambda_val / mu_val
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu_val - lambda_val)
    Wq = rho / (mu_val - lambda_val)

    # Tampilkan metrik hasil
    col1, col2, col3 = st.columns([1, 1, 1])
    col1.metric("ρ (Utilisasi Server)", f"{rho:.2f}", help="Persentase waktu server sibuk")
    col2.metric("L (Pelanggan dlm Sistem)", f"{L:.2f}", help="Jumlah rata-rata pelanggan di sistem (antri + dilayani)")
    col3.metric("Lq (Pelanggan Antri)", f"{Lq:.2f}", help="Jumlah rata-rata pelanggan yang sedang mengantri")

    col4, col5 = st.columns([1, 1])
    col4.metric("W (Waktu dlm Sistem)", f"{W:.2f}", help="Rata-rata waktu pelanggan berada di sistem (antri + layanan)")
    col5.metric("Wq (Waktu Antri)", f"{Wq:.2f}", help="Rata-rata waktu pelanggan hanya saat mengantri")

    # Visualisasi distribusi jumlah pelanggan
    st.markdown("### 📉 Visualisasi Distribusi Jumlah Pelanggan dalam Sistem")
    fig, ax = plt.subplots(figsize=(7, 4))
    n = np.arange(0, 20)
    p_n = (1 - rho) * rho**n
    ax.bar(n, p_n, color="#4B8BBE", edgecolor="black")
    ax.set_xlabel("Jumlah Pelanggan dalam Sistem (n)")
    ax.set_ylabel("Probabilitas P(n)")
    ax.set_title("Distribusi Probabilitas Jumlah Pelanggan di Sistem")
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    st.pyplot(fig)

    st.info("📌 Grafik menunjukkan kemungkinan jumlah pelanggan dalam sistem. Semakin tinggi utilisasi (ρ), semakin besar peluang sistem padat.")

# Footer
st.markdown('<div class="footer">Dibuat dengan ❤️ oleh As Septian | Teori Antrian M/M/1 | Streamlit App</div>', unsafe_allow_html=True)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 🧭 Konfigurasi halaman
st.set_page_config(page_title="Simulasi Antrian M/M/1", layout="wide")

# 🎯 Header
st.markdown("""
<style>
.title { font-size: 32px; font-weight: bold; color: #4B8BBE; }
.subtitle { font-size: 18px; color: #333; margin-top: -10px; }
.footer { font-size: 14px; color: #999; text-align: center; margin-top: 40px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📊 Simulasi Model Antrian M/M/1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Model antrian dengan kedatangan dan pelayanan mengikuti distribusi Poisson</div>', unsafe_allow_html=True)

# 🔧 Input di sidebar
st.sidebar.header("⚙️ Parameter Antrian")
λ = st.sidebar.slider("λ - Rata-rata kedatangan", 0.1, 10.0, 2.0, 0.1,
                      help="Jumlah rata-rata pelanggan yang datang per satuan waktu")
μ = st.sidebar.slider("μ - Rata-rata layanan", 0.1, 10.0, 3.0, 0.1,
                      help="Jumlah rata-rata pelanggan yang dapat dilayani per satuan waktu")
st.sidebar.caption("ℹ️ Pastikan λ < μ agar sistem stabil")

# 🚨 Validasi kestabilan sistem
if λ >= μ:
    st.error("🚨 Sistem TIDAK stabil (λ ≥ μ). Pelanggan akan terus menumpuk!")
else:
    # 📊 Hitung metrik M/M/1
    ρ = λ / μ
    L = ρ / (1 - ρ)
    Lq = ρ**2 / (1 - ρ)
    W = 1 / (μ - λ)
    Wq = ρ / (μ - λ)

    # 📈 Tampilkan metrik hasil
    st.markdown("## 📋 Hasil Simulasi")
    col1, col2, col3 = st.columns(3)
    col1.metric("ρ - Utilisasi Server", f"{ρ:.2f}", help="Persentase waktu server sedang sibuk")
    col2.metric("L - Pelanggan dalam Sistem", f"{L:.2f}", help="Rata-rata pelanggan dalam sistem")
    col3.metric("Lq - Pelanggan dalam Antrian", f"{Lq:.2f}", help="Rata-rata pelanggan menunggu di antrian")

    col4, col5 = st.columns(2)
    col4.metric("W - Waktu Total per Pelanggan", f"{W:.2f}", help="Waktu rata-rata pelanggan di sistem")
    col5.metric("Wq - Waktu Tunggu", f"{Wq:.2f}", help="Waktu rata-rata pelanggan hanya di antrian")

    # 📉 Visualisasi Distribusi
    st.markdown("## 📉 Distribusi Probabilitas Pelanggan dalam Sistem")
    fig, ax = plt.subplots(figsize=(10, 5))
    n = np.arange(0, 20)
    p_n = (1 - ρ) * ρ**n
    bars = ax.bar(n, p_n, color="#4B8BBE", edgecolor="black")

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.005, f"{yval:.2f}",
                ha='center', va='bottom', fontsize=9)

    ax.set_xlabel("Jumlah Pelanggan (n)", fontsize=12)
    ax.set_ylabel("Probabilitas P(n)", fontsize=12)
    ax.set_title("Distribusi Peluang Jumlah Pelanggan dalam Sistem", fontsize=14, weight='bold')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)
    st.caption("📌 Semakin besar ρ, sistem makin padat dan distribusi makin berat ke kanan.")

# 👣 Footer
st.markdown('<div class="footer">Dibuat dengan ❤️ oleh As Septian | Model M/M/1 | Streamlit App</div>', unsafe_allow_html=True)

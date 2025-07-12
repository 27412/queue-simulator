import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Simulasi Antrian M/M/1", layout="centered")

st.title("📊 Simulasi Antrian M/M/1")

# Input λ dan μ
lambda_val = st.number_input("Rata-rata kedatangan (λ)", min_value=0.01, value=2.0, step=0.1)
mu_val = st.number_input("Rata-rata layanan (μ)", min_value=0.01, value=3.0, step=0.1)

# Validasi sistem stabil
if lambda_val >= mu_val:
    st.error("⚠️ Sistem tidak stabil. Pastikan λ < μ")
else:
    rho = lambda_val / mu_val
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu_val - lambda_val)
    Wq = rho / (mu_val - lambda_val)

    st.subheader("📈 Hasil Perhitungan:")
    st.write(f"ρ (Utilisasi): {rho:.2f}")
    st.write(f"L (Pelanggan dalam sistem): {L:.2f}")
    st.write(f"Lq (Pelanggan dalam antrian): {Lq:.2f}")
    st.write(f"W (Waktu dalam sistem): {W:.2f}")
    st.write(f"Wq (Waktu dalam antrian): {Wq:.2f}")

    st.subheader("📉 Visualisasi Distribusi Probabilitas")
    fig, ax = plt.subplots()
    n = np.arange(0, 20)
    p_n = (1 - rho) * rho**n
    ax.bar(n, p_n, color="skyblue")
    ax.set_xlabel("Jumlah Pelanggan dalam Sistem")
    ax.set_ylabel("Probabilitas")
    ax.set_title("Distribusi Jumlah Pelanggan")
    st.pyplot(fig)

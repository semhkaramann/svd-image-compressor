import numpy as np
from PIL import Image
import streamlit as st

# --- 1. MATEMATİKSEL SVD MOTORU ---
def compress_channel(channel_matrix: np.ndarray, k: int) -> np.ndarray:
    # Matrisi U, Sigma (S) ve V^T bileşenlerine ayır
    U, S, Vt = np.linalg.svd(channel_matrix, full_matrices=False)
    # İlk k tekil değeri kullanarak matrisi yeniden inşa et
    reconstructed = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))
    # Değerleri 0-255 piksel sınırında tut
    return np.clip(reconstructed, 0, 255)

def compress_image(image: Image.Image, k: int) -> Image.Image:
    img_array = np.array(image, dtype=float)
    # R, G ve B renk kanallarını ayrı ayrı işle
    r_compressed = compress_channel(img_array[:, :, 0], k)
    g_compressed = compress_channel(img_array[:, :, 1], k)
    b_compressed = compress_channel(img_array[:, :, 2], k)
    # Kanalları birleştir ve görsele dönüştür
    compressed_array = np.stack([r_compressed, g_compressed, b_compressed], axis=2)
    return Image.fromarray(compressed_array.astype(np.uint8))

# --- 2. KULLANICI ARAYÜZÜ (STREAMLIT) ---
st.set_page_config(page_title="SVD Görsel Sıkıştırma", layout="wide")

st.title("Lineer Cebir (SVD) ile Görsel Sıkıştırma")
st.write("Tekil Değer Ayrışımı ($A = U \\Sigma V^T$) kullanarak matris mertebesini düşürme deneyi.")

uploaded_file = st.file_uploader("Bir görsel yükleyin (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    original_img = Image.open(uploaded_file).convert("RGB")
    width, height = original_img.size
    max_k = min(width, height)

    k = st.slider(
        "Kullanılacak Tekil Değer Sayısı (k)", 
        min_value=1, 
        max_value=min(max_k, 150), 
        value=20, 
        step=1
    )

    with st.spinner("Matris ayrışımı hesaplanıyor..."):
        compressed_img = compress_image(original_img, k)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"Orijinal Görsel ({width}x{height})")
        st.image(original_img, use_container_width=True)
        
    with col2:
        st.subheader(f"Sıkıştırılmış Görsel (k = {k})")
        st.image(compressed_img, use_container_width=True)

    original_elements = width * height
    compressed_elements = k * (width + height + 1)
    savings = (1 - (compressed_elements / original_elements)) * 100
    
    st.success(f"Teorik Matris Tasarrufu: Yaklaşık %{max(0.0, savings):.1f}")
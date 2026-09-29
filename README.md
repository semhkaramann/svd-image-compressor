# 📷 SVD Tabanlı Görsel Sıkıştırma Motoru

Bu proje, Lineer Cebir prensiplerinden **Tekil Değer Ayrışımı (Singular Value Decomposition - SVD)** yöntemini kullanarak dijital görüntüler üzerinde düşük mertebeli matris yaklaşımı (low-rank approximation) gerçekleştiren interaktif bir web uygulamasıdır.

---

## 📐 Matematiksel Temel

Dijital bir görsel matrisi $A \in \mathbb{R}^{m \times n}$, SVD ile üç ayrı matrisin çarpımı olarak ifade edilir:

$$A = U \Sigma V^T$$

* **$U \in \mathbb{R}^{m \times m}$**: Sol tekil vektörleri içeren ortogonal matris.
* **$\Sigma \in \mathbb{R}^{m \times n}$**: Köşegeninde büyükten küçüğe sıralı tekil değerleri ($\sigma_1 \ge \sigma_2 \ge \dots \ge 0$) barındıran matris.
* **$V^T \in \mathbb{R}^{n \times n}$**: Sağ tekil vektörlerin transpozesi.

### Düşük Mertebeli Yaklaşım (Rank-$k$ Approximation)
Görüntüdeki en baskın $k$ adet tekil değer seçilerek matris yeniden oluşturulur ($k \ll \min(m, n)$):

$$A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^T$$

Eckart-Young-Mirsky teoremine göre $A_k$, $A$ matrisine Frobenius normunda en yakın $k$-mertebeli yaklaşımdır. Bu sayede insan gözünün algılayamayacağı bilgi fazlalığı elenerek **%70'in üzerinde teorik veri tasarrufu** sağlanır.

---

## 🛠️ Teknolojiler
* **Python 3.x**
* **NumPy:** Matris ayrışımı ve vektörize işlemler
* **Pillow (PIL):** Piksel matris manipülasyonu
* **Streamlit:** İnteraktif veri arayüzü

---

## 🚀 Kurulum ve Çalıştırma

1. Depoyu klonlayın:
```bash
git clone [https://github.com/KULLANICI_ADINIZ/svd-image-compressor.git](https://github.com/KULLANICI_ADINIZ/svd-image-compressor.git)
cd svd-image-compressor
pip install -r requirements.txt
streamlit run app.py

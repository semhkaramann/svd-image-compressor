import numpy as np
from PIL import Image
def compress_channel(channel_matrix: np.ndarray, k: int) -> np.ndarray:
    U, S, Vt = np.linalg.svd(channel_matrix, full_matrices=False)
    reconstructed = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))
    return np.clip(reconstructed, 0, 255)
    def compress_image(image: Image.Image, k: int) -> Image.Image:
        img_array = np.array(image, dtype=float)
        r_compressed = compress_channel(img_array[:, :, 0], k)
    g_compressed = compress_channel(img_array[:, :, 1], k)
    b_compressed = compress_channel(img_array[:, :, 2], k)
    compressed_array = np.stack([r_compressed, g_compressed, b_compressed], axis=2)
    return Image.fromarray(compressed_array.astype(np.uint8))

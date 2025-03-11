
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def recreate_approx_image(u, sigma, v, k):
    B = np.dot(u[:, :k], np.dot(np.diag(sigma[:k]), v[:k, :]))
    A_hat = np.clip(B, 0, 255).astype(np.uint8)
    return A_hat

def get_error(A, A_hat):
    return np.linalg.norm(A - A_hat)

def svd_compression(image_path):
    print("~~Image Compression Using SVD~~")
    img = Image.open(image_path)
    plt.imshow(img)
    plt.show()
    img = img.convert('L')
    A = np.array(img)

    u, sigma, v = np.linalg.svd(A, full_matrices=False)
    m, n = A.shape
    print('Dimensions of the Image:', m, n)

    errors, compression_ratios, compressed_sizes = [], [], []
    for k in [2, 4, 8, 16, 32, 64, 128]:
        A_hat = recreate_approx_image(u, sigma, v, k)
        error = get_error(A, A_hat)
        errors.append(error)

        svd_rep = k * (m + n + 1)
        compressed_sizes.append(svd_rep)

        compression_ratio = svd_rep / (m * n)
        compression_ratios.append(compression_ratio)

        plt.subplot(1, 2, 1)
        plt.imshow(A, cmap='gray')
        plt.title('Original Image')

        plt.subplot(1, 2, 2)
        plt.imshow(A_hat, cmap='gray')
        plt.title(f'Reconstructed Image (k={k})')

        plt.show()

    print(f"Total Compressed Size: {sum(compressed_sizes)}")
    print(f"Total File Size (original): {os.path.getsize(image_path)} bytes")

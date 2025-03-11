import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

def get_error(A, A_hat):
    return np.linalg.norm(A - A_hat)

def manual_pca_reconstruction(A, k):
    A_meaned = A - np.mean(A, axis=0)
    covariance_matrix = np.cov(A_meaned, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
    
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    
    W = sorted_eigenvectors[:, :k]
    A_reduced = np.dot(A_meaned, W)
    A_hat = np.dot(A_reduced, W.T) + np.mean(A, axis=0)
    
    return np.clip(A_hat, 0, 255).astype(np.uint8)

def pca_compression(image_path):
    print("~~Image Compression Using PCA~~")
    img = Image.open(image_path)
    plt.imshow(img)
    plt.show()

    img = img.convert('L')
    A = np.array(img)
    m, n = A.shape

    errors, compression_ratios, compressed_sizes = [], [], []
    for k in [2, 4, 8, 16, 32, 64, 128]:
        A_hat = manual_pca_reconstruction(A.astype(float), k)
        error = get_error(A.astype(float), A_hat)
        errors.append(error)

        pca_rep = k * (m + n)
        compressed_sizes.append(pca_rep)

        compression_ratio = pca_rep / (m * n)
        compression_ratios.append(compression_ratio)

        plt.subplot(1, 2, 1)
        plt.imshow(A.astype(float), cmap='gray')
        plt.title('Original Image')

        plt.subplot(1, 2, 2)
        plt.imshow(A_hat.astype(float), cmap='gray')
        plt.title(f'Reconstructed Image (PCA k={k})')

        plt.show()

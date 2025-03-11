from svd_compression import svd_compression
from pca_compression import pca_compression
from image_utils import display_image_info, resize_image, crop_image

def main_menu():
    print("~ Image Compression Menu ~")
    
    while True:
        print("1. Compress using SVD")
        print("2. Compress using PCA")
        print("3. Display Image Information")
        print("4. Resize Image")
        print("5. Crop Image")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            image_path = input("Enter the path of the image file: ")
            svd_compression(image_path)

        elif choice == '2':
            image_path = input("Enter the path of the image file: ")
            pca_compression(image_path)

        elif choice == '3':
            image_path = input("Enter the path of the image file: ")
            display_image_info(image_path)

        elif choice == '4':
            image_path = input("Enter the path of the image file: ")
            new_size = tuple(map(int, input("Enter new size (width height): ").split()))
            resize_image(image_path, new_size)

        elif choice == '5':
            image_path = input("Enter the path of the image file: ")
            crop_box = tuple(map(int, input("Enter the crop box (left top right bottom): ").split()))
            crop_image(image_path, crop_box)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()

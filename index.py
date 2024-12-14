import os
from PIL import Image

def img_to_pdf():
    try:
        n = int(input("Enter the number of images to convert: "))

        if (n<=0) :
            print("Number of images should be greater than 0")
            return
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    

    imgs = []
    print("\nEnter the paths to images in order:-")
    for i in range(n):
        img_path = input(f"Enter the path to image {i+1}: ").strip()
        if not os.path.isfile(img_path):
            print(f"Image {img_path} does not exist.")
            return
        
        imgs.append(img_path)
    

    output_dir = "/home/nexus/Glint"
    os.makedirs(output_dir, exist_ok=True)

    filename = input("\nWhat do you want to name the pdf file? ").strip()
    if not filename:
        filename = "glint_pdf_converted"
    
    output_path = os.path.join(output_dir, (filename+'.pdf'))

    if os.path.exists(output_path):
        print(f"\nA file named '{filename}.pdf' already exists in {output_dir}. Please choose a different name.")
        return

    try:
        images = [Image.open(path).convert("RGB") for path in imgs]
        images[0].save(output_path, save_all=True, append_images=images[1:])
        print(f"PDF saved at {output_path}")
    except Exception as e:
        print(f"An error occurred while converting images to PDF: {e}")

if __name__ == '__main__':
    img_to_pdf()
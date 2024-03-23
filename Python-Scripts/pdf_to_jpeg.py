from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Convert each PDF file to images
    for pdf_file in os.listdir(pdf_path):
        if pdf_file.endswith(".pdf"):
            pdf_file_path = os.path.join(pdf_path, pdf_file)
            images = convert_from_path(pdf_file_path)
            
            # Save each page of the PDF as an image
            for i, image in enumerate(images):
                image_path = os.path.join(output_folder, f"{pdf_file[:-4]}_page_{i+1}.jpg")

                image.save(image_path, "JPEG")

if __name__ == "__main__":
    pdf_folder ="/home/aswin/Downloads/down/drive-download-20230506T104155Z-001/1_Profile" 
    output_folder ="/home/aswin/Downloads/down/drive-download-20230506T104155Z-001/1_Profile/images"
    
    pdf_to_images(pdf_folder, output_folder)


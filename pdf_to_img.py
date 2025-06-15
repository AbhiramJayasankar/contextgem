import os
import pymupdf  # Using the modern 'pymupdf' import for PyMuPDF

def convert_pdfs_to_images(input_dir: str, output_dir: str, zoom_factor: int = 1):
    """
    Recursively finds all PDF files in a given input directory, converts each
    page to a PNG image with a specified zoom factor, and saves them in a
    corresponding folder structure within the output directory.

    Args:
        input_dir (str): The absolute or relative path to the directory
                         containing the source PDF files.
        output_dir (str): The absolute or relative path to the directory where
                          the output images will be saved.
        zoom_factor (int): The factor by which to increase the image resolution.
                           A value of 1 is standard (72 DPI). A value of 2
                           doubles the resolution (144 DPI), and so on.
    """
    # --- Validate input directory ---
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{os.path.abspath(input_dir)}' not found or is not a directory.")
        return

    print("Starting PDF conversion process...")
    print(f"Input directory: '{os.path.abspath(input_dir)}'")
    print(f"Output directory: '{os.path.abspath(output_dir)}'")
    print(f"Image Zoom Factor: {zoom_factor}x (Resulting DPI: {72 * zoom_factor})")

    # The transformation matrix is created directly from the zoom factor.
    matrix = pymupdf.Matrix(zoom_factor, zoom_factor)
    
    # Traverse the input directory recursively
    for dirpath, _, filenames in os.walk(input_dir):
        for filename in filenames:
            # Check if the file is a PDF
            if filename.lower().endswith(".pdf"):
                pdf_full_path = os.path.join(dirpath, filename)
                print(f"\nProcessing PDF: {pdf_full_path}")

                try:
                    # --- Create the corresponding output directory structure ---
                    
                    # Get the base name of the PDF without the extension
                    pdf_name_without_ext = os.path.splitext(filename)[0]
                    
                    # Get the relative path of the PDF's directory from the input_dir
                    relative_dir_path = os.path.relpath(dirpath, input_dir)
                    
                    # Define the specific folder for this PDF's images
                    image_output_folder = os.path.join(output_dir, relative_dir_path, pdf_name_without_ext)
                    
                    # Create the directories if they don't exist
                    os.makedirs(image_output_folder, exist_ok=True)
                    print(f"  -> Saving images to: {image_output_folder}")

                    # --- Open the PDF and convert pages to images ---
                    
                    with pymupdf.open(pdf_full_path) as doc:
                        if not doc.page_count:
                            print(f"  -> Warning: PDF '{filename}' has no pages. Skipping.")
                            continue
                            
                        # Iterate through each page of the document
                        for page_num, page in enumerate(doc):
                            # Render page to an image (pixmap) using the zoom matrix
                            pix = page.get_pixmap(matrix=matrix)
                            
                            # Define the output path for the image
                            output_image_path = os.path.join(image_output_folder, f"page_{page_num + 1}.png")
                            
                            # Save the pixmap as a PNG file
                            pix.save(output_image_path)

                        print(f"  -> Successfully converted {doc.page_count} pages.")

                except Exception as e:
                    print(f"  -> Error processing file {pdf_full_path}: {e}")
                    continue
    
    print("\nConversion process finished.")

# --- Example Usage ---
if __name__ == "__main__":
    # INSTRUCTIONS:
    # 1. Make sure you have PyMuPDF installed:
    #    pip install PyMuPDF
    #
    # 2. Set the input, output, and zoom factor parameters below.
    #
    # 3. Run the script.

    # Define the directory where your PDFs are located
    input_directory = "pdfs"
    
    # Define the directory where the images will be saved
    output_directory = "images"
    
    # Set the desired zoom factor.
    # 1 = standard resolution (72 DPI)
    # 2 = double resolution (144 DPI)
    # 3 = triple resolution (216 DPI), etc.
    resolution_zoom = 3

    # Create dummy files and folders for demonstration if they don't exist
    if not os.path.exists(input_directory):
        print("Creating dummy source directory and PDF for demonstration.")
        os.makedirs(os.path.join(input_directory, "projects"))
        try:
            # Use the modern pymupdf.Document() to create a new PDF
            doc = pymupdf.Document()  
            page = doc.new_page()
            page.insert_text((50, 72), "This is a sample PDF.")
            doc.save(os.path.join(input_directory, "report.pdf"))
            doc.close()
        except Exception as e:
            print(f"Could not create a dummy PDF. Please place your own PDFs in the '{input_directory}' folder. Error: {e}")

    # Call the main function with the specified zoom factor
    convert_pdfs_to_images(input_directory, output_directory, zoom_factor=resolution_zoom)
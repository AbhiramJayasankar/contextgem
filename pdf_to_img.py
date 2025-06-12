import os
import fitz  # PyMuPDF

def convert_pdfs_to_images(input_dir: str, output_dir: str):
    """
    Recursively finds all PDF files in a given input directory, converts each
    page to a PNG image, and saves them in a corresponding folder structure
    within the output directory.

    Args:
        input_dir (str): The absolute or relative path to the directory
                         containing the source PDF files.
        output_dir (str): The absolute or relative path to the directory where
                          the output images will be saved.
    """
    print(f"Starting PDF conversion process...")
    print(f"Input directory: '{os.path.abspath(input_dir)}'")
    print(f"Output directory: '{os.path.abspath(output_dir)}'")
    
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
                    # This preserves the folder hierarchy.
                    relative_dir_path = os.path.relpath(dirpath, input_dir)
                    
                    # Define the specific folder for this PDF's images
                    # If the PDF was at the root of input_dir, relative_dir_path will be '.',
                    # which os.path.join handles correctly.
                    image_output_folder = os.path.join(output_dir, relative_dir_path, pdf_name_without_ext)
                    
                    # Create the directories if they don't exist
                    os.makedirs(image_output_folder, exist_ok=True)
                    print(f"  -> Saving images to: {image_output_folder}")

                    # --- Open the PDF and convert pages to images ---
                    
                    # Use a context manager to ensure the file is closed properly
                    with fitz.open(pdf_full_path) as doc:
                        if not doc.page_count:
                            print(f"  -> Warning: PDF '{filename}' has no pages. Skipping.")
                            continue
                            
                        # Iterate through each page of the document
                        for page_num, page in enumerate(doc):
                            # Render page to an image (pixmap)
                            # Default resolution is 96 DPI. Increase matrix for higher resolution.
                            # For example, use fitz.Matrix(2, 2) for 192 DPI.
                            pix = page.get_pixmap()
                            
                            # Define the output path for the image
                            # Page numbers are 0-indexed, so we add 1 for human-readable filenames
                            output_image_path = os.path.join(image_output_folder, f"page_{page_num + 1}.png")
                            
                            # Save the pixmap as a PNG file
                            pix.save(output_image_path)

                        print(f"  -> Successfully converted {doc.page_count} pages.")

                except Exception as e:
                    print(f"  -> Error processing file {pdf_full_path}: {e}")
                    # Continue to the next file even if one fails
                    continue
    
    print("\nConversion process finished.")

# --- Example Usage ---
if __name__ == "__main__":
    # INSTRUCTIONS:
    # 1. Make sure you have PyMuPDF installed:
    #    pip install PyMuPDF
    #
    # 2. Set the input and output directories below.
    #    - Create a folder structure in 'source_pdfs' with some PDFs inside.
    #      For example:
    #      source_pdfs/
    #      ├── report.pdf
    #      └── projects/
    #          └── project_alpha.pdf
    #
    # 3. Run the script.
    #
    # 4. Check the 'output_images' folder. The script will create a
    #    structure like this:
    #    output_images/
    #    ├── report/
    #    │   ├── page_1.png
    #    │   └── page_2.png
    #    └── projects/
    #        └── project_alpha/
    #            ├── page_1.png
    #            └── ...

    # Define the directory where your PDFs are located
    input_directory = "pdfs"
    
    # Define the directory where the images will be saved
    output_directory = "images"

    # Call the main function
    convert_pdfs_to_images(input_directory, output_directory)

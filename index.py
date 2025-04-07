import fitz  # PyMuPDF
from deep_translator import GoogleTranslator

# Load the PDF
doc = fitz.open("pdf-location")

# Create a new PDF to store translated content
new_doc = fitz.open()

# Loop through pages
for page in doc:
    text = page.get_text()
    translated = GoogleTranslator(source='auto', target='fr').translate(text)
    
    # Create a new page with the same dimensions
    new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
    
    # Insert translated text (you can improve layout preservation here)
    new_page.insert_text((72, 72), translated, fontsize=10)

# Save the translated PDF
new_doc.save("savedpdfname")


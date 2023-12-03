import os
from colorama import Fore, Back, Style
import fitz  # pip install PyMuPDF

print("PDF to PNG converter")
pdffile = input("Enter PDF file path: ")
namefile = input("Enter saving name of the file: ")
zoom = input("Enter zoom level (1-10, Default is 2): ")

# Convert zoom to integer
zoom = int(zoom) if zoom else 2

# Setting default zoom level
if zoom > 10:
    zoom = 10
elif zoom < 1:
    zoom = 1

# Setting default saving path
save = namefile
if not os.path.exists(save):
    os.makedirs(save, exist_ok=True)

doc = fitz.open(pdffile)
i = 0
mat = fitz.Matrix(zoom, zoom)

# Loop through all pages
for page in doc:  # Total number of pages
    pix = page.get_pixmap(matrix=mat)
    output = os.path.join(save, f"{namefile}_{page.number}.png")  # Name and path of your saving folder
    pix.save(output)
    print(f"Finish converting page {page.number}")
    i += 1

print(f"{Fore.GREEN}Finish converting{Fore.BLUE} {i} {Style.RESET_ALL}{Fore.GREEN}pages{Style.RESET_ALL}")

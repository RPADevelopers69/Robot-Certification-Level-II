import os
import PyPDF2

# Chemin vers le dossier contenant les fichiers PDF
pdf_dir = 'C:\Ohlone\RoboCorp-main\Task_Files\Embeded_PDFs'

# Parcourir tous les fichiers PDF du dossier
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        # Ouvrir le fichier PDF
        with open(os.path.join(pdf_dir, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)

            # Extraire chaque page du PDF
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)

                # Réduire la taille de la page pour qu'elle s'affiche sur une seule page
                page.scale(1.5, 1.5)

                # Créer un objet PdfFileWriter pour stocker les pages modifiées
                pdf_writer = PyPDF2.PdfFileWriter()
                pdf_writer.addPage(page)

                # Écrire les pages modifiées dans un nouveau fichier PDF
                output_filename = os.path.splitext(filename)[0] + '_modifie.pdf'
                with open(os.path.join(pdf_dir, output_filename), 'wb') as output_file:
                    pdf_writer.write(output_file)

from pypdf import PdfReader, PdfWriter

class EncryptPdf:
    def encrypt(self, pdfname):
        reader = PdfReader(f"/home/linuxer77/Programs/Hackathon-Project/Disease-bullshit/media/pdfs/{pdfname}")
        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.encrypt("pass")

        encrypt_pdf_loc = f"/home/linuxer77/Programs/Hackathon-Project/Disease-bullshit/media/pdfs/{pdfname}"
        with open(f"/home/linuxer77/Programs/Hackathon-Project/Disease-bullshit/media/pdfs/{pdfname}", "wb") as f:
            writer.write(f) 
        
        return encrypt_pdf_loc

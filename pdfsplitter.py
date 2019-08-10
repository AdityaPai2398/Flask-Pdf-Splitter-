from PyPDF2 import PdfFileWriter,PdfFileReader

def cropper(start,end,file):
    inputPdf = PdfFileReader(open(file,"rb"))
    outPdf = PdfFileWriter()
    with open(file.split(".")[0]+"cropped"+".pdf","wb") as ostream:
        for page in range(start, end + 1):
          outPdf.addPage(inputPdf.getPage(start))
          outPdf.write(ostream)



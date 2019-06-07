from PyPDF2 import PdfFileWriter,PdfFileReader

def cropper(start,end,file):
    inputPdf=PdfFileReader(open(file,"rb"))
    outPdf=PdfFileWriter()

    ostream=open(file.split(".")[0]+"cropped"+".pdf","wb")

    while start <= end:
        outPdf.addPage(inputPdf.getPage(start))

        outPdf.write(ostream)

        start+=1
    ostream.close()

cropper(1,3,"sample.pdf")
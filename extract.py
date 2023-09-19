import PyPDF2

def extract_from_pdf(pdf_file:str) -> [str]:
    with open(pdf_file,'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf,strict =False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
        return pdf_text    
    
def extract_text_for_audio(extracted_text = extract_from_pdf('sample.pdf')):
      t=''
      for text in extracted_text:
           t += text
      return t
      
    

if __name__ == '__main__':
    extracted_text = extract_text_for_audio()
    #extract_from_pdf('sample.pdf')
    # for text in extracted_text:
    #      print(text)
    print(extracted_text)
#Importing the libraries
#You need to install both of these modules using pip command
import pyttsx3
import PyPDF2
#book=open('.....file_path\\Filename.pdf','rb')
book=open('Audiobook Sample.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print("Total no. of Pages inside PDF:"+ str(pages))
speaker= pyttsx3.init()
#For reading a particular pages you just need to give the it's previous pages number.
'''pnum=int(input("Enter the page number :"))
page = pdfReader.getPage(pnum)
text = page.extractText()
speaker.say(text)
print("Reading...")
speaker.runAndWait()'''

#for reading full pdf
for num in range(0,pages):
    print('Reading on page no.: ',0+num)
    page=pdfReader.getPage(0+num)
    text=page.extractText()
    speaker.say(text)
    print("Reading...")
    speaker.runAndWait()

'''Code By Aditya Chopra 7/10/20 11:46:21'''

import PyPDF2 
import csv
pdfFileObj = open('Grade.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
with open('File.csv') as csv_file:
	with open('audit_file.csv', mode='w') as audit_file:
		writer = csv.writer(audit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if(row[0][6:].isnumeric()):
				for j in range(pdfReader.numPages):
					pageObj = pdfReader.getPage(j)
					page=pageObj.extractText()
					z=len(page)
					for i in range(z-7):
						if(page[i:i+7]==row[0]):
							c=0
							for k in range(i+7,z):
								if(page[k]=='-'):
									c+=1
									if(c==1):
										row[3]=page[k-4]
									else:
										row[4]=page[k-2:k+9]
										break
			writer.writerow(row)
						
			
		print(row)








  
# extracting text from page 
print() 
pdfFileObj.close() 

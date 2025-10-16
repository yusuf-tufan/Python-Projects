import logging
from pdf2docx import Converter
import img2pdf

def pdftodocx(x,y):
    pdf_file=f'{x}.pdf'
    docx_file=f'{y}.docx'
    cv=Converter(pdf_file=pdf_file)
    cv.convert(docx_filename=docx_file)
    print('\nSuccesfully created!\n')
    cv.close()

def imgtopdf(a,b):
    with open(f'{b}.pdf',"wb") as f:
        f.write(img2pdf.convert(f'{a}.png'))
        print('\nSuccesfully created!')
print('''
0) Quit
1) Pdf to Docx
2) Img to Pdf
''')
logging.getLogger().setLevel(logging.ERROR)
while True:
    try:

        choose_procces=int(input("Choose a procces: "))

        if choose_procces==0:
            break
        elif choose_procces==1:
            x=input('PDF name: ')
            y=input('New name: ')
            pdftodocx(x,y)
        elif choose_procces==2:
            a=input('İmage name: ')
            b=input('New name: ')
            imgtopdf(a,b)
        else:
            print('Wrong Proccess')
    except TypeError:
        print('Not Found File Name')
    except KeyboardInterrupt:
        break
    except:
        print('Error!')

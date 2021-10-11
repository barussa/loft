import os
from pathlib import Path

from read_pdf import PdfReader
from excel_output import Excel

dir_read_files = input('Which directory would you like to execute?')

if Path(dir_read_files).exists():
    for i in os.listdir(dir_read_files):
        contract = PdfReader(f'{dir_read_files}/{i}')
        print(f'Extração do arquivo {i}')
        excel_output = Excel(contract)
else:
    print('Diretório Inválido!')



from pathlib import Path

import pandas as pd


class Excel:
    deed = None
    columns = None
    extraction = None

    def __init__(self, deed):
        if deed:
            try:
                deed.get_unit_id()
                self.deed = deed
                self.create_file()
            except:
                raise ValueError('Invalid Contract')

    def create_file(self):
        try:
            self.format_columns()
            self.generate_columns()
            self.get_values()
            self.insert_values()
        except:
            raise ValueError('Error creating file')

    def format_columns(self):
        pd.io.formats.excel.ExcelFormatter.header_style = None

    def generate_columns(self):
        self.columns = ['Unit_id', 'Valor_Total', 'Data_Contrato', 'Data_Escritura']

    def get_values(self):
        self.extraction = [self.deed.get_unit_id(), self.deed.get_total_value(), self.deed.get_sign_date(), self.deed.get_end_date()]

    def insert_values(self):
        if Path('OutputContratos.xlsx').exists():
            df = pd.read_excel('OutputContratos.xlsx')
            df2 = pd.DataFrame([self.extraction], columns=self.columns)
            df = pd.concat([df,df2])
        else:
            df = pd.DataFrame([self.extraction], columns=self.columns)
        df.to_excel('OutputContratos.xlsx', index=False)
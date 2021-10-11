import os

import PyPDF2
import re

from datetime import datetime, timedelta


class PdfReader:
    load_pdf = None
    number_of_pages = None
    text = str()

    def __init__(self, path_to_file):
        self.load_pdf = self.load(path_to_file)
        self.number_of_pages = self.load_pdf.getNumPages()
        self.text = self.read_text()

    def load(self, path_to_file):
        pdf_file = open(path_to_file, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        return read_pdf

    def read_text(self):
        text = str()
        for i in range(self.number_of_pages):
            page = self.load_pdf.getPage(i)
            text += page.extractText()
        text = text.replace('\n', '')
        return text

    def get_unit_id(self):
        try:
            unit_id = re.findall(r"\d{6}", self.text)[0]
            return unit_id
        except:
            return None

    def get_total_value(self):
        try:
            find_total_value = self.text.find('3.1')
            text2 = self.text[find_total_value:len(self.text)]
            total_value = re.findall("R\$\s([\d\.,]+)", text2)
            return total_value[0]
        except:
            return None


    def get_sign_date(self):
        try:
            find_sign_date = self.text.find("6.2")
            text_date = self.text[find_sign_date:]
            sign_date = text_date.split()[-1]
            return sign_date
        except:
            return None

    def date_by_adding_business_days(self, from_date, add_days):
        business_days_to_add = add_days
        current_date = from_date
        while business_days_to_add > 0:
            current_date += timedelta(days=1)
            weekday = current_date.weekday()
            if weekday >= 5:
                continue
            business_days_to_add -= 1
        return current_date

    def get_end_date(self):
        try:
            sign_date = self.get_sign_date()
            find_deed_date = self.text.find('5.1')
            find_52 = self.text.find('5.2')
            text_deed_date = self.text[find_deed_date:find_52]
            deed = re.findall("\d+", text_deed_date)
            deed = int(deed[-1])
            refact_sign_date = datetime.strptime(sign_date, "%d/%m/%Y")
            end_date = self.date_by_adding_business_days(refact_sign_date, 7)
            end_date = end_date.strftime("%d/%m/%Y")

            return end_date
        except:
            return None


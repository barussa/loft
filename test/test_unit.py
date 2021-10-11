import read_pdf as pdf

pdf_reader = pdf.PdfReader('../contracts/Contrato Teste.pdf')
class TestUnit:

    def test_get_unit_id_must_be_equal_to_expected_result(self):
        result = pdf_reader.get_unit_id()
        assert result == '942739'

    def test_check_numeric_value_in_string(self):
        result = pdf_reader.get_unit_id()
        assert result.isnumeric()

    def test_check_sign_date_format(self):
        result = pdf_reader.get_sign_date()
        assert result == '13/04/2021'

    def test_check_total_value(self):
        result = pdf_reader.get_total_value()
        assert result == '590.000,00'




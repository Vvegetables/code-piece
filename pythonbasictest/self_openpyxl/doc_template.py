from openpyxl.reader.excel import load_workbook
wb = load_workbook('document.xlsx')
wb.template = True
wb.save('document_template.xltx')
'''PDF merger using python'''

from pypdf import PdfWriter

merger=PdfWriter()

merger.append("DBMS-3.pdf")
merger.append("DDL.pdf")
merger.append("DML.pdf")
merger.write("Combined.pdf")

merger.close()
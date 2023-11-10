from pyhtml2pdf import converter
def convert(url,name) :
    converter.convert(url,name+'.pdf')
from datetime import datetime
from pydantic import BaseModel

class InvoiceInDb(BaseModel):
    id_factura: int=0
    nombre_cliente:str
    nombre_vendedor:str
    date:datetime=datetime.now()
    total:int

database_facturas= []
generator = {"No.Factura":0}

milisegs=datetime.now().strftime("%f")
ms=milisegs[-2:]

date_format = datetime.now().strftime("%Y%m%d%H%M%S")
time_stamp=date_format+ms

def save_invoice(invoice_in_db: InvoiceInDb):
    generator["No.Factura"]=generator["No.Factura"]+1
    identificador=int(time_stamp+str(generator["No.Factura"]))
    invoice_in_db.id_factura=identificador
    database_facturas.append(invoice_in_db)
    return invoice_in_db

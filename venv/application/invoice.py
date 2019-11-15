import os

from tempfile import NamedTemporaryFile

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
# choose english as language
os.environ["INVOICE_LANG"] = "en"

client = Client('Client company')
provider = Provider('My company', bank_account='2600420569', bank_code='2010')
creator = Creator('John Doe')

invoice = Invoice(client, provider, creator)
invoice.currency_locale = 'en_US.UTF-8'
invoice.add_item(Item(32, 600, description="Item 1"))
invoice.add_item(Item(60, 50, description="Item 2", tax=21))
invoice.add_item(Item(50, 60, description="Item 3", tax=0))
invoice.add_item(Item(5, 600, description="Item 4", tax=15))

pdf = SimpleInvoice(invoice)
pdf.gen("invoice.pdf", generate_qr_code=True)
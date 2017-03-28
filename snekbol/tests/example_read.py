from snekbol.document import Document

doc = Document('https://genemill.liv.ac.uk/sbol/')

with open('tests/BBa_I0462.xml', 'r') as f:
    doc.read(f)

with open('tests/BBa_I0462_rewrite.xml', 'wb') as fw:
    doc.write(fw)

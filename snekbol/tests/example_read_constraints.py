from snekbol.document import Document

doc = Document('https://genemill.liv.ac.uk/sbol/')

with open('tests/SequenceConstraintOutput.xml', 'r') as f:
    doc.read(f)

with open('tests/SequenceConstraintOutput_rewrite.xml', 'wb') as fw:
    doc.write(fw)

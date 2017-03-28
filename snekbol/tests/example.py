from snekbol.document import Document
from snekbol.componentdefinition import *
from snekbol.sequence import *

doc = Document('https://genemill.liv.ac.uk/sbol/')

gene = ComponentDefinition("BB0001")

promoter_seq = Sequence("R0010_seq", "ggctgca")
RBS_seq = Sequence("B0032_seq", "aattatataaa")
CDS_seq = Sequence("E0040_seq", "atgtaa")
terminator_seq = Sequence("B0012_seq", "attcga")

promoter = ComponentDefinition("R0010", roles=['Promoter'], sequences=[promoter_seq])
CDS = ComponentDefinition("B0032", roles=['CDS'], sequences=[CDS_seq])
RBS = ComponentDefinition("E0040", roles=['RBS'], sequences=[RBS_seq])
terminator = ComponentDefinition("B0012", roles=['Terminator'], sequences=[terminator_seq])

doc.add_component_definition(gene)
doc.add_component_definition(promoter)
doc.add_component_definition(CDS)
doc.add_component_definition(RBS)
doc.add_component_definition(terminator)

doc.assemble_component(gene, [promoter, RBS, CDS, terminator])

with open('tests/example.xml', 'wb+') as f:
    doc.write(f)

# first = gene.getFirstComponent()
# print(first.identity.get())
# last = gene.getLastComponent()
# print(last.identity.get())

import os
import unittest

from snekbol.document import Document
from snekbol.componentdefinition import ComponentDefinition
from snekbol.sequence import *

class DocumentTestCase(unittest.TestCase):

    def setUp(self):
        self.document = Document('http://example.org/sbol/')

    def test_create_invalid_url(self):
        with self.assertRaises(Exception) as context:
            doc = Document('example.org')
        self.assertTrue('Invalid namespace URI' in str(context.exception))

    def test_create_example_document(self):
        gene = ComponentDefinition("BB0001")

        promoter_seq = Sequence("R0010_seq", "ggctgca")
        RBS_seq = Sequence("B0032_seq", "aattatataaa")
        CDS_seq = Sequence("E0040_seq", "atgtaa")
        terminator_seq = Sequence("B0012_seq", "attcga")

        promoter = ComponentDefinition("R0010", roles=['Promoter'], sequences=[promoter_seq])
        CDS = ComponentDefinition("B0032", roles=['CDS'], sequences=[CDS_seq])
        RBS = ComponentDefinition("E0040", roles=['RBS'], sequences=[RBS_seq])
        terminator = ComponentDefinition("B0012", roles=['Terminator'], sequences=[terminator_seq])

        self.document.add_component_definition(gene)
        self.document.add_component_definition(promoter)
        self.document.add_component_definition(CDS)
        self.document.add_component_definition(RBS)
        self.document.add_component_definition(terminator)

        self.assertTrue(len(self.document._sequences) == 0)

        self.document.assemble_component(gene, [promoter, RBS, CDS, terminator])

        self.assertTrue(len(self.document._components) == 5)
        self.assertTrue(len(self.document._sequences) == 5)

    def test_read_valid(self):
        for file_path in os.listdir('./snekbol/tests/valid'):
            if file_path.endswith('xml'):
                with open('./snekbol/tests/valid/'+file_path) as rf:
                    doc = Document('https://example.org/sbol/')
                    doc.read(rf)

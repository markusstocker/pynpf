import unittest
from rdflib import URIRef
from pynpf.entity.entity import Entity


class TestEntity(unittest.TestCase):

    def test_init_1(self):
        e = Entity()
        self.assertIsNone(e.get_identifier())

    def test_init_2(self):
        e = Entity('http://example.org/e1')
        self.assertEqual('http://example.org/e1', e.get_identifier())
        self.assertEqual(URIRef('http://example.org/e1'), e.get_uri())

    def test_set_identifier_1(self):
        e = Entity()
        e.set_identifier('http://example.org/e1')
        self.assertEqual('http://example.org/e1', e.get_identifier())

    def test_set_identifier_2(self):
        e = Entity('http://example.org/e1')
        e.set_identifier('http://example.org/e1')
        self.assertEqual('http://example.org/e1', e.get_identifier())

    def test_set_identifier_3(self):
        e = Entity('http://example.org/e1')
        try:
            e.set_identifier('http://example.org/e2')
        except ValueError as e:
            self.assertEqual('Incompatible identifiers http://example.org/e1 http://example.org/e2', str(e))

suite = unittest.TestLoader().loadTestsFromTestCase(TestEntity)
unittest.TextTestRunner(verbosity=2).run(suite)
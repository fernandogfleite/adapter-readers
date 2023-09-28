from app.readers import JSONReader, XMLReader, ReaderAdapter
from xml.etree.ElementTree import ParseError

import pytest


class TestJSONReader:
    def test_read_existent_json(self):
        reader = JSONReader('app/tests/fixtures/test.json')
        data = reader.read()
        assert data == {'test': 'test'}
    
    def test_read_non_existent_json(self):
        reader = JSONReader('app/tests/fixtures/test2.json')
        with pytest.raises(FileNotFoundError):
            reader.read()
    
    def test_read_invalid_json(self):
        reader = JSONReader('app/tests/fixtures/test3.json')
        with pytest.raises(ValueError):
            reader.read()
    
    def test_read_invalid_file(self):
        reader = JSONReader('app/tests/fixtures/test.txt')
        with pytest.raises(ValueError):
            reader.read()


class TestXMLReader:
    def test_read_existent_xml(self):
        reader = XMLReader('app/tests/fixtures/test.xml')
        data = reader.read()
        assert data.tag == 'test'
    
    def test_read_non_existent_xml(self):
        reader = XMLReader('app/tests/fixtures/test2.xml')
        with pytest.raises(FileNotFoundError):
            reader.read()
    
    def test_read_invalid_xml(self):
        reader = XMLReader('app/tests/fixtures/test3.xml')
        with pytest.raises(ParseError):
            reader.read()
    
    def test_read_invalid_file(self):
        reader = XMLReader('app/tests/fixtures/test.txt')
        with pytest.raises(ParseError):
            reader.read()


class TestReaderAdapter:
    def test_read_json(self):
        reader = ReaderAdapter('app/tests/fixtures/test.json')
        data = reader.read()
        assert data == {'test': 'test'}
    
    def test_read_xml(self):
        reader = ReaderAdapter('app/tests/fixtures/test.xml')
        data = reader.read()
        assert data.tag == 'test'
    
    def test_read_invalid_file(self):
        with pytest.raises(ValueError):
            reader = ReaderAdapter('app/tests/fixtures/test.txt')
            reader.read()

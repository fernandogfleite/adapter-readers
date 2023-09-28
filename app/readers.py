import xml.etree.ElementTree as ET
import json
import os
import abc


class Reader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass


class XMLReader(Reader):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        return root


class JSONReader(Reader):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as json_file:
            data = json.load(json_file)
        return data


class ReaderAdapter(Reader):
    def __init__(self, filename):
        self.filename = filename
        self.extension = os.path.splitext(filename)[1][1:]
        
    def get_reader(self):
        try:
            readers = {
                'xml': XMLReader,
                'json': JSONReader
            }
            return readers[self.extension]
        except KeyError:
            raise ValueError('Unknown file type')

    def read(self):
        return self.get_reader()(self.filename).read()

#!/usr/bin/python
# -*- mode:python; coding:utf-8; tab-width:4 -*-

import os
import yaml
import json
import pprint
import subprocess
import csv
import logging

logging.basicConfig(
    level=logging.DEBUG,
    )
logger = logging.getLogger(__name__)


#DIRECTORY = '/home/miguel/proyectos/web/_private/posts'
DIRECTORY = 'example'


def stat_time_loader(filename):
    return os.stat(filename).st_atime

def git_time_loader(filename):
    # proof of concept. It doesn't works
    name = os.path.basename(filename)
    path = os.path.dirname(filename)
    cmd = 'git log -n1 --pretty=format:"%%at" -- %s' % name
    return subprocess.check_output(cmd, cwd=path)

def os_filename_loader(filename):
    return os.path.basename(filename)

def os_path_loader(filename):
    return os.path.dirname(filename)


class PropertyReader(object):
    def __init__(self, data_loaders = None):
        self._data_loaders = data_loaders if data_loaders else {}

    def read_file(self, filename):
        with file(filename) as fd:
            properties = yaml.safe_load_all(fd).next()
            for key, loader in self._data_loaders.items():
                properties[key] = loader(filename)
            return properties

    def read_files(self, directory):
        for root, dirs, files in os.walk(directory):
            for filename in files:
                yield self.read_file(os.path.join(root, filename))


class IndexGenerator(object):
    def __init__(self, keys=[], output_path='output'):
        self._keys = keys
        self._output_path = output_path

    def generate(self, inverse_file):
        try:
            os.makedirs(self._output_path)
        except OSError:
            pass

        for category, properties in inverse_file.items():
            output_file = os.path.join(self._output_path, category)
            logger.info('Generating file %s', output_file)
            with file(output_file, 'w+') as fd:
                json.dump(properties, fd)

class InverseFile(object):
    def __init__(self):
        self.inverse = {}

    def add(self, dictionary):
        for data in dictionary:
            for key, value in data.items():
                if key.startswith('.'):
                    continue
                self.__process_value(key, value, data)

    def __process_value(self, key, value, data):
        if isinstance(value, list):
            for item in value:
                self.__process_value
            return
        if key not in self.inverse:
            self.inverse[key] = {}
        if value not in self.inverse[key]:
            self.inverse[key][value] = []
        self.inverse[key][value].append(data)

def main():
    data_loaders = {
        '.filename': os_filename_loader,
        '.time': stat_time_loader,
        '.author': lambda x:'magmax',
        }

    prop_reader = PropertyReader(data_loaders)
    properties = list(prop_reader.read_files(DIRECTORY))

    inverse_file = InverseFile()
    inverse_file.add(properties)

    index_generator = IndexGenerator(['.filename', '.time', 'title'], 'site/app/index')
    index_generator.generate(inverse_file.inverse)


if __name__ == '__main__':
    main()


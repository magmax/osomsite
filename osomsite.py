#!/usr/bin/python
# -*- mode:python; coding:utf-8; tab-width:4 -*-

import os
import yaml
import pprint
import subprocess
import csv

DIRECTORY = '/home/miguel/proyectos/web/_private/posts'
#DIRECTORY = 'example'


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


class CsvFilesGenerator(object):
    def __init__(self, keys=[], output_path='output'):
        self.output_path = output_path
        self.keys = keys

    def generate(self, inverse_file):
        for category, properties in inverse_file.items():
            index_path = os.path.join(self.output_path, category)
            if not os.path.exists(index_path):
                os.makedirs(index_path)
            for category_value, items in properties.items():
                output_file = os.path.join(index_path, category_value)
                with file(output_file, 'w+') as fd:
                    csvwriter = csv.writer(fd)
                    for item in items:
                        row = []
                        for key in self.keys:
                            row.append(item.get(key, ''))
                        csvwriter.writerow(row)


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

    index_generator = CsvFilesGenerator(['.filename', '.time', 'title'], 'site/app/index')

#    pprint.pprint(inverse_file.inverse)
    index_generator.generate(inverse_file.inverse)

if __name__ == '__main__':
    main()


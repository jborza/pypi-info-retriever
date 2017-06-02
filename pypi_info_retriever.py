"""Retrieves package summary and licensing information from pypi repository
Accepts semicolon separated list of module;version such as
celery;4.0.2
requests;2.14.2
multiprocessing;2.6.2.1
scipy;0.18.1

Outputs a CSV with name, version, license_info, summary, homepage information
"""
import sys
import fileinput
import csv
import requests

def fix_new_line(s):
    return s.replace('\n', ' ')

def get_package_info(name, version):
    url = 'https://pypi.python.org/pypi/%s/%s/json' % (name, version)
    req = requests.get(url)
    if req.status_code == 404:
        return [name, version]
    json = req.json()
    license_info = fix_new_line(json['info']['license'])
    summary = fix_new_line(json['info']['summary'])
    homepage = json['info']['home_page']
    data = [name, version, license_info, summary, homepage]
    return data

def main():
    package_and_version_list = [line.strip().split(';') for line in fileinput.input()]
    processed = []
    for name, version in package_and_version_list:
        processed.append(get_package_info(name, version))
    writer = csv.writer(sys.stdout,
                        dialect='excel',
                        quoting=csv.QUOTE_NONNUMERIC,
                        lineterminator='\n')
    writer.writerow(['name', 'version', 'license', 'summary', 'homepage'])
    writer.writerows(processed)

main()

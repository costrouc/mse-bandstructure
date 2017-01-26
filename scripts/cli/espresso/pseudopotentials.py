import json
import pkg_resources

pps = json.loads(pkg_resources.resource_string(__name__, 'data/pseudopotentials.json').decode('utf-8'))

def filter_element(pps, element):
    return [pp for pp in pps if pp['symbol'].lower() == element.lower()]

def filter_type(pps, pp_type):
    return [pp for pp in pps if pp['pp_type'].lower() == pp_type.lower()]

def filter_functional(pps, functional):
    return [pp for pp in pps if pp['functional'].lower() == functional.lower()]

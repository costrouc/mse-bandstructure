try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import click

from espresso.pseudopotentials import pps, filter_element, filter_type, filter_functional


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    pass


@cli.command()
@click.option('--element', '-e', default=None)
@click.option('--detail/--no-detail', '-d', default=False)
@click.option('--type', '-t', default=None, type=click.Choice(['ULTRASOFT', 'NORMCONS', 'PAW']))
@click.option('--functional', '-f', default=None, type=click.Choice(['PBE', 'PBESOL', 'LDA', 'LDA exch-coor', 'BLYP', 'BP', 'PW91', 'meta-GGA']))
def list(element, detail, type, functional):
    filtered_pps = pps
    if element:
        filtered_pps = filter_element(filtered_pps, element)
    if type:
        filtered_pps = filter_type(filtered_pps, type)
    if functional:
        filtered_pps = filter_functional(filtered_pps, functional)

    for pp in filtered_pps:
        print('[{index:04}]\t{symbol:2}\t{pp_type:10}\t{functional:15}\tverified:{verified} - {title}'.format(**pp))
        if detail:
            startline = '|    '
            print(startline + pp['description'][2:].replace('\n', '\n' + startline) + '\n')

@cli.command()
@click.argument('index', type=click.INT)
def download(index):
    print('Downloading:\t{symbol:2}\t{pp_type:10}\t{functional:15} - {title}'.format(**pps[index]))
    with open(pps[index]['title'], 'wb') as f:
        f.write(urlopen(pps[index]['link']).read())


if __name__ == '__main__':
    cli(obj={})

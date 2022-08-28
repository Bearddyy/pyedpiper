import argparse
import json
from rich import print
from rich.layout import Layout
from rich.live import Live
from rich.table import Table

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description='PyEDPiper')
    
    # log output file
    parser.add_argument('-l', '--log', help='log output file', default='pyedpiper.log')

    #config file
    parser.add_argument('-c', '--config', help='config file', default='pyedpiper.json')

    #Parse arguments
    args = parser.parse_args()

    #Parse the config file
    with open(configFile) as f:
        config = json.load(f)

    rows = config['layout']['rows']
    cols = config['layout']['cols']

    #Create the layout
    layout = Layout(name="root")
    

if __name__ == '__main__':
    main()
    

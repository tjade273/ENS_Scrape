#!/usr/bin/env python3
from web3 import HTTPProvider
from ens import ENS
from sys import argv

if __name__ == '__main__':
    if len(argv) < 3:
        print("Usage: ./name_search.py [RPC endpoint] [name_file]")
    else:
        with open(argv[1], 'r') as f:
            names = f.read().splitlines()

        provider =HTTPProvider(argv[2]+":8545")

        ens = ENS(provider)

        open_names = []

        for name in names:
            if ens.owner(name) is None:
                open_names.append(name)

        print("Unclaimed names:\n")
        print('\n'.join(open_names))

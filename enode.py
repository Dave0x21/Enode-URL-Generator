#!/usr/bin/env python

import argparse
import codecs

from eth_keys import keys

parser = argparse.ArgumentParser(description='Generate enode url from private key')
parser.add_argument('privKey', metavar='privKey', type=str, help='Private key for generate enode url')
parser.add_argument('-i', '--ip', metavar='ip', dest='ip', default='0.0.0.0', type=str, help='IP Address of the node [Default 0.0.0.0.]')
parser.add_argument('-p', '--p2p', metavar='p2p', dest='p2p', default='30303', type=str, help='p2p port of the node [Default 30303]')
args = parser.parse_args()

if args.privKey.startswith('0x'):
    args.privKey = args.privKey[2:]

decoder = codecs.getdecoder("hex_codec")
private_key_bytes = decoder(args.privKey)

pk = keys.PrivateKey(private_key_bytes[0])

print('Your enode url is:\nenode://{}@{}:{}'.format(pk.public_key.to_hex()[2:], args.ip, args.p2p))

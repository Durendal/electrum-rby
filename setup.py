#!/usr/bin/env python3

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (3, 4, 0):
    sys.exit("Error: Electrum requires Python version >= 3.4.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-rby.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-rby.png'])
    ]

setup(
    name="Electrum-RBY",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'scrypt>=0.6.0',
        'protobuf',
        'dnspython',
        'jsonrpclib-pelix',
        'PySocks>=1.6.6',
    ],
    packages=[
        'electrum_rby',
        'electrum_rby_gui',
        'electrum_rby_gui.qt',
        'electrum_rby_plugins',
        'electrum_rby_plugins.audio_modem',
        'electrum_rby_plugins.cosigner_pool',
        'electrum_rby_plugins.email_requests',
        'electrum_rby_plugins.hw_wallet',
        'electrum_rby_plugins.keepkey',
        'electrum_rby_plugins.labels',
        'electrum_rby_plugins.ledger',
        'electrum_rby_plugins.trezor',
        'electrum_rby_plugins.digitalbitbox',
        'electrum_rby_plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum_rby': 'lib',
        'electrum_rby_gui': 'gui',
        'electrum_rby_plugins': 'plugins',
    },
    package_data={
        'electrum_rby': [
            'servers.json',
            'servers_testnet.json',
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum-rby'],
    data_files=data_files,
    description="Lightweight Rubycoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="http://electrum-rby.org",
    long_description="""Lightweight Rubycoin Wallet"""
)

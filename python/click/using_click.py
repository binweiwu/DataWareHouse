#! /usr/bin/env python
# coding: utf-8

import click

@click.command()
@click.option('--count', default=1, help='Number of repear.')
@click.option('--action', prompt='Action', help='action you enter.')

def using_click(count, action):
    """Simple program …….."""
    for i in range(count):
        click.echo('Study %s!' %action)

if __name__=='__main__':
    using_click()


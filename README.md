# Trowel

Utilities for finding, getting and parsing web map tiles.

## Install

    pip install git+https://github.com/mikeskaug/trowel.git

## Usage

    from trowel import utils

    (tile_X, tile_Y) = utils.lonlat_to_tile(-74.5567, 45.8773, 10)
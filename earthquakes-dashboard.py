import dask.dataframe as dd
import holoviews as hv
import datashader as ds
from colorcet import palette
import panel as pn
from holoviews.element.tiles import EsriImagery

topts = hv.opts.Tiles(width=700, height=600, bgcolor='black', 
                      xaxis=None, yaxis=None, show_grid=False)
tiles = EsriImagery().opts(topts) 
earthquakes  = dd.read_parquet('data/earthquakes.parq', engine='fastparquet').persist()
colormaps = {n: palette[n] for n in ['fire','bgy','bgyw','bmy','gray','kbc']}

x, y = ds.utils.lnglat_to_meters(earthquakes.longitude, earthquakes.latitude)
projected_earthquakes = earthquakes.assign(x=x, y=y).persist()

def view(cmap=colormaps['fire'], alpha=1, reverse_colormap=False):
    cmap = cmap if not reverse_colormap else cmap[::-1]
    return tiles.opts(alpha=alpha) * projected_earthquakes.hvplot.points(
        'x', 'y', datashade=True, cmap=cmap
    )

explorer = pn.interact(view, cmap=colormaps, alpha=(0, 1.), reverse_colormap=False)

pn.Row(pn.Column('# Earthquake Explorer', explorer[0]), explorer[1]).servable()

from bokeh.plotting import figure, output_file, show
from bokeh.io import save
from bokeh.layouts import gridplot 
from motw.snapshot import Snapshot
import requests as req
from datetime import datetime
import pandas as pd

def download(str):
	res = req.get("http://web.archive.org/cdx/search/cdx?url="+str)
	snapshots = res.text.split('\n')
	snapshot_list = []
	for snapshot in snapshots:
		snapshot_items = snapshot.split(' ')
		if len(snapshot_items) == 7:
			snap = Snapshot(snapshot_items[0], snapshot_items[1], snapshot_items[2], snapshot_items[3], snapshot_items[4], snapshot_items[5], snapshot_items[6])
		snapshot_list.append(snap)
	return snapshot_list

def Count(str):
	snapshot_list = download(str)
	total_number = len(snapshot_list)
	return total_number



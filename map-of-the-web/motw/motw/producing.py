from bokeh.plotting import figure, output_file, show
from bokeh.io import save
from bokeh.layouts import gridplot 
from motw.snapshot import Snapshot
import requests as req
from datetime import datetime
import pandas as pd

def timestamp2date(x):
	return x[0:4]+"-"+x[4:6]+"-01"

def Frequency(snapshot_list):
	string = snapshot_list[0]['timestamp']
	time = timestamp2date(string)
	timestamp_list = []
	frequency_list = []
	frequency = dict()
	frequency[time] = 1
	timestamp_list.append(time)
	number = 1
	for i in range(1, len(snapshot_list)):
		if (timestamp2date(snapshot_list[i]['timestamp']) != time):
			time = timestamp2date(snapshot_list[i]['timestamp'])
			timestamp_list.append(time)
			frequency_list.append(number)
			number = 1
		else:
			number += 1
			frequency[time] = number
	frequency_list.append(number)
	return [timestamp_list, frequency_list]

def test_use(snapshot_list):
	digest_use = dict()
	digest_list = []
	timestamp_list = []
	usefulnes_list = []
	digest_use[snapshot_list[0]['digest']] = snapshot_list[0]['timestamp']
	digest_list.append(snapshot_list[0]['digest'])
	timestamp_list.append(snapshot_list[0]['timestamp'])
	usefulnes_list.append(1)
	for i in range(1, len(snapshot_list)):
		timestamp_list.append(snapshot_list[i]['timestamp'])
		if snapshot_list[i]['digest'] in digest_use.keys():
			snapshot_list[i]['usefulness'] = 0
			snapshot_list[i]['same_as'] = digest_use[snapshot_list[i]['digest']]
		else:
			digest_use[snapshot_list[i]['digest']] = snapshot_list[i]['timestamp']
			digest_list.append(snapshot_list[i]['digest'])
		usefulnes_list.append(snapshot_list[i]['usefulness'])
	return [timestamp_list, usefulnes_list]

def draw_broken_line(data, dw, dh):
	tools = "pan,box_zoom,reset,save"
	#path = r"bokehTest.html"
	#output_file(path)  
	x = pd.to_datetime(data[0])
	y = data[1]
	s1 = figure(plot_width=dw, plot_height=dh, title=None, x_axis_type="datetime")
	s1.line(x, y, color="navy", line_width=2)
	s1.text(x, y, text=y, text_baseline="middle", text_align="center")
	return s1

def test_use_draw(data, duplist, dw, dh):
	one = []
	for i in range(len(data)):
		one.append(0.5)
	xd = pd.to_datetime(data)
	print(xd[2])
	s1 = figure(plot_width=dw, plot_height=dh, x_axis_type="datetime")
	s1.vbar(x=xd, width=3, bottom=0, top=one, color="firebrick")
	s1.vbar(x=xd, width=3, bottom=0, top=duplist, color="navy")
	return s1

'''def huadiandian(data, dw, dh):
	one = []
	for i in range(len(data)):
		one.append(1)
	s1 = figure(plot_width=dw, plot_height=dh)'''

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

def duplicatelist(snapshot_list):
	digest_use = dict()
	digest_list = []
	timestamp_list = []
	usefulnes_list = []
	digest_use[snapshot_list[0]['digest']] = snapshot_list[0]['timestamp']
	digest_list.append(snapshot_list[0]['digest'])
	timestamp_list.append(snapshot_list[0]['timestamp'])
	usefulnes_list.append(1)
	for i in range(1, len(snapshot_list)):
		timestamp_list.append(snapshot_list[i]['timestamp'])
		if snapshot_list[i]['digest'] in digest_use.keys():
			snapshot_list[i]['usefulness'] = 0
			snapshot_list[i]['same_as'] = digest_use[snapshot_list[i]['digest']]
		else:
			digest_use[snapshot_list[i]['digest']] = snapshot_list[i]['timestamp']
			digest_list.append(snapshot_list[i]['digest'])
		usefulnes_list.append(snapshot_list[i]['usefulness'])
	dl=[]
	for i in range(len(snapshot_list)):
		dl.append(snapshot_list[i]["usefulness"])
	#print(dl)
	return dl

def processing(str):
	snapshot_list = download(str)
	duplist = duplicatelist(snapshot_list)
	data = Frequency(snapshot_list)
	picture1 = draw_broken_line(data, 1280, 480)
	use = test_use(snapshot_list)
	timestamp_list = use[0]
	#print(timestamp_list[1])
	picture2 = test_use_draw(timestamp_list, duplist, 1280, 480)
	return [picture1, picture2]

def Count(str):
	snapshot_list = download(str)
	total_number = len(snapshot_list)
	return total_number



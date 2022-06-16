from posixpath import split
import re
from django.shortcuts import redirect
from flask import Flask, request, render_template, jsonify, redirect
app = Flask(__name__)
import runsrcIp, rundestIp, runTerminalData, printData, runApi, runApiall
import os, json
import matplotlib.pyplot as plt

import ast
#from srx import analyze_session_table

totalConnections=0

@app.route('/', methods= ['GET', 'POST'])
def get_message():
 # if request.method == "GET":
 print("Got request in main function")
 return render_template("index.html")

@app.route('/upload_static_file', methods=['POST'])
def upload_static_file():
 print("Got request in static files")
 print(request.files)
 f = request.files['static_file']
 f.save(f.filename)

 src=f.filename
 dest="sessiontable.txt"
 f.filename=os.rename(src,dest)

 resp = {"success": True, "response": "file saved!"}
 return jsonify(resp), 200

@app.route('/metrics')
def display_metrics():
    terData=runTerminalData.terminalMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    print(metricsJson)
    f=open("graphVal.txt","r")
    graphList=f.read()
    return render_template("metrics.html",metricsData=metricsJson,graphList=graphList)
    #return (metricsJson)

    #return jsonify(data)
    #return srx.analyze_session_table()  
    #return redirect("https://seashells.io/", code=302)

@app.route('/metricstest')
def display_metricstest():
    # terData=rundestIp.destMetrics()
    # metricsJson=terData.decode('utf-8').replace("'",'"')
    # print(metricsJson)
    # splitmetricsJson=metricsJson.split(",")
    # print(splitmetricsJson)
    # print(len(splitmetricsJson))
    #paramerters   ,metricsData=metricsJson,splitData=splitmetricsJson
    return render_template("newmetrics.html")

@app.route('/metricsall')
def display_metricsall():
    # terData=rundestIp.destMetrics()
    # metricsJson=terData.decode('utf-8').replace("'",'"')
    # print(metricsJson)
    # splitmetricsJson=metricsJson.split(",")
    # print(splitmetricsJson)
    # print(len(splitmetricsJson))
    #paramerters   ,metricsData=metricsJson,splitData=splitmetricsJson
    return render_template("allmetrics.html")

@app.route('/metricsOut')
def metricsOut():
    terData=runTerminalData.terminalMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/srcipOut')
def srcipOut():
    terData=runApi.srcMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/dstipOut')
def destipOut():
    terData=runApi.dstMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/srcportOut')
def srcportOut():
    terData=runApi.srcPortMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/dstportOut')
def destportOut():
    terData=runApi.dstPortMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/protoOut')
def protoOut():
    terData=runApi.protoMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/policyOut')
def policyOut():
    terData=runApi.policyMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/interfaceOut')
def interfaceOut():
    terData=runApi.interfaceMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/packetsOut')
def packetsOut():
    terData=runApi.packetsMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/bytesOut')
def bytesOut():
    terData=runApi.bytesMetrics()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/srcipOutall')
def srcipOutall():
    terData=runApiall.srcMetricsall()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/dstipOutall')
def destipOutall():
    terData=runApiall.dstMetricsall()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/srcportOutall')
def srcportOutall():
    terData=runApiall.srcPortMetricsall()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/dstportOutall')
def destportOutall():
    terData=runApiall.dstPortMetricsall()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/protoOutall')
def protoOutall():
    terData=runApiall.protoMetricsall()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/policyOutall')
def policyOutall():
    terData=runApiall.policyMetricsall()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/interfaceOutall')
def interfaceOutall():
    terData=runApiall.interfaceMetricsall()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/packetsOutall')
def packetsOutall():
    terData=runApiall.packetsMetricsall()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

@app.route('/metrics/bytesOutall')
def bytesOutall():
    terData=runApiall.bytesMetricsall()
    metricsJson=terData.decode('utf-8').replace("'",'"')
    return metricsJson

if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)
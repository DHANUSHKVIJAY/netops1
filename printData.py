from flask import render_template

def parseMetricsGraph(connectionCount,inCount,outCount):
	print("Total Connections: ",connectionCount,"\nIn Count: ",inCount,"\t\tOut Count: ",outCount)
    
# def saveGraphValues(totalConnections,successConnections,destroyedConnections):
#     totalConnections=totalConnections
#     successConnections=successConnections
#     destroyedConnections=destroyedConnections
#     #print("TC:",totalConnections,"SC:",successConnections,"DC:",destroyedConnections)
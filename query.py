from datadog import initialize, api
import time
import json
import sys
 
#must pass in api key and app key from teamcity
options = {
    'api_key': sys.argv[1],
    'app_key': sys.argv[2]
}
 
initialize(**options)
 
start = int(time.time()) - 120
end = start + 120

#system.load.1 = The average system load over one minute.
query_cpu = 'system.cpu.idle{farm:caproxy,environment:development,farm_role:caproxy-app} by {host}' 
results = api.Metric.query(start=start - 120, end=end, query=query_cpu)

with open('/opt/tcagents/tc_cs_agent/temp/agentTmp/cpu.json', 'w') as file_:
    file_.write(json.dumps(results))

#system.mem.used = The amount of RAM in use shown as byte
query_memory = 'system.mem.used{farm:caproxy,environment:development,farm_role:caproxy-app} by {host}'
results = api.Metric.query(start=start - 120, end=end, query=query_memory)

with open('/opt/tcagents/tc_cs_agent/temp/agentTmp/memory.json', 'w') as file_:
    file_.write(json.dumps(results))
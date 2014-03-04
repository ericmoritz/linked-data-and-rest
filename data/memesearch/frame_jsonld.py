from pyld import jsonld
import sys
import json
graph = json.load(sys.stdin)
frame = json.load(open(sys.argv[1]))

print json.dumps(jsonld.frame(graph, frame), indent=2)

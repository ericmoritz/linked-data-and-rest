from rdflib import Graph
import sys


if __name__ == '__main__':
    if len(sys.argv) == 3:
        file = sys.stdin
        in_format = sys.argv[1]
        out_format = sys.argv[2]
        graph = Graph().parse(file=file, publicID="http://example.com/", format=in_format)
    else:
        in_uri = sys.argv[1]
        in_format = sys.argv[2]
        out_format = sys.argv[3]
        graph = Graph().parse(in_uri, publicID="http://example.com/", format=in_format)

    print graph.serialize(format=out_format),


from rdflib import Graph, URIRef


g = Graph().parse("./graph.ttl", format="turtle")

# build up the index resource
index = Graph()
index + g.triples( (URIRef("/"), None, None) ) # copy the IndexPage object

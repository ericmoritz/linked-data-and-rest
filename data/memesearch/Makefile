all: index.json

deps:
	pip install -r requirements.txt

clean:
	rm index.json

index.json:
	python convert_rdf.py index.ttl turtle json-ld | python frame_jsonld.py ./index.frame.json > index.json

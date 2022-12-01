SHELL:= /bin/bash

# install:
# 	# unnecessary if you build docker image to run
# 	pip install -r requirements.txt

build:
	# run twice to get wtc setup
	jupyter lite build && \
	jupyter lite build

# docker:
# 	docker build --pull \
# 		-t "jupyterlite" -f Dockerfile .

# port%:
# 	docker run --rm -it -p$*:8888 -v "$$(pwd)":/home/jovyan/work jupyterlite

clean:
	rm -rf _output .jupyterlite.doit.db

page:
	ghp-import -nfp _output

modules := clean docker port build page

.PHONY: $(modules)
SHELL:= /bin/bash
# Registry for docker images
REGISTRY=localhost:32000
# REGISTRY=chungc
# version for tagging image for deployment
VERSION=0.0.2

push-%:
	docker tag "$*" "${REGISTRY}/$*:${VERSION}"
	docker push "${REGISTRY}/$*:${VERSION}"

# Scipy notebook with GPU support (Nvidia CUDA)
scipy-nv:
	docker build \
		--pull \
		--build-arg ROOT_CONTAINER="nvidia/cuda:11.2.2-cudnn8-runtime-ubuntu20.04" \
		--build-arg PYTHON_VERSION="3.9" \
		-t "base-notebook-nv" docker-stacks/base-notebook
	docker build \
		--build-arg BASE_CONTAINER="base-notebook-nv" \
		-t "minimal-notebook-nv" docker-stacks/minimal-notebook
	docker build \
		--build-arg BASE_CONTAINER="minimal-notebook-nv" \
		-t "scipy-nv" docker-stacks/scipy-notebook

# Support different programming languages in addition to python such as
# C++, Java, SQL, javascript, typescript, ...
programming:
	docker build \
		-t "programming" -f programming/Dockerfile .
	docker run --rm -it  -p 8888:8888/tcp -v "$$(pwd)/programming/examples":/home/jovyan/work programming

# Support different interfaces such as
# VSCode, remote desktop, retrolab, ...
jupyter-interface:
	docker build --pull \
		-t "jupyter-interface" -f jupyter-interface/Dockerfile .
	docker run --rm -it  -p 8888:8888/tcp -v "$$(pwd)/jupyter-interface/examples":/home/jovyan/work jupyter-interface

# Tools for mathematics
math:
	docker build --pull \
		-t "math" -f math/Dockerfile .
	docker run --rm -it  -p 8888:8888/tcp math

cs1302nb: scipy-10
	base=scipy-10; i=0; \
	for module in jupyter-interface programming math grading dev; \
	do \
	stage="cs1302nb$$((++i))_$$module"; \
	docker build --build-arg BASE_CONTAINER="$$base" \
		-t "$$stage" -f "$$module/Dockerfile" .; \
	base="$$stage"; \
	done; \
	docker tag "$$stage" cs1302nb
	docker run --rm -it  -p 8888:8888/tcp cs1302nb

cs1302hub: cds
	base=scipy-cds; i=0; \
	for module in jupyter-interface programming math grading dev; \
	do \
	stage="cs1302$$((++i))_$$module"; \
	docker build --build-arg BASE_CONTAINER="$$base" \
		-t "$$stage" -f "$$module/Dockerfile" .; \
	base="$$stage"; \
	done; \
	docker tag "$$stage" cs1302
	docker run --rm -it  -p 8888:8888/tcp cs1302

cds:
	docker build \
		-t "cds" -f cds/Dockerfile .
	# docker run --rm -it  -p 8888:8888/tcp -v "$$(pwd)/cds":/home/jovyan/work cds bash
	# jupyterhub --config /home/jovyan/work/config.py

scipy-10:
	docker build \
		--build-arg PYTHON_VERSION="3.10" \
		-t "base-notebook-10" docker-stacks/base-notebook
	docker build \
		--build-arg BASE_CONTAINER="base-notebook-10" \
		-t "minimal-notebook-10" docker-stacks/minimal-notebook
	docker build \
		--build-arg BASE_CONTAINER="minimal-notebook-10" \
		-t "scipy-10" docker-stacks/scipy-notebook


modules := cs1302nb cs1302hub main cds scipy-nv scipy-10 programming divedeep jupyter-interface math datamining classic push

.PHONY: $(modules)
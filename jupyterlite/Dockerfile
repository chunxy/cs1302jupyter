ARG BASE_CONTAINER=jupyter/scipy-notebook

FROM ${BASE_CONTAINER}

USER ${NB_USER}

COPY --chown=${NB_UID}:${NB_GID} requirements.txt requirements.txt

RUN pip install --quiet --no-cache-dir \
    -r requirements.txt && \
    fix-permissions "${CONDA_DIR}"
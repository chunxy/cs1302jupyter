ARG BASE_CONTAINER=jupyter/scipy-notebook

FROM ${BASE_CONTAINER}

USER ${NB_USER}

# Programming languages frontends
RUN mamba install --quiet --yes \
    'ghp-import' && \
    pip install --quiet --no-cache-dir \
    'jupyterlite==0.1.0b12' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}"
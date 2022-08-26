ARG BASE_CONTAINER=jupyterhub/k8s-hub:1.2.0

FROM ${BASE_CONTAINER}

ARG CDSVERSION=0.6.2

USER root

RUN python3 -m pip install --upgrade cdsdashboards>=$CDSVERSION

RUN userdel jovyan


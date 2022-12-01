FROM jupyterhub/k8s-hub:1.2.0

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"

USER root

# For LDAP & RADIUS
RUN apt-get update && \
    apt-get upgrade --yes && \
    apt-get install --yes --no-install-recommends \
    libnss-ldap \
    libpam-ldap \
    libpam-radius-auth \
    ldap-utils \
    sudo \
    && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN echo "${NB_USER}  ALL=(ALL) NOPASSWD: $(which mkhomedir_helper)" >> /etc/sudoers.d/nbuser_mkhomedir
RUN python3 -m pip install --upgrade cdsdashboards>=0.6.2

COPY etc/ldap.conf /etc/ldap.conf
COPY etc/nsswitch.conf /etc/nsswitch.conf
COPY etc/pam_radius_auth.conf /etc/pam_radius_auth.conf
COPY etc/pam.d /etc/pam.d

USER jovyan


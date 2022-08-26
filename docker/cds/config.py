c.ConfigurableHTTPProxy.command = '/usr/local/bin/configurable-http-proxy'

from cdsdashboards.hubextension import cds_extra_handlers
c.JupyterHub.extra_handlers = cds_extra_handlers

from cdsdashboards.app import CDS_TEMPLATE_PATHS
c.JupyterHub.template_paths = CDS_TEMPLATE_PATHS

c.JupyterHub.spawner_class = 'cdsdashboards.hubextension.spawners.variablekube.VariableKubeSpawner'
c.CDSDashboardsConfig.builder_class = 'cdsdashboards.builder.kubebuilder.KubeBuilder'
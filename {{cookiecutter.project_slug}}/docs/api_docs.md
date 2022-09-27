# API documentation

{% if cookiecutter.service_or_package == 'package' -%}
:::{{ cookiecutter.package_name }}
{%- endif -%}
{% if cookiecutter.service_or_package == 'service' -%}
:::src
:::src.main
{%- endif -%}

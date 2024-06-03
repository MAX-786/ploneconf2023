# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Plone Foundation <collective@plone.org>" \
      org.label-schema.name="ploneconf2023-varnish" \
      org.label-schema.description="Plone Conference Training Varnish image." \
      org.label-schema.vendor="Plone Foundation"

COPY etc/varnish.vcl /etc/varnish/default.vcl

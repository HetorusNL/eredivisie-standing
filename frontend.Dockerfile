# use the caddy image as base to host the frontend
FROM caddy

# add the frontend to the caddy srv/ directory
ADD frontend/ /srv/frontend
# add the Caddyfile for the frontend
COPY gha/Caddyfile /etc/caddy/Caddyfile

# add/update the container labels
ARG VCS_REF
LABEL org.label-schema.vcs-ref="${VCS_REF}"
LABEL org.label-schema.vcs-url=https://github.com/HetorusNL/eredivisie-standing
LABEL org.opencontainers.image.authors=tim@hetorus.nl
LABEL org.opencontainers.image.source=https://github.com/HetorusNL/eredivisie-standing
LABEL org.opencontainers.image.description="Repository to show a table with scores for predictions of the standing in the eredivisie"
LABEL org.opencontainers.image.licenses=MIT

# take the base image of python
FROM python:3.13-alpine

# add the uv and uvx binaries
COPY --from=ghcr.io/astral-sh/uv:0.8.2 /uv /uvx /bin/

# add the api file to the docker
ADD api/ /app

# add the workdir
WORKDIR /app

# sync the project, make sure everything is installed
RUN uv sync --locked

# start the project by running main.py
CMD ["uv", "run", "python", "main.py"]

# add/update the container labels
ARG VCS_REF
LABEL org.label-schema.vcs-ref="${VCS_REF}"
LABEL org.label-schema.vcs-url=https://github.com/HetorusNL/eredivisie-standing
LABEL org.opencontainers.image.authors=tim@hetorus.nl
LABEL org.opencontainers.image.source=https://github.com/HetorusNL/eredivisie-standing
LABEL org.opencontainers.image.description="Repository to show a table with scores for predictions of the standing in the eredivisie"
LABEL org.opencontainers.image.licenses=MIT

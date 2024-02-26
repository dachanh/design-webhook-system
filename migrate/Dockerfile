FROM golang:1.22.0-alpine

# Install tools required for project
# Run `docker build --no-cache .` to update dependencies
RUN echo "Installing system dependencies.." && \
      apk update && \
      apk add bash make && \
    echo "Cleanups.." && \
      rm -rf /var/cache/apk/*

ENV ROOT /migrate

WORKDIR $ROOT
COPY Makefile ./

RUN make install

COPY run.sh ./

RUN chmod a+x /migrate/run.sh

CMD ["bash", "/migrate/run.sh"]
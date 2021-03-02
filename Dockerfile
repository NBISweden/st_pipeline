FROM continuumio/miniconda3:4.9.2

LABEL maintainer="John Sundh" email=john.sundh@nbis.se
LABEL description="Docker image for STpipeline"

# Use bash as shell
SHELL ["/bin/bash", "-c"]

# Set workdir
WORKDIR /analysis

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl gcc libc6-dev && apt-get clean

# Add environment file
COPY environment.yml .

# Install environment into base
RUN conda env update -n base -f environment.yml && conda clean -a

# Install pipeline
COPY MANIFEST.in setup* requirements.txt ./
COPY stpipeline stpipeline
COPY scripts scripts
RUN python setup.py build && python setup.py clean --all install
# Run tests
COPY tests tests
COPY testrun.py .
RUN python setup.py test

ENTRYPOINT ["st_pipeline_run.py"]
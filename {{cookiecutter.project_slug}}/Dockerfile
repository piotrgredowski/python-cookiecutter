FROM python:{{cookiecutter.python_version}}-slim-buster

RUN apt-get update && apt-get install -y build-essential unzip wget python-dev

# Clean apt-get
RUN apt-get clean -y

# Install poetry
RUN pip install "poetry=={{cookiecutter.poetry_version}}"
# Install python requirements
RUN poetry export --format requirements.txt --output requirements.txt --without-hashes  | /venv/bin/pip install -r /dev/stdin

RUN groupadd --gid 1000 runner \
    && useradd --uid 1000 --gid runner --shell /bin/bash --create-home runner

COPY . /home/runner/app
WORKDIR /home/runner/app

CMD [ "python", "-m", "src.main" ]

FROM python:3.9.2-alpine

COPY . /code

WORKDIR /code

RUN  pip install --upgrade pip && \
  python3 -m pip install --upgrade setuptools && \
  apk add --no-cache \
      python3-dev \
      cargo \
      openssl-dev  \
      libc-dev \
      gcc \
      libressl-dev \
      musl-dev \
      libffi-dev && \
    pip install --no-cache-dir --upgrade -r requirements.txt  && \
    apk del \
      libressl-dev \
      musl-dev \
      libffi-dev \
      cargo \
      openssl-dev \
      python3-dev
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
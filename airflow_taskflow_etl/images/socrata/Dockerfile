FROM python:3.9.10-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY scripts/get_metadata.py /usr/local/bin/get_metadata
RUN chmod +x /usr/local/bin/get_metadata

ENTRYPOINT ["/usr/local/bin/get_metadata"]

CMD ["--help"]
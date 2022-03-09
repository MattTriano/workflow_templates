FROM python:3.9.10-slim

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

USER app_user

COPY . .

CMD ["bash"]
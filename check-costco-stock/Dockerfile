FROM python:slim

WORKDIR /app

RUN python3 -m venv venv
RUN . venv/bin/activate

RUN pip install requests

COPY costco.py .

# Install the say command
RUN apt-get update
RUN apt-get install gnustep-gui-runtime -y

CMD [ "python", "costco.py"]

FROM python:rc-alpine

LABEL author="Jonathan Nisell jnisell@gmail.com"

WORKDIR /usr/src/app
RUN pip install flask

COPY app.py ./

CMD ["python"] ["./app.py"]
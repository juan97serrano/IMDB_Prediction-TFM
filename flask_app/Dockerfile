FROM python:3.8
WORKDIR /flask_app
ADD . /flask_app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]

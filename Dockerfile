FROM python:3-onbuild
COPY . /app
EXPOSE 5000
CMD python ./api.py

# FROM python:3-onbuild
# RUN mkdir -p /deploy/app
# COPY requirements.txt /deploy/

# RUN pip install -r /deploy/requirements.txt
# WORKDIR /deploy/app
# COPY . /deploy/
# EXPOSE 5000
# CMD python ./api.py
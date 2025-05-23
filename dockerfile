FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3.12
RUN apt-get install -y python3-pip
RUN pip3 install flask
RUN pip3 install matplotlib
RUN pip3 install psutil
WORKDIR /
COPY app.py .
EXPOSE 5000
CMD ["flask", "--app", "app.py","run", "--host","0.0.0.0", "--debug"]
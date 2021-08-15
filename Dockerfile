#  UBUNTU
FROM ubuntu:20.04    
LABEL description = "Desarrollo Web: IDGS-81"  
LABEL mainteiner = "Carmen Kaplan"  
LABEL version = "0.1"    

#  PYTHON
RUN apt-get update
RUN apt install -y python3
RUN apt install -y python3-pip 

#  LIBRERIAS
RUN pip3 install web.py
RUN pip3 install pyrebase
RUN pip3 install simplejson
RUN pip3 install requests
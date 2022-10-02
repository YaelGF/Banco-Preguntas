FROM ubuntu:20.04 
 
RUN apt-get update 
RUN apt-get install -y 
RUN apt-get install python3 -y 
RUN apt-get install python3-pip -y 
RUN apt-get install sqlite3 -y 
RUN pip3 install web.py



ENV requiremets.txt /home/requiremets.txt 
 
COPY requiremets.txt ${requiremets} 
RUN pip3 install -r requiremets.txt 


WORKDIR /home/git/backend





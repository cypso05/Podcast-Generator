# a docker file controls how your cloud server creates a virtual machine in the cloud. below are steps for making virtual machine 
FROM  ubuntu : latest

RUN apt-get update && apt-get install -y \
    python3.10 \ 
    python3-pip \
    git

RUN pip3 imstall PyYAML

COPY feed.py /usr/bin/feed.py 

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

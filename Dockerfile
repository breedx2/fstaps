# FlightStats taps Server
# https://github.com/alexwitherspoon/fstaps
FROM alexwitherspoon/debian

MAINTAINER Alex Witherspoon <alex@alexwitherspoon.com>

# Network Ports Used by App
EXPOSE 80
EXPOSE 22

# Commands to Stage OS
RUN echo "Updating OS" && \
    bash -c "apt-get update -qq" && \
    bash -c "apt-get upgrade -qq --force-yes" && \
    echo "OS Updated, installing software" && \
    echo "...."

RUN echo "Installing Base Utilties" && \
    bash -c "apt-get update -qq" && \
    bash -c "apt-get install -qq --force-yes build-essential nano ssh" && \
    bash -c "echo 'root:beer' | chpasswd" && \
    echo "Base Utilities Installed" && \
    echo "...."

# Commands to Stage App
RUN echo "Installing git" && \
    bash -c "apt-get install -qq --force-yes git" && \
    echo "git Installed" && \
    echo "...."
    
RUN echo "Installing python" && \
    bash -c "apt-get install -qq --force-yes build-essential python2.7 python2.7-dev python-pip" && \
    bash -c "pip install -U pip" && \
    bash -c "pip install virtualenv" && \
    echo "python Installed" && \
    echo "...."
    
RUN echo "Installing fstaps App" && \
    bash -c "git clone https://github.com/alexwitherspoon/fstaps.git /opt/fstaps" && \
    bash -c "cd /opt/fstaps && virtualenv --no-site-packages env" && \
    bash -c "cd /opt/fstaps && source env/bin/activate && easy_install flask PyYAML inflect" && \
    echo "fstaps Installed" && \
    echo "...."

# Commands to Run App
CMD bash -c "/etc/init.d/ssh start" && \
    bash -c "cd /opt/fstaps && source env/bin/activate && python fstaps.py" && \
    bash -c "sleep 80085d"

install docker on vps :
=========>

apt install -y apt-transport-https ca-certificates curl software-properties-common && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && apt update && apt install -y docker-ce docker-ce-cli containerd.io && usermod -aG docker $USER && service docker restart

vps docker method 1 :

1. wget https://raw.githubusercontent.com/cihuuy/docker-wine/master/docker-wine && chmod +x docker-wine && ./docker-wine --rdp
2. connect vps with ngrok
    wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz && tar -xf ngrok-v3-stable-linux-amd64.tgz && ./ngrok config add-authtoken 2ac8pfkG32hq6EzIboK3kQ2v8Ej_68k6bH7G4jFNQFjY7RFT8 && ./ngrok tcp 3389
   
==========>
Login Docker : zg212 : ADang_999
 1. docker pull zg212/winerdp:v1
 2. docker run -d --name windeep zg212/winerdp:v1 --rdp=start
 3. connect vps with ngrok
    wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz && tar -xf ngrok-v3-stable-linux-amd64.tgz && ./ngrok config add-authtoken 2ac8pfkG32hq6EzIboK3kQ2v8Ej_68k6bH7G4jFNQFjY7RFT8 && ./ngrok tcp 3389
 4. run rdp windeep
 5. 


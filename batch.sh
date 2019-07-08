#batch file for quick start up

sudo apt-get update && sudo apt-get dist-upgrade -y

#install node-red
sudo sudo apt-get install build-essential -y
bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
sudo systemctl enable nodered.service
node-red-stop

cd
cd $HOME/pi/.node-red/
npm install -g node-red-admin
npm install node-red-dashboard
npm install node-red-contrib-mqtt-broker

#install webmin
sudo apt-get install perl libnet-ssleay-perl openssl libauthen-pam-perl libpam-runtime libio-pty-perl apt-show-versions python -y
wget http://prdownloads.sourceforge.net/webadmin/webmin_1.920_all.deb
sudo dpkg --install webmin_1.920_all.deb

#install tools
sudo apt-get install nmap tmux hwmon -y

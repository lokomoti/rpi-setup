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
sudo apt-get install nmap tmux -y

#install openCV4
sudo apt-get install build-essential cmake unzip pkg-config -y
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev -y
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
sudo apt-get install libxvidcore-dev libx264-dev -y
sudo apt-get install libgtk-3-dev -y
sudo apt-get install libcanberra-gtk* -y
sudo apt-get install libatlas-base-dev gfortran -y
sudo apt-get install python3-dev -y

cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip 

unzip opencv.zip
unzip opencv_contrib.zip

mv opencv-4.0.0 opencv
mv opencv_contrib-4.0.0 opencv_contrib

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

# raspberry AP setup
wget -q https://git.io/voEUQ -O /tmp/raspap && bash /tmp/raspap

sudo service network-manager stop
sudo ifconfig wlp5s0 down
sudo iwconfig wlp5s0 mode ad-hoc 
sudo iwconfig wlp5s0 channel 1
sudo iwconfig wlp5s0 essid 'fermi'
sudo iwconfig wlp5s0 key 1234567890
sudo ifconfig wlp5s0 192.168.1.4


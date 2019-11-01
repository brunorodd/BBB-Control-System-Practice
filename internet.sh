#run this is a root

route add default gw 192.168.7.1
route -n

echo "nameserver 8.8.8.8" > /etc/resolv.conf

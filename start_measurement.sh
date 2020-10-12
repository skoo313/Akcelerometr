sudo service grafana-server start

#   gnome-terminal --tab -t "BD" -e influx

gnome-terminal --tab -t "Server" -e "python3 server.py" 

sleep 5

gnome-terminal --tab -t "Client" -e "python3 client.py"

google-chrome --start-fullscreen --app="http://localhost:3000/d/oWbq1XvMz/akcelerometr?orgId=1&refresh=1s&var-nazwa=2020-09-17X13:11:16"
#chromium-browser --start-fullscreen --app="http://localhost:3000/d/oWbq1XvMz/akcelerometr?orgId=1&refresh=1s&from=now-40s&to=now&kiosk"

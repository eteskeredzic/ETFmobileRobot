#!/bin/bash

sudo chmod 777 lidar.sh
chmod 777 tutorial.sh
chmod 777 nav.sh
chmod 777 se_controller.sh
chmod 777 motoController.sh

read -p "Press [Enter] key to start..."
gnome-terminal -x sh -c "./lidar.sh; bash" 

read -p "Press [Enter] key to start..."
gnome-terminal -x sh -c "./tutorial.sh; bash"

read -p "Press [Enter] key to start..."
gnome-terminal -x sh -c "./nav.sh; bash"

read -p "Press [Enter] key to start..."
gnome-terminal -x sh -c "./se_controller.sh; bash"

read -p "Press [Enter] key to GET READY TO RUMBLEEEEEE..."
gnome-terminal -x sh -c "./motoController.sh; bash"


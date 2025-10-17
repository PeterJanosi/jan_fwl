# jan_fwl

Ez a ROS 2 package két node-ot tartalmaz:

- **temp_sensor_node**: Szimulált hőmérséklet értékeket generál (20.0–40.0 °C között), és elküldi a `temperature` nevű topicra.
- **alert_node**: Figyeli a `temperature` topicot, és ha az érték meghaladja a 30.0 °C-ot, akkor egy riasztást publikál `temperature_alert` topicon.

## Követelmények

- ROS 2 Humble
- Python 3
- A `sensor_msgs` és `std_msgs` csomagok

## Telepítés és build

```bash
cd ~/ros2_ws/src
git clone <a_te_repo_linked_ide>
cd ~/ros2_ws
colcon build --packages-select jan_fwl
source install/setup.bash

# Terminál 1 - Temperature szenzor node
ros2 run jan_fwl temp_sensor_node

# Terminál 2 - Alert node
ros2 run jan_fwl alert_node
# VAGY launch fájllal együtt:

ros2 launch jan_fwl monitor.launch.py

A launch fájl a launch/monitor.launch.py útvonalon található, és a következő node-okat indítja:

temp_sensor_node (név: temp_sensor)

alert_node
| Node             | Topic                | Típus                         | I/O          |
| ---------------- | -------------------- | ----------------------------- | ------------ |
| temp_sensor_node | `/temperature`       | `sensor_msgs/msg/Temperature` | Publikál     |
| alert_node       | `/temperature`       | `sensor_msgs/msg/Temperature` | Feliratkozik |
| alert_node       | `/temperature_alert` | `std_msgs/msg/String`         | Publikál     |

graph TD
    temp_sensor_node["temp_sensor_node"]
    alert_node["alert_node"]
    
    temp_sensor_node -->|sensor_msgs/Temperature| temperature((/temperature))
    temperature --> alert_node
    alert_node -->|std_msgs/String| temperature_alert((/temperature_alert))
[INFO] [temp_sensor_node]: Published temperature: 33.21 °C
[WARN] [alert_node]: ⚠️ High temperature alert: 33.21 °C

Név: [Jánosi Péter]

Neptun: [FWLFEQ]

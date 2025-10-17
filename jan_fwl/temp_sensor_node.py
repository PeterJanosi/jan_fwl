import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature
import random

class TempSensorNode(Node):
    def __init__(self):
        super().__init__('temp_sensor_node')
        self.publisher_ = self.create_publisher(Temperature, 'temperature', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)
        self.get_logger().info('Temperature sensor node started.')

    def publish_temperature(self):
        msg = Temperature()
        msg.temperature = random.uniform(20.0, 40.0)
        msg.variance = 0.1
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published temperature: {msg.temperature:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = TempSensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

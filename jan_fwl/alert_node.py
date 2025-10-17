import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature
from std_msgs.msg import String

class AlertNode(Node):
    def __init__(self):
        super().__init__('alert_node')
        self.subscription = self.create_subscription(
            Temperature, 'temperature', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'temperature_alert', 10)
        self.get_logger().info('Alert node started.')

    def listener_callback(self, msg):
        if msg.temperature > 30.0:
            alert_msg = String()
            alert_msg.data = f'⚠️ High temperature alert: {msg.temperature:.2f} °C'
            self.publisher_.publish(alert_msg)
            self.get_logger().warn(alert_msg.data)
        else:
            self.get_logger().info(f'Temperature normal: {msg.temperature:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = AlertNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

import rclpy
import numpy as np

from rclpy.node import Node
from std_msgs.msg import Float32MultiArray


class VectorPublisher(Node):

    def __init__(self):
        super().__init__('vector_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'bearing_vector', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
        # Bearing vector to publish
        vec = list(np.random.uniform(low=-1.0, high=1.0, size=3))

        # Formatting msg
        msg = Float32MultiArray()
        msg.data = vec

        # Publishing
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing vector "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    vector_publisher = VectorPublisher()
    rclpy.spin(vector_publisher)

    vector_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

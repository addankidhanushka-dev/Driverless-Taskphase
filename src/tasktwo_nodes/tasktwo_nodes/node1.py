#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from tasktwo_interfaces.msg import RT2String

class Node1Publisher(Node):

    def __init__(self):
        super().__init__("node1")
        self.publisher_ = self.create_publisher(RT2String, "topic1_input", 10)
        self.timer = self.create_timer(2.0, self.publish_string)

    def publish_string(self):
        user_input = input("Enter a string: ")

        msg = RT2String()
        msg.data = user_input

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Node1Publisher()
    rclpy.spin(node)
    rclpy.shutdown()


    


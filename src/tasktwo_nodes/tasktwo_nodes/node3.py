#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from tasktwo_interfaces.msg import PalindromeResult
from tasktwo_interfaces.msg import PalindromeResponse

class Node3Responder(Node):
    def __init__(self):
        super().__init__("node3_responder")

        self.sub_result = self.create_subscription(
            PalindromeResult, "topic2_result", self.result_callback, 10)
        self.pub_response = self.create_publisher(PalindromeResponse, "topic3_response", 10)

    def result_callback(self, msg):
        
        response_msg = PalindromeResponse()
        
        if msg.is_palindrome:
            response_msg.response = "Yes"
        else:
            response_msg.response = "No"

        self.pub_response.publish(response_msg)
        self.get_logger().info(f"Sent response: {response_msg.response}")

    
def main(args=None):
    rclpy.init(args=args)
    node = Node3Responder()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
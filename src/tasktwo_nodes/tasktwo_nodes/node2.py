#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from tasktwo_interfaces.msg import RT2String
from tasktwo_interfaces.msg import PalindromeResult
from tasktwo_interfaces.msg import PalindromeResponse


class Node2Processor(Node):
    def __init__(self):
        super().__init__("node2_processor")

        self.sub_input = self.create_subscription(RT2String, "topic1_input", self.input_callback, 10)
        self.pub_result = self.create_publisher(PalindromeResult, "topic2_result", 10)
        self.sub_response = self.create_subscription(
            PalindromeResponse, "topic3_response", self.response_callback, 10)


    def input_callback(self, msg):
        text = msg.data
        is_palindrome = (text==text[::-1])

        result = PalindromeResult()
        result.is_palindrome = is_palindrome
        self.pub_result.publish(result)

        self.get_logger().info(f"Received: {text}")

    def response_callback(self, msg):
        self.get_logger().info(f"Final answer from Node3: {msg.response}")


def main(args=None):
    rclpy.init(args=args)
    node = Node2Processor()
    rclpy.spin(node)
    rclpy.shutdown()


#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from taskone_msgs.msg import TaskOne

class TaskOnePublisher(Node):
    def __init__(self):
        super().__init__("taskone_publisher")
        self.publisher_ = self.create_publisher(TaskOne, "/taskone", 10)
        self.timer = self.create_timer(2.0, self.publish_data)

    def publish_data(self):
        msg = TaskOne()

        try:
            ang_vel = float(input("Enter angular velocity: "))
            radius = float(input("Enter radius: "))
        except:
            self.get_logger().info("Invalid input")
            return
        msg.ang_vel = ang_vel
        msg.radius = radius

        self.publisher_.publish(msg)
        self.get_logger().info(f"Published {msg.ang_vel}, {msg.radius}")

    
def main(args=None):
    rclpy.init(args=args)
    node = TaskOnePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =='__main__':
    main()

                    
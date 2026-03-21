#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from taskone_msgs.msg import TaskOne


class TaskOneSubscriber(Node):

    def __init__(self):
        super().__init__('taskone_subscriber')
        self.subscription = self.create_subscription(
            TaskOne,
            '/taskone',
            self.callback,
            10
        )

    def callback(self, msg):
        speed = msg.ang_vel * msg.radius
        self.get_logger().info(f"Speed: {speed}")


def main(args=None):
    rclpy.init(args=args)
    node = TaskOneSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
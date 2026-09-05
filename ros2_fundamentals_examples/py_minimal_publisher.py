#! /usr/bin/env python3

"""
Description : 
    This ROS2 node periodically publishes "Hello World" messgaes to topic.

------
Publishing Topics: 
    The channel containing the hello world messages
    /py_example_topic - std_msgs/string

Subscription Topics:
    None
------
Author: Arjun Mohandas
Date:25.08.2026
"""
import rclpy # Import the ros2 client library from python
from rclpy.node import Node # Import node class,used for creating nodes

from std_msgs.msg import String # Import string message type ros2

class MinimalPyPublisher(Node):
    """
    Create a minimal publisher node.
    """

    def __init__(self):
        """
        Create a custom node class for publishing messages
        """
        #initialize the node with a name
        super().__init__('minimal_py_publisher')

        #create a publisher on the topic with a queue size of 10 messages

        self.publisher_1=self.create_publisher(String, '/py_example_topic',10)

        #create a timer with a period of 0.5 sec to trigger pubishing of messages
        timer_period = 0.5
        self.timer = self.create_timer(timer_period,self.timer_callback)

        #Initialize a counter variable for message content
        self.i=0

    def timer_callback(self):
        """
        Callback function executed periodically by timer
        """
        # create a new string message object
        msg=String()

        # set the message data with counter
        msg.data='Hello World: %d' % self.i

        #Publish the message the i created about the topic

        self.publisher_1.publish(msg)

        #Log a message indicating that the message has been published
        self.get_logger().info('Publishing: "%s"' % msg.data)

        self.i=self.i + 1

def main(args=None):
    """
    Main Function to start ros 2 node

    Args:
        args(List,optinal): command-line arguments.Default to none.
    """
    rclpy.init(args=args)

    #create an instance of the Minimal publisher node
    minimal_py_publisher=MinimalPyPublisher()

    rclpy.spin(minimal_py_publisher)

    # Destroy the node explicitly

    minimal_py_publisher.destroy_node()

    #shutdown ros2 communication
    rclpy.shutdown()

if __name__ == '__main__':
    #Execute the main fuction if the script is run directly
    main()
#!/usr/bin/env python3

"""
Test Suite for the ROS2 minimal publisher node.

This script contains unit tests for verifying the functionality of a minimal ros2 publisher.
It t3ests the node creation,message counter increment and message content formatting.

------
Subscription topics:
    None
------

Publishing topics:

    /py_example_topic (std_msgs/String): Example messages with increment counter.

:author: Arjun
:date: 05/09/2026

"""

import pytest
import rclpy
from std_msgs.msg import String
from ros2_fundamentals_examples.py_minimal_publisher import MinimalPyPublisher


def test_publisher_creation():
    """
    To test if the publisher node is created correctly.

    This test verifies: 
    1. The node name is set correctly.
    2.The publisher object exists.
    3.The topic name is correct.

    :raises:Assertion error if any of the checks fail.
    """

    # Initialize ros2 communication

    rclpy.init()

    try:
        #create instance of our publisher node
        node = MinimalPyPublisher()

        # Test 1: Verify the node has the expected name
        assert node.get_name() == "minimal_py_publisher"

        #Test 2 : Vertify the publisher exists and has the correct topic name

        assert hasattr(node,'publisher_1')
        assert node.publisher_1.topic_name == '/py_example_topic'

    finally:
        #clean up ros2 communication
        rclpy.shutdown()

def test_message_counter():
    """
    Test if the message counter increments correctly.

    This test verifies that the counter (node.i) increases by 1 after each timer callback execution.

     :raises:Assertion error if the counter doesnt increment properly.
    """
    rclpy.init()

    try:
        node = MinimalPyPublisher()
        initial_count = node.i
        node.timer_callback()
        assert node.i == initial_count + 1
    finally:
        rclpy.shutdown()

def test_message_content():
    """
    Test if the message content is fortmatted correctly.

    This test verifies that the message string is properly formatted using an f-string with the current counter value.
    :raises:Assertion error if the message format doesnt match the exmected output.

    """
    rclpy.init()
    
    try:
        node = MinimalPyPublisher()

        # Set counter to a know value for testing
        node.i = 5
        msg = String()

        # Using f-string instead of % formatting
        msg.data = f'Hello World: {node.i}'
        assert msg.data == 'Hello World: 5'

    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    pytest.main(['-v'])

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WarehouseEavesdropper(Node):
    def __init__(self):
        super().__init__('warehouse_eavesdropper')          # Node name

        # Create subscriber: topic_name, message_type, callback_function
        self.subscription = self.create_subscription(
            String,
            'hmi/unified_status',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard some warehouse gossip: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    warehouse_eavesdropper = WarehouseEavesdropper()
    rclpy.spin(warehouse_eavesdropper)
    warehouse_eavesdropper.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

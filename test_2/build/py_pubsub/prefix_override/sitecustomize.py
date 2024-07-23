import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ylo-laptop/ROS_Projects/test_2/install/py_pubsub'

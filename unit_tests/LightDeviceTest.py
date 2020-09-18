import unittest
from zenfinder.device import LightDevice

class LightDeviceTest(unittest.TestCase):

    def setUp(self):
        self.linear_device = LightDevice("00:0a:95:9d:68:16", "192.168.1.4", 8888, "test")
    
    def test_set_lightmap(self):
        self.linear_device.set_light_map(1, 5, [(0,2), (0,4)])
        self.assertEqual(self.linear_device.light_configuration, [[-1, -1, 0, -1, 1]])
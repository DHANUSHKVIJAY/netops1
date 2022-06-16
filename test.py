from app import app
import unittest

class FlaskTest(unittest.TestCase):

    def test_dash(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_all(self):
        tester = app.test_client(self)
        response = tester.get('/metricsall')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_srcipOutall_data(self):
        tester = app.test_client(self)
        response = tester.get('/metrics/srcipOutall')
        self.assertTrue(b'Number of Connections' in response.data)
        self.assertTrue(b'IP Address' in response.data)

    def test_dstipOutall_data(self):
        tester = app.test_client(self)
        response = tester.get('/metrics/dstipOutall')
        self.assertTrue(b'Number of Connections' in response.data)
        self.assertTrue(b'IP Address' in response.data)

    def test_srcportOutall_data(self):
        tester = app.test_client(self)
        response = tester.get('/metrics/srcportOutall')
        self.assertTrue(b'Number of Connections' in response.data)
        self.assertTrue(b'Port' in response.data)

    def test_dstportOutall_data(self):
        tester = app.test_client(self)
        response = tester.get('/metrics/dstportOutall')
        self.assertTrue(b'Number of Connections' in response.data)
        self.assertTrue(b'Port' in response.data)

    def test_protoOutall_data(self):
        tester = app.test_client(self)
        response = tester.get('/metrics/protoOutall')
        self.assertTrue(b'Number of Connections' in response.data)
        self.assertTrue(b'Protocol' in response.data)

    def test_policyOutall_data(self):
        tester = app.test_client(self)
        response = tester.get('/metrics/policyOutall')
        self.assertTrue(b'Number of Connections' in response.data)
        self.assertTrue(b'Policy' in response.data)

    def test_interfaceOutall_data(self):
        tester = app.test_client(self)
        response = tester.get('/metrics/interfaceOutall')
        self.assertTrue(b'Number of Connections' in response.data)
        self.assertTrue(b'Interface' in response.data)

    def test_packetsOutall_data(self):
        tester = app.test_client(self)
        response = tester.get('/metrics/packetsOutall')
        self.assertTrue(b'Source IP' in response.data)
        self.assertTrue(b'Destination IP' in response.data)
        self.assertTrue(b'Source Port' in response.data)
        self.assertTrue(b'Destination Port' in response.data)
        self.assertTrue(b'Packets' in response.data)

    def test_bytesOutall_data(self):
        tester = app.test_client(self)
        response = tester.get('/metrics/bytesOutall')
        self.assertTrue(b'Source IP' in response.data)
        self.assertTrue(b'Destination IP' in response.data)
        self.assertTrue(b'Source Port' in response.data)
        self.assertTrue(b'Destination Port' in response.data)
        self.assertTrue(b'Bytes' in response.data)
        
if __name__ == "__main__":
    unittest.main()
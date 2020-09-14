from aws_xray_sdk.core import xray_recorder

import app

xray_recorder.begin_segment("Test")


class TestApp:
    def test_helloworld(self):
        response = app.read_root()
        assert response == {"hello": "world"}

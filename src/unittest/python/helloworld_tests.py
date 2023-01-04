from mockito import mock, verify
import unittest

from helloworld import helloworld
from helloworld import rest

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        helloworld(out)

        verify(out).write("Hello world of Python\n")

    def test_rest(self):
        out = mock()

        rest(out)

        verify(out).write("200")

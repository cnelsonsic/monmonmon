#!/usr/bin/env python
# coding:utf-8
'''This test file ensures that everything works end-to-end.'''

import os
import json
import flask
import monmonmon
import unittest

class MonMonMonTestCase(unittest.TestCase):

    def setUp(self):
        monmonmon.metadata.bind = "sqlite:///:memory:"
        monmonmon.setup_all()
        monmonmon.create_all()
        monmonmon.app.config['TESTING'] = True
        self.app = monmonmon.app.test_client()


class UserAuthTestCase(MonMonMonTestCase):
    def test_register(self):
        rv = self.app.post('/users/register', data=dict(username="jimbob@example.com", password="password1"))
        self.assertIn('200', rv.status)

    def test_register_twice(self):
        rv = self.app.post('/users/register', data=dict(username="jimbob@example.com", password="password1"))
        self.assertIn('200', rv.status)
        rv = self.app.post('/users/register', data=dict(username="jimbob@example.com", password="password1"))
        self.assertIn('403', rv.status)

    def test_login(self):
        self.app.post('/users/register', data=dict(username="jimbob@example.com", password="password1"))
        rv = self.app.post('/users/login', data=dict(username="jimbob@example.com", password="password1"))
        self.assertIn('200', rv.status)
        self.assertIn('username', rv.headers['Set-Cookie'])


class StartBattleTestCase(MonMonMonTestCase):

    def test_start_battle(self):
        self.app.post('/users/register', data=dict(username="jimbob@example.com", password="password1"))
        self.app.post('/users/register', data=dict(username="enemy@example.com", password="password1"))
        self.app.post('/users/login', data=dict(username="jimbob@example.com", password="password1"))
        rv = self.app.post('/battle/start', data=dict(target='enemy@example.com'))
        self.assertIn('200', rv.status)
        result = json.loads(rv.data)
        self.assertIn('battle', result)
        self.assertEqual(result['battle'], 1)


if __name__ == '__main__':
    unittest.main()

# coding=utf-8
import unittest

from flask_script import Manager

from app import create_app

app = create_app()
manager = Manager(app)


@manager.command
def test():
    loader = unittest.TestLoader()
    tests = loader.discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
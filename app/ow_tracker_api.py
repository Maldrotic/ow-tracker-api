import os

from app import create_app


app_config_name = os.environ.get('FLASK_CONFIG', 'default')
app = create_app(app_config_name)


@app.cli.command()
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

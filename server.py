from waitress import serve
import logging
from mysite.wsgi import application
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)
if __name__ == '__main__':
    serve(application, port = '8080')


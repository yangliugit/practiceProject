import logging


logging.basicConfig(level=logging.INFO, filename='mylog.log')

logging.info('Starting program')
logging.info('Trying to divide 1 by 0')

try:

    print 1 / 0

except Exception as err:
    logging.info(err)
logging.info('The division succeeded')
logging.info('End program')

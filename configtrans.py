from ConfigParser import ConfigParser


CONFIGFILE = 'picongfig.txt'

config = ConfigParser()
config.read(CONFIGFILE)

print config.get('messages', 'greeting')

radius = input(config.get('messages', 'question') + ' ')

print config.get('messages', 'result_message')

print config.getfloat('numbers', 'pi') * radius ** 2


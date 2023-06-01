import logging as log


# Muestra los log de DEBUG, INFO o WARNING en adelante. El default es Warning
log.basicConfig(
    level=log.DEBUG,
    format='%(message)s',
    datefmt='%I:%M:%S %p',
    handlers=[
        log.FileHandler('Logger.log'),
        log.StreamHandler()
    ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel DEBUG')
    log.info('Mensaje a nivel INFO')
    log.warning('Mensaje a nivel WARNING')
    log.error('Mensaje a nivel ERROR')
    log.critical('Mensaje a nivel CRÍTICO')

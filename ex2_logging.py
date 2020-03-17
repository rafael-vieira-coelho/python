import logging

def main():
    logging.basicConfig(filename='info.log', level=logging.INFO)
    logging.info('Started')
    #...
    logging.info('Finished')

if __name__ == '__main__':
    main()

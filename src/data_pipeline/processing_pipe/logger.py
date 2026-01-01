import logging

logger = logging.getLogger(__name__)    # TO-DO improve logger configuration
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)-8s %(message)s', 
                    datefmt='%a, %d %b %Y %H:%M:%S', 
                    filename='src/data_pipeline/logs/pipeline.log', 
                    filemode='w')
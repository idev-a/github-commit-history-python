import logging as logger
import sys

# log_level = logging.DEBUG

# log_format = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s [in %(pathname)s:%(lineno)d]")
# logger = logging.getLogger('mas.log')                                  
# logger.setLevel(log_level)     

logger.basicConfig(
	filename='log.log',
	level=logger.INFO,
	format="%(asctime)s:%(levelname)s:%(message)s [in %(pathname)s:%(lineno)d]"
)                                  

# writing to stdout                                                     
# handler = logging.StreamHandler(sys.stdout)                             
# handler.setLevel(log_level)                                        
# handler.setFormatter(log_format)                                        
# logger.addHandler(handler)           
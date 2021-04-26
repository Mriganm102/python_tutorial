a = 'abcdefghijklmnopqrstuvwxyz'
print(set(a))
import reprlib
print(reprlib.repr(set(a)))
import pprint
listlist = [["Blue", "Green"], "Black",
            [["Red", "Yellow"]],
            "White"]
pprint.pprint(listlist)
print(listlist)

import logging
logging.debug("Debugging Information")
logging.info("Information Message")
logging.warning("Warning:config file %s not found", 'server.conf')
logging.error("Error Continued")
logging.critical("Critical error -- shutting down")

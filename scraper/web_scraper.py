from . import ca
from . import ky
from . import tn
from . import tx
from . import wa

def scrape_for_notices():
    tx.scrape_web_tx()
    return tn.scrape_web_TN()
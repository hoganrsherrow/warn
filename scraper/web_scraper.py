from . import ak
from . import al
from . import ca
from . import ky
from . import tn
from . import tx
from . import wa

def scrape_for_notices():
    data = []
    data.extend(ak.scrape_web_ak())
    return data
    # tx.scrape_web_tx()
    # return tn.scrape_web_TN()
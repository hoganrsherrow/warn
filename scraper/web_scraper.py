from . import ak
from . import al
from . import az
from . import ca
from . import co
from . import ct
from . import de
from . import fl
from . import ky
from . import tn
from . import tx
from . import wa

def scrape_for_notices():
    data = []
    data.extend(fl.scrape_web_fl())
    return data
    # tx.scrape_web_tx()
    # return tn.scrape_web_TN()
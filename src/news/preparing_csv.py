from get_notices import get_notice
import pandas as pd
from dotenv import load_dotenv
import os

api_key = os.getenv("API_KEY")

data = get_notice(api_key,"SPY", "financial","20160101T0130","20160401T0130")

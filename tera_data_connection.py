import datetime

import teradata
import time
import pandas as pd
def teradata_connector():

    start_time = (datetime.now().replace(microsecond=0))
    udaExec =teradata.UdaExec(appName= "test",version ="1.0", logConsole= False)

    with udaExec.connect(method = "odbc", system="" , username= " ",password ="",
                         driver ="Teradata Database ODBC Driver 17.00" ) as connect :

        print("Connected to Teradata DB.")

        query = "Select * from xyz"
        df_tera_lnd = pd.read_sql(query,connect)
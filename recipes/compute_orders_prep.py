# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
orders = dataiku.Dataset("orders")
orders_df = orders.get_dataframe()


# iets erbij

orders_prep_df = orders_df # For this sample code, simply copy input to output


# Write recipe outputs
orders_prep = dataiku.Dataset("orders_prep")
orders_prep.write_with_schema(orders_prep_df)

# Market data pull task
# Prototype for Python Data Pipelines course by kjam with modifications

from pandas_datareader import data

def get_stock_info(stock, start, end, source='yahoo'):
	df = data.DataReader(stock, source, start,end)
	df['Stock'] = stock
	agg = df.groupby('Stock').agg({
		'Open': ['min','max','mean','median'],
		'Adjust Close': ['min','max','mean','median'],
		'Close': ['min','max','mean','median'],
		'High': ['min','max','mean','median'],
		'Low': ['min','max','mean','median'],
	})
	agg.columns = [' '.join(col).strip() for col in agg.columns.values]  #readability
	return agg.to_json()  #return dataframe

# -30- End of task

'''Can test in REPL with
from task1 import get_stock_info
from datetime import dateime
res = get_stock_info('__ticker_symbol__', datetime(2017, 1, 1), datetime.today())
res
'''

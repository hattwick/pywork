# Market data pull task
# Prototype for Python Data Pipelines course by kjam with modifications
# this version adds celery decorator to the task

from pandas_datareader import data
from celeryapp1 import app

@app.task
def get_stock_info(stock, start, end, source='yahoo'):
	df = data.DataReader(stock, source, start,end)
	df['Stock'] = stock
	agg = df.groupby('Stock').agg({
		'Open': ['min','max','mean','median'],
		'Adj Close': ['min','max','mean','median'],
		'Close': ['min','max','mean','median'],
		'High': ['min','max','mean','median'],
		'Low': ['min','max','mean','median'],
	})
	agg.columns = [' '.join(col).strip() for col in agg.columns.values]  #readability
	return agg.to_json()  #return dataframe

# -30- End of task

'''Can test in REPL with celery worker process running a worker task using task2 and the following
>> worker setup: $ celery -A task2 worker --loglevel=INFO

>>task submission in REPL:
from task1 import get_stock_info
from datetime import dateime
res = get_stock_info.delay('__ticker_symbol__', datetime(2017, 1, 1), datetime.today())
or specify queue: res = get_stock_info.apply_async(('__ticker_symbol__', datetime(2017, 1, 1), datetime.today()), queue = 'priority')

>> results will appear in worker console or log
'''

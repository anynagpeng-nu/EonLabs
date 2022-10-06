import pandas as pd
import matplotlib.pyplot as plt

class Trends():
	def __init__(self):
		self.hourly = pd.read_csv('hourly_data.csv')
		self.weekly = pd.read_csv('weekly_data.csv')
		self.monthly = pd.read_csv('monthly_data.csv')

	def process(self):
		# convert object to datetime
		self.hourly['date'] = pd.to_datetime(self.hourly['date'])
		self.weekly['date'] = pd.to_datetime(self.weekly['date'])
		self.monthly['date'] = pd.to_datetime(self.monthly['date'])

		#merge
		self.hourly=self.hourly.merge(self.weekly,how='left', on='date')
		self.hourly=self.hourly.merge(self.monthly,how='left', on='date')

		#fillna
		self.hourly = self.hourly[['value_hour', 'date','value_week','value_month']]
		self.hourly = self.hourly.fillna(method='ffill')

		#rescale
		self.hourly['value_hour'] = self.hourly['value_hour']*self.hourly['value_week']*self.hourly['value_month']/10000

	def plot(self):
		plt.plot(self.hourly['date'], self.hourly['value_hour'],'-')
		plt.xlabel('Time')
		plt.ylabel('Counts')
		plt.savefig('hourly.jpg')

if __name__ == '__main__':
	trend = Trends()
	trend.process()
	trend.plot()






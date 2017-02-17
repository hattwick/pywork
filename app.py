# experimenting with nesting functions


def get_budget():
	budget_string = input("What is your allocation for this month: ")
	budget = int(budget_string)
	return budget

def day_of_month():
	day_string = input("What day of the month is today: ")
	day = int(day_string)
	return day

def burndown(budget, day):
	return budget - ((budget/30) * day)

def run():
	budget=get_budget()
	day=day_of_month()10
	print("You should have spent $".format(burndown(budget, day)))


run()

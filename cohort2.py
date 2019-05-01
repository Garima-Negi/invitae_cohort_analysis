import arrow
import sys

def analysis(start_date, end_date, customers_path, orders_path):
	print(f"Cohort: {start_date} - {end_date}")
	start_date = arrow.get(start_date, 'M/DD/YYYY')
	end_date = arrow.get(end_date, 'M/DD/YYYY')

	customers = {}
	with open(customers_path, 'r') as fh:
		next(fh)
		for line in fh:
			signup_date = arrow.get(line.split(',')[1], 'M/D/YY H:mm')
			if start_date < signup_date <= end_date:
				customers[line.split(',')[0]] = signup_date

	print(f"Customers: {len(customers)}")

	num_customers_week_1 = 0
	num_customers_week_2 = 0
	num_customers_week_2_first = 0
	num_customers_week_3 = 0
	num_customers_week_3_first = 0
	customers_already_ordered = []

	with open(orders_path, 'r') as fh:
		next(fh)
		for line in fh:
			customer_id = line.split(',')[2]
			if customer_id in customers:
				order_date = arrow.get(line.split(',')[3], 'YYYY-MM-DD HH:mm:ss')
				if customers[customer_id] < order_date < customers[customer_id].shift(days=+7):
					num_customers_week_1 += 1
					customers_already_ordered.append(customer_id)

				if customers[customer_id].shift(days=+7) < order_date < customers[customer_id].shift(days=+14):
					num_customers_week_2 += 1
					if customer_id not in customers_already_ordered:
						num_customers_week_2_first += 1
						customers_already_ordered.append(customer_id)
					
				if customers[customer_id].shift(days=+14) < order_date < customers[customer_id].shift(days=+21):
					num_customers_week_3 += 1
					if customer_id not in customers_already_ordered:
						num_customers_week_3_first += 1
						#customers_already_ordered.append(customer_id)
					

	pct_customers_week_1 = (num_customers_week_1 / len(customers)) * 100.0
	pct_customers_week_2 = (num_customers_week_2 / len(customers)) * 100.0
	pct_customers_week_2_first = (num_customers_week_2_first / len(customers)) * 100.0
	pct_customers_week_3 = (num_customers_week_3 / len(customers)) * 100.0
	pct_customers_week_3_first = (num_customers_week_3_first / len(customers)) * 100.0


	print(f"Week 1: {pct_customers_week_1}% customers ({num_customers_week_1}) / {pct_customers_week_1}% 1st time ({num_customers_week_1})")
	print(f"Week 2: {pct_customers_week_2}% customers ({num_customers_week_2}) / {pct_customers_week_2_first}% 1st time ({num_customers_week_2_first})")
	print(f"Week 3: {pct_customers_week_3}% customers ({num_customers_week_3}) / {pct_customers_week_3_first}% 1st time ({num_customers_week_3_first})")




if __name__ == '__main__':

	start_date = sys.argv[1]
	end_date = sys.argv[2]
	customers_path = sys.argv[3]
	orders_path = sys.argv[4]

	analysis(start_date, end_date, customers_path, orders_path)

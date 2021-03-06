#!/usr/bin/env python3

# Optional challenge:
# As optional challenges, you could try some of the following functionalities:
#
# [✓] Sort the list of cars in the PDF by total sales.
# [ ] Create a pie chart for the total sales of each car made.
# [ ]  Create a bar chart showing total sales for the top 10 best selling vehicles using the ReportLab Diagra library. Put the vehicle name on the X-axis and total revenue (remember, price * total sales!) along the Y-axis.


from email import message
import json
import locale
import sys
import operator

import reports
import emails

def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    max_sales = {"total_sales": 0}
    year_sales = {} # Dictionary with year as key, and total_sales as value
    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
        # TODO: also handle max sales
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item
        # TODO: also handle most popular car_year
        item_year = item["car"]["car_year"]
        year_sales[item_year] = year_sales.get(item_year, 0) + item["total_sales"]
        
    
    popular_year = max (year_sales.items(), key=operator.itemgetter(1))[0]

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} generated the most sales: {}".format(
            format_car(max_sales["car"]), max_sales["total_sales"]),
        "The most popular year was {} with {} sales".format(
            popular_year, year_sales[popular_year])
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_header = ["ID", "Car", "Price", "Total Sales"]
    table_data = []
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    # Sort table based on total_sales (item index 3))
    table_data.sort(key=operator.itemgetter(3), reverse=True)
    table_data.insert(0, table_header)

    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    summary = process_data(data)
    print(summary)
    # TODO: turn this into a PDF report -> /tmp/cars.pdf
    reports.generate(
                    "cars.pdf", # Should be "/tmp/cars.pdf" in qwicklabs
                    "Sales summary for last month",
                    '<br/>'.join(summary),
                    cars_dict_to_table(data)

    )

    # TODO: send the PDF report as an email attachment
    message = emails.generate(
        sender="automation@example.com",
        recipient="username@example.com",
        subject="Sales summary for last month",
        body="\n".join(summary),
        attachment_path="cars.pdf"
    )
    # emails.send(message)


if __name__ == "__main__":
    main(sys.argv)

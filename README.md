# TripCost
A simple Python script to calculate the total cost of a trip based on its distance, applying different rates for shorter and longer journeys.

# ✈️ Trip Cost Calculator

A command-line Python script that calculates the total price of a trip based on the distance entered by the user. The program applies a different price per kilometer depending on whether the trip is longer or shorter than 200 km.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `TripCost.py`).
3.  Run the script from your terminal:
    ```sh
    python TripCost.py
    ```
4.  The program will prompt you for the trip distance. Once you enter the value, it will calculate and display the total cost.

## Pricing Logic

The cost of the trip is calculated based on the following rules:

* **For trips up to 200 km:** The price is **$0.50** per kilometer.
* **For trips longer than 200 km:** The price is reduced to **$0.45** per kilometer.

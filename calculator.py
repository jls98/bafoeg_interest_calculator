# yearly interest rate
interest_rate = 0.05

# compute the monthly interest assuming a monthly interest
interest_month = 1+ interest_rate/12

# max number of months to pay off debts
total_months = 77

# amount to pay back
sum = 10010

# remaining amount after discount (21 % for 10000+)
sum_off = 10010*0.79

# compute the state after a month (add monthly interest, every quarter deduct rate)
def next_month(sum, month, interest_month):
    if month % 3 == 0:
        sum-=3*130
    return sum*interest_month

# V1 compute the amount of money when paying as long as possible
def compute_money(sum): 
    month = 0
    temp = sum
    for month in range (total_months):
        temp=next_month(temp, month, interest_month)
    return temp   

result = compute_money(sum)
print("V1 pay rates: with yearly interest rate of", interest_rate, "a total of", result, "EUR after", total_months, "months!" )

# V2 pay off debt at once and profit from discount
result2 = sum_off*(interest_month**total_months)
print("V2 instant pay: with yearly interest rate of", interest_rate, "a total of", result2, "EUR after", total_months, "months!" )


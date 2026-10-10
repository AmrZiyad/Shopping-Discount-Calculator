# SHOPPING DISCOUNT CALCULATOR

# Part 1: valid & try + while loop
valid = False

# Start a while loop that runs while valid is False
while not valid:
    
    # Part 2: try + input and calculation
    try:
        # 1. Ask for the bill, and turn it into a number with float().
        bill = float(input("Bill amount: "))
        
        # 2. Ask for the discount percent, and turn it into a number with float().
        discount_percent = float(input("Discount percent: "))
        
        # 3. Ask for the number of people, and turn it into a whole number with int().
        people = int(input("Number of people: "))
        
        # 4. Work out the discount amount, the final bill and what each person pays.
        discount_amount = bill * discount_percent / 100
        final_bill = bill - discount_amount
        each_person_pays = final_bill / people
        
    # Part 3: except blocks
    except ValueError:
        # Catches letters/symbols typed instead of numbers
        print("Please type numbers only.")
        
    except ZeroDivisionError:
        # Catches division by zero when number of people is 0
        print("People cannot be 0.")
        
    # Part 4: else and finally blocks
    else:
        # Runs only when no error occurs
        print(f"Final bill: {final_bill}")
        print(f"Each person pays: {each_person_pays}")
        valid = True  # Stops the loop
        
    finally:
        # Runs every single time after a good or bad attempt
        print("Attempt finished.")

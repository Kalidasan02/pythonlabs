header = """\n\tBOOKSTORE RECEIPT
\t------------------"""

book1_title = "Python Basics"
book1_price = 450
book2_title = "Data Science Intro"
book2_price = 600

book1_line = "\nBook Title: {}\t\t₹{}".format(book1_title, book1_price)
book2_line = "\nBook Title: {}\t₹{}".format(book2_title, book2_price)

total_price = book1_price + book2_price
total_line = "\n\nTotal:\t\t\t₹{}".format(total_price)

thank_you = "\n\n\tTHANK YOU FOR SHOPPING WITH US!"

receipt = header + book1_line + book2_line + total_line + thank_you

print(receipt.upper())

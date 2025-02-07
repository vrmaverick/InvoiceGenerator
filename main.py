from sub import generate_html
if __name__ == "__main__" : 
    print(" This project was specially built for generating invoices for pickup services used by mails\n In India there is a UPI system whose qr code is appended for payment \n")
    name = input("Enter the name of client : ")
    pickup = input("Enter pickup address : ")
    drop = input("Enter dropoff address : ")
    cost = int(input(" Cost (RS) : "))
    print(name,cost,pickup,drop)
    generate_html(name,cost,pickup,drop)

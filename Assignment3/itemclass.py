"""This is a class file that I haven't done anything with yet: I think I will probably use this in my DisplayCXInserts py eventally to better organize
the table data, but at the moment it isn't connected to anything."""

class customer():
    def __init__(self, customer_email, phone_number, first_name, last_name):
        self.first_name = customer_email
        self.last_name = phone_number
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.customer_email}'

    def customer_email(self):
        return self.customer_email

class address():
    def __init(self, address, city, state, zipcode):
        self.address = address
        self.city = city
        self.state = state
        self. zipcode = zipcode

    def __str__(self):
        return f'{self.address} , {self.city}, {self.state}, {self.zipcode}'

    def address(self):
        return self.address

    def city(self):
        return self.city

    def state(self):
        return self.state

    def zipcode(self):
        return self.zipcode()


class order_table():
    def __init(self, order_id, prod_purch, age_of_order, experience, review):
        self.order_id = order_id
        self.prod_purch = prod_purch
        self.age_of_order = age_of_order
        self.experience = experience
        self.review = review

    def order_id(self):
        return self.age_of_order

    def prod_purch(self):
        return self.prod_purch

    def experience(self):
        return self.experience

    def review(self):
        return self.review

class request():
    def __init__(self, request_id, prod_request):
        self.request_id = request_id
        self.prod_request = prod_request

    def request_id(self):
        return self.request_id

    def prod_request(self):
        return self.prod_request



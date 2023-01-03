from flask import Flask
app = Flask(__name__)

#init ma
ma = Marshmallow(app)

# Customers model
class Customers(db.Model):
    CustomerID = db.Column(db.String(5), primary_key=True, nullable = False)
    CompanyName = db.Column(db.String(40), nullable = False)
    ContactName = db.Column(db.String(30))
    ContactTitle = db.Column(db.String(30))
    Address = db.Column(db.String(60))
    City = db.Column(db.String(15))
    Region = db.Column(db.String(15))
    PostalCode = db.Column(db.String(10))
    Country = db.Column(db.String(15))
    Phone = db.Column(db.String(24))
    Fax = db.Column(db.String(24))

    def _init_(self,CustomerID,CompanyName,ContactName,ContactTitle,Address,City,Region,PostalCode,Country,Phone,Fax):
        self.CustomerID = CustomerID
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax 

# Customer schema
class CustomersSchema(ma.Schema):
    class Meta:
        fields = ("CustomerID", "CompanyName", "ContactName","ContactTitle",
        "Address", "City","Region", "PostalCode", "Country", "Phone", "Fax")

# init customer schema
customer_schema = CustomersSchema()
customers_schema = CustomersSchema(many=True)

class NorthWindCustomers:
    # Insert A Customer
    @app.route('/customers', methods = ['POST'])
    def add_customers():
        CustomerID = request.json["CustomerID"]
        CompanyName = request.json["CompanyName"]
        ContactName = request.json["ContactName"]
        ContactTitle = request.json["ContactTitle"]
        Address = request.json["Address"]
        City = request.json["City"]
        Region = request.json["Region"]
        PostalCode = request.json["PostalCode"]
        Country = request.json["Country"]
        Phone = request.json["Phone"]
        Fax = request.json["Fax"]
        
        new_customers = Customers(CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)
        db.session.add(new_customers)
        db.session.commit()
        
        return customer_schema.jsonify(new_customers)

    # Select All Customers
    @app.route('/customers/all', methods = ['GET'])
    def get_customers():
        all_customers = Customers.query.all()
        result = customers_schema.dump(all_customers)
        return jsonify(result)

    # Select single Customer
    @app.route('/customers/<CustomerID>', methods = ['GET'])
    def get_customer(CustomerID):
        customer = Customers.query.get(CustomerID)
        return customer_schema.jsonify(customer)

    # Update A Customer
    @app.route('/customers/<CustomerID>', methods = ['PUT'])
    def update_customer(CustomerID):
        customer = Customers.query.get(CustomerID)
        
        CustomerID = request.json["CustomerID"]
        CompanyName = request.json["CompanyName"]
        ContactName = request.json["ContactName"]
        ContactTitle = request.json["ContactTitle"]
        Address = request.json["Address"]
        City = request.json["City"]
        Region = request.json["Region"]
        PostalCode = request.json["PostalCode"]
        Country = request.json["Country"]
        Phone = request.json["Phone"]
        Fax = request.json["Fax"]
        
        customer.CustomerID = CustomerID
        customer.CompanyName = CompanyName
        customer.ContactName = ContactName
        customer.ContactTitle = ContactTitle
        customer.Address = Address
        customer.City = City
        customer.Region = Region
        customer.PostalCode = PostalCode
        customer.Country = Country
        customer.Phone = Phone
        customer.Fax = Fax

        db.session.commit()
        
        return customer_schema.jsonify(customer)

# Products model
class Products(db.Model):
    ProductID = db.Column(db.Integer, primary_key=True, nullable = False)
    ProductName = db.Column(db.String(40), nullable = False)
    SupplierID = db.Column(db.Integer)
    CategoryID = db.Column(db.Integer)
    QuantityPerUnit = db.Column(db.String(20))
    UnitPrice = db.Column(db.Float)
    UnitsInStock = db.Column(db.Integer)
    UnitsOnOrder = db.Column(db.Integer)
    ReorderLevel = db.Column(db.Integer)
    Discontinued = db.Column(db.Integer)
    

    def _init_(self, ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit,
    UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.SupplierID = SupplierID
        self.CategoryID = CategoryID
        self.QuantityPerUnit = QuantityPerUnit
        self.UnitPrice = UnitPrice
        self.UnitsInStock = UnitsInStock
        self.UnitsOnOrder = UnitsOnOrder
        self.ReorderLevel = ReorderLevel
        self.Discontinued = Discontinued

# Product schema
class ProductsSchema(ma.Schema):
    class Meta:
        fields = ("ProductID", "ProductName", "SupplierID", "CategoryID", "QuantityPerUnit",
        "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued")

# init Product schema
product_schema = ProductsSchema()
products_schema = ProductsSchema(many=True)


class NorthWindProducts:
    # Insert A Product
    @app.route('/products', methods = ['POST'])
    def add_products():
        ProductID = request.json["ProductID"]
        ProductName = request.json["ProductName"]
        SupplierID = request.json["SupplierID"]
        CategoryID = request.json["CategoryID"]
        QuantityPerUnit = request.json["QuantityPerUnit"]
        UnitPrice = request.json["UnitPrice"]
        UnitsInStock = request.json["UnitsInStock"]
        UnitsOnOrder = request.json["UnitsOnOrder"]
        ReorderLevel = request.json["ReorderLevel"]
        Discontinued = request.json["Discontinued"]
        
        new_products = Products(ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit,
        UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
        db.session.add(new_products)
        db.session.commit()
        
        return product_schema.jsonify(new_products)

    # Select All Products
    @app.route('/products/all', methods = ['GET'])
    def get_products():
        all_products = Products.query.all()
        result = products_schema.dump(all_products)
        return jsonify(result)

    # Select single Product
    @app.route('/products/<ProductID>', methods = ['GET'])
    def get_product(ProductID):
        product = Products.query.get(ProductID)
        return product_schema.jsonify(product)

    # Update A Product
    @app.route('/products/<ProductID>', methods = ['PUT'])
    def update_product(ProductID):
        product = Products.query.get(ProductID)
        
        ProductID = request.json["ProductID"]
        ProductName = request.json["ProductName"]
        SupplierID = request.json["SupplierID"]
        CategoryID = request.json["CategoryID"]
        QuantityPerUnit = request.json["QuantityPerUnit"]
        UnitPrice = request.json["UnitPrice"]
        UnitsInStock = request.json["UnitsInStock"]
        UnitsOnOrder = request.json["UnitsOnOrder"]
        ReorderLevel = request.json["ReorderLevel"]
        Discontinued = request.json["Discontinued"]
        
        
        product.ProductID = ProductID
        product.ProductName = ProductName
        product.SupplierID = SupplierID
        product.CategoryID = CategoryID
        product.QuantityPerUnit = QuantityPerUnit
        product.UnitPrice = UnitPrice
        product.UnitsInStock = UnitsInStock
        product.UnitsOnOrder = UnitsOnOrder
        product.ReorderLevel = ReorderLevel
        product.Discontinued = Discontinued

        db.session.commit()
        
        return product_schema.jsonify(product)


# Orders model
class Orders(db.Model):
    OrderID = db.Column(db.Integer, primary_key=True, nullable = False)
    CustomerID = db.Column(db.String(5), nullable = False)
    EmployeeID = db.Column(db.Integer, nullable = False)
    OrderDate = db.Column(db.DateTime)
    RequiredDate = db.Column(db.DateTime)
    ShippedDate = db.Column(db.DateTime)
    ShipVia = db.Column(db.Integer)
    Freight = db.Column(db.Float)
    ShipName = db.Column(db.String(40))
    ShipAddress = db.Column(db.Text)
    ShipCity = db.Column(db.String(15))
    ShipRegion = db.Column(db.String(15))
    ShipPostalCode = db.Column(db.String(10))
    ShipCountry = db.Column(db.String(15))

    def _init_(self, OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate,
    ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.EmployeeID = EmployeeID
        self.OrderDate = OrderDate
        self.RequiredDate = RequiredDate
        self.ShippedDate = ShippedDate
        self.ShipVia = ShipVia
        self.Freight = Freight
        self.ShipName = ShipName
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipRegion = ShipRegion
        self.ShipPostalCode = ShipPostalCode
        self.ShipCountry = ShipCountry

# Order schema
class OrdersSchema(ma.Schema):
    class Meta:
        fields = ("OrderID", "CustomerID", "EmployeeID", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia",
        "Freight", "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry")

# init Order schema
order_schema = OrdersSchema()
orders_schema = OrdersSchema(many=True)


class NorthWindOrders:
    # Insert An Order
    @app.route('/orders', methods = ['POST'])
    def add_orders():
        OrderID = request.json["OrderID"]
        CustomerID = request.json["CustomerID"]
        EmployeeID = request.json["EmployeeID"]
        OrderDate = request.json["OrderDate"]
        RequiredDate = request.json["RequiredDate"]
        ShippedDate = request.json["ShippedDate"]
        ShipVia = request.json["ShipVia"]
        Freight = request.json["Freight"]
        ShipName = request.json["ShipName"]
        ShipAddress = request.json["ShipAddress"]
        ShipCity = request.json["ShipCity"]
        ShipRegion = request.json["ShipRegion"]
        ShipPostalCode = request.json["ShipPostalCode"]
        ShipCountry = request.json["ShipCountry"]

        new_orders = Orders(OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate,
        ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry)

        db.session.add(new_orders)
        db.session.commit()
        
        return order_schema.jsonify(new_orders)

    # Select All Orders
    @app.route('/orders/all', methods = ['GET'])
    def get_orders():
        all_orders = Orders.query.all()
        result = orders_schema.dump(all_orders)
        return jsonify(result)

    # Select single Order
    @app.route('/orders/<OrderID>', methods = ['GET'])
    def get_order(OrderID):
        order = Orders.query.get(OrderID)
        return order_schema.jsonify(order)

    # Update An Order
    @app.route('/orders/<OrderID>', methods = ['PUT'])
    def update_order(OrderID):
        order = Orders.query.get(OrderID)
        
        OrderID = request.json["OrderID"]
        CustomerID = request.json["CustomerID"]
        EmployeeID = request.json["EmployeeID"]
        OrderDate = request.json["OrderDate"]
        RequiredDate = request.json["RequiredDate"]
        ShippedDate = request.json["ShippedDate"]
        ShipVia = request.json["ShipVia"]
        Freight = request.json["Freight"]
        ShipName = request.json["ShipName"]
        ShipAddress = request.json["ShipAddress"]
        ShipCity = request.json["ShipCity"]
        ShipRegion = request.json["ShipRegion"]
        ShipPostalCode = request.json["ShipPostalCode"]
        ShipCountry = request.json["ShipCountry"]
        
        
        order.OrderID = OrderID
        order.CustomerID = CustomerID
        order.EmployeeID = EmployeeID
        order.OrderDate = OrderDate
        order.RequiredDate = RequiredDate
        order.ShippedDate = ShippedDate
        order.ShipVia = ShipVia
        order.Freight = Freight
        order.ShipName = ShipName
        order.ShipAddress = ShipAddress
        order.ShipCity = ShipCity
        order.ShipRegion = ShipRegion
        order.ShipPostalCode = ShipPostalCode
        order.ShipCountry = ShipCountry

        db.session.commit()
        
        return order_schema.jsonify(order)

    # Order history of given customer

    @app.route('/ordershistory/<CustomerID>', methods = ['GET'])
    def get_order_history(CustomerID):
        all_orders = Orders.query.filter_by(CustomerID = CustomerID)
        result = orders_schema.dump(all_orders)
        return jsonify(result)

#Run Server
if __name__=='__main__':
    app.run(debug=True)
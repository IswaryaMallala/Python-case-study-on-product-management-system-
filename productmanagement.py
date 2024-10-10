class Product:

    def __init__(self, pid, name, category, price):

        self.pid = pid

        self.name = name

        self.category = category

        self.price = price

 

    def __repr__(self):

        return f"ID: {self.pid}, Name: {self.name}, Price: {self.price} Category: {self.category}"

 

class ProductManagementSystem:

    def __init__(self):

        self.products = {}

 

    # Add product

    def add_product(self, pid, name, category, price):

        if pid in self.products:

            print(f"Product with ID {pid} already exists.")

            return

        self.products[pid] = Product(pid, name, category, price)

        print(f"Added: {self.products[pid]}")

 

    # Update product

    def update_product(self, pid, name=None, category=None, price=None):

        if pid not in self.products:

            print(f"Product with ID {pid} does not exist.")

            return

        product = self.products[pid]

        if name:

            product.name = name

        if category:

            product.category = category

        if price is not None:

            product.price = price

        print(f"Updated: {product}")

 

    # Delete product

    def delete_product(self, pid):

        if pid in self.products:

            deleted_product = self.products.pop(pid)

            print(f"Deleted: name: {deleted_product.name}, price: {deleted_product.price}")

        else:

            print(f"Product with ID {pid} does not exist.")

 

    # Get product by PID

    def get_product_by_pid(self, pid):

        product = self.products.get(pid)

        if product:

            return f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category:{product.category}"

        return f"Product with ID {pid} does not exist."

 

    # Get all products

    def get_all_products(self):

        return [f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category:{product.category}" for product in self.products.values()]

 

    # Get products by category

    def get_products_by_category(self, category):

        return [f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category:{product.category}" for product in self.products.values() if product.category.lower() == category.lower()]

 

    # Get products between price range

    def get_products_between_price(self, min_price, max_price):

        return [f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category:{product.category}" for product in self.products.values() if min_price <= product.price <= max_price]

 

def main():

    pms = ProductManagementSystem()

 

    while True:

        print("\nProduct Management System")

        print("1. Add Product")

        print("2. Update Product")

        print("3. Delete Product")

        print("4. Get Product by PID")

        print("5. Get All Products")

        print("6. Get Products by Category")

        print("7. Get Products Between Price")

        print("8. Exit")

 

        choice = input("Enter your choice: ")

 

        if choice == '1':

            pid = int(input("Enter Product ID: "))

            name = input("Enter Product Name: ")

            category = input("Enter Product Category: ")

            price = float(input("Enter Product Price: "))

            pms.add_product(pid, name, category, price)

 

        elif choice == '2':

            pid = int(input("Enter Product ID to update: "))

            name = input("Enter new Product Name (leave blank to keep current): ")

            category = input("Enter new Product Category (leave blank to keep current): ")

            price_input = input("Enter new Product Price (leave blank to keep current): ")

            price = float(price_input) if price_input else None

            pms.update_product(pid, name if name else None, category if category else None, price)

 

        elif choice == '3':

            pid = int(input("Enter Product ID to delete: "))

            pms.delete_product(pid)

 

        elif choice == '4':

            pid = int(input("Enter Product ID to retrieve: "))

            print(pms.get_product_by_pid(pid))

 

        elif choice == '5':

            products = pms.get_all_products()

            if products:

                for product in products:

                    print(product)

            else:

                print("No products available.")

 

        elif choice == '6':

            category = input("Enter Product Category to filter by: ")

            products = pms.get_products_by_category(category)

            if products:

                for product in products:

                    print(product)

            else:

                print(f"No products found in category '{category}'.")

 

        elif choice == '7':

            min_price = float(input("Enter minimum price: "))

            max_price = float(input("Enter maximum price: "))

            products = pms.get_products_between_price(min_price, max_price)

            if products:

                for product in products:

                    print(product)

            else:

                print(f"No products found in the price range {min_price} - {max_price}.")

 

        elif choice == '8':

            print("Exiting the system.")

            break

 

        else:

            print("Invalid choice. Please try again.")

 

if __name__ == "__main__":

    main()

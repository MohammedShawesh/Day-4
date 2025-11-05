class Item:
      def __init__(self, item_id, name, department, price, stock_quantity, on_sale=False, sale_price=None):
            # Attributes (What the item has)
            self.item_id = item_id
            self.name = name
            self.department = department
            self.price = price
            self.stock_quantity = stock_quantity
            self.on_sale = on_sale
            self.sale_price = sale_price
      def purchase(self, quantity):
            if quantity > 0:
                if self.stock_quantity >= quantity:
                    self.stock_quantity -= quantity
                    print(f" Successful purchase of {quantity} units of {self.name}. Remaining stock: {self.stock_quantity}")
                    return True
                else:
                    print(f" Error: Not enough stock of {self.name}. Available: {self.stock_quantity}.")
                    return False
            else:
                print(" Error: Purchase quantity must be positive.")
                return False

      def restock(self, quantity):
            if quantity > 0:
                self.stock_quantity += quantity
                print(f"Restocked {quantity} units of {self.name}. New stock: {self.stock_quantity}")
            else:
                print("Error: Restock quantity must be positive.")

      def set_price(self, new_price):
            if new_price >= 0:
                self.price = new_price
                if self.on_sale:
                    self.end_sale()
                print(f"Price of {self.name} updated to ${self.price:.2f}")
            else:
                print("Error: Price cannot be negative.")

      def apply_sale(self, discount_percentage):
            if 0 < discount_percentage <= 100:
                self.on_sale = True
                discount_factor = (100 - discount_percentage) / 100
                self.sale_price = self.price * discount_factor
                print(f"{self.name} is now on sale! Discount: {discount_percentage}%. Sale Price: ${self.sale_price:.2f}")
            else:
                print("Error: Discount percentage must be between 0 and 100.")
      def end_sale(self):
            self.on_sale = False
            self.sale_price = None
            print(f"Sale ended for {self.name}. Standard price is back: ${self.price:.2f}")
      def get_current_price(self):
            if self.on_sale and self.sale_price is not None:
                return self.sale_price
            return self.price

      def __str__(self):
          price_display = f"${self.get_current_price():.2f} (Sale)" if self.on_sale else f"${self.price:.2f}"
          return f"Item: {self.name} (ID: {self.item_id}) | Dept: {self.department} | Price: {price_display} | Stock: {self.stock_quantity}"

# 1. Create a new item
milk = Item(item_id="M123", name="Organic Milk 1L", department="Dairy", price=4.50, stock_quantity=100)
print(milk)

# 2. Restock the item
milk.restock(50)

# 3. Apply a sale
milk.apply_sale(20)

# 4. Purchase the item
milk.purchase(5)

# 5. Check the current price and status
print(milk)

# 6. End the sale and purchase again
milk.end_sale()
milk.purchase(10)
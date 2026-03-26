def print_order(name,chai_type):
    print(f"{name} ordered {chai_type} chai")

print_order("Aman","masal")
print_order("Gina","Green")
print_order("kumin","lemon")

# Example 2

def fetch_sales():
    print("Fetching data")

def filter_orders():
    print("Filter sales")

def summarize_data():
    print("Summarize")

def generate_report():
    fetch_sales()
    filter_orders()
    summarize_data()
    print("Report ready")

generate_report()
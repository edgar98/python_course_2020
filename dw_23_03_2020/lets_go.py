import filer
import transactions

if __name__ == '__main__':
    # filer.create_file()
    # filer.open_file()
    manager = transactions.TransactionManager()
    manager.calculate_transactions()
    manager.show_transactions()

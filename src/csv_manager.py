import csv
import os


class CSVManager:
    """Class for managing CSV files."""

    def __init__(self, path):
        """
        Initializes the CSVManager class.

        Parameters:
        path: Path to the CSV file.
        """

        self.path = path

        # if the file does not exist, create it
        if not os.path.exists(self.path):
            with open(path, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['name', 'type', 'price'])
        

    def load(self):
        """
        Loads the CSV file.

        Returns:
        A list of dictionaries.
        """
        
        with open(self.path) as f:
            reader = csv.DictReader(f)
            return list(reader)
        
    def save(self, name, type, price):
        """
        Saves the CSV file.

        Parameters:
        name: Name of the item.
        type: Type of the item.
        price: Price of the item.
        """

        with open(self.path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([name, type, price])

    def csv_append(self, rows):
        '''
        Appends to the end of the csv

        rows: a list of a list with the following format ["name", 'type', 'price']
        '''
        with open(self.path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
            
    

    
import pandas as pd
import os

class SlugTestData:
    def __init__(self, config):
        self.config = config

    def load_data(self, file_path):
        """Loads slug test data from CSV or Excel files."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == '.csv':
            return pd.read_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            return pd.read_excel(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

    def validate_well_parameters(self, data):
        """Validates well parameters in the data."""
        required_columns = ['Well ID', 'Slug Test Date', 'Drawdown']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        return True

    def handle_configuration(self, config_updates):
        """Handles configuration updates."""
        self.config.update(config_updates)
        return self.config


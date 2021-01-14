"""A class that represents a regex pattern and its associated tag and date."""

import re
import json
import pandas as pd
import datetime as dt
import plotly.express as px

class DateTag:
    """Search for a regex pattern and its associated tag and date."""

    def __init__(self, source_file, match_pattern):
        """Initialize source document attribute."""
        self.source = source_file
        self.pattern = match_pattern

    def make_pattern_object(self):
        """Make a regex pattern object."""
        regex = fr"{self.pattern}"
        pattern_object = re.compile(regex, re.MULTILINE)
        return pattern_object

    def save_data(self, data, filename):
        """Save data to file in JSON format."""
        with open(filename, 'w+') as f:
            json.dump(data, f)

    def value_date_new(self, dictionary):
        """Find the most recent value and the date it was recorded."""
        val_date = dictionary
        n_date = list(val_date)[0]
        n_value = val_date[n_date]
        return n_value, n_date

    def value_date_max(self, dictionary):
        """Find the maximum value and the date(s) it was recorded."""
        val_date = dictionary
        max_val = {}
        # Set a starting date and value for maximum.
        m_date = list(val_date)[0]
        m_value = val_date[m_date]
        max_val[m_date] = m_value
        for key, value in val_date.items():
            if value > m_value:
                m_value = value
                m_date = key
                max_val = {} # reset to empty
                max_val[m_date] = m_value
            elif value == m_value:
                max_val[key] = value
        return max_val

    def value_date_min(self, dictionary):
        """Find the minimum value and the date(s) it was recorded."""
        val_date = dictionary
        min_val = {}
        # Set a starting date and value for minimum.
        m_date = list(val_date)[0]
        m_value = val_date[m_date]
        min_val[m_date] = m_value
        for key, value in val_date.items():
            if value < m_value:
                m_value = value
                m_date = key
                min_val = {}
                min_val[m_date] = m_value
            elif value == m_value:
                min_val[key] = value
        return min_val

    def value_average(self, dictionary):
        """Find the average value from a list of numbers."""
        src = dictionary
        data = []
        for value in src.values():
            data.append(float(value))
        avg = round(sum(data)/len(data), 1)
        return avg

    def make_list(self):
        """
        Retrieve measurements and dates they were recorded
        from self.source_file and return as a list.
        """
        try:
            with open(self.source) as f:
                contents = f.read()
                p = self.make_pattern_object() # call as a member function
                match_list = re.findall(p, contents)
            return match_list
        except FileNotFoundError:
            print(f"\nError: File '{filename}' not found.")

    def list_to_dictionary(self, source_list, key_slice_start, key_slice_end, 
        value_slice_start, value_slice_end):
        """
        Retrieve items from source_list and create a dictionary 
        using <key>-<value>.
        """
        ks = key_slice_start
        ke = key_slice_end
        vs = value_slice_start
        ve = value_slice_end
        dictionary = {}
        for item in source_list:
            dict_key = item[0][ks:ke]
            dict_value = item[1][vs:ve]
            dictionary[dict_key] = dict_value
        return dictionary

    def dict_to_tab(self, dictionary, date_column, measure_column):
        """Convert dictionary to tabular data."""
        my_dict = dictionary
        col_1 = date_column
        col_2 = measure_column
        d = '%Y-%m-%d'
        # Display all rows (do not truncate).
        pd.set_option('display.max_rows', None)
        # Convert dictionary to dataframe
        df = pd.DataFrame(list(my_dict.items()),columns = [col_1,col_2])
        # Create date objects in the syntax `datetime.date(Y, M, D)`
        df[col_1] = df[col_1].apply(lambda x: dt.datetime.strptime(x,d))
        # Reverse order of dataframe
        df = df[::-1]
        return df

    def make_scatter(self, data_frame, title, xlabel, ylabel):
        """Make a scatter plot from <data_frame>."""
        df = data_frame
        tl = title
        xl = xlabel
        yl = ylabel
        fig = px.scatter(df, x=xl, y=yl, title=tl)
        fig.show()

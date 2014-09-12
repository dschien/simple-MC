'''
simple-MC: Main module

Copyright 2014, Dan Schien
Licensed under MIT.
'''

import importlib
import xlrd

__author__ = 'schien'

NAME = 'name'
TYPE = 'type'
PARAM_A = 'param_a'
PARAM_B = 'param_b'
PARAM_C = 'param_c'

MODULE = 'module'

LABEL = 'label'

UNIT = 'unit'
TABLE_STRUCT = {
    NAME: 0,
    MODULE: 1,
    TYPE: 2,
    PARAM_A: 3,
    PARAM_B: 4,
    PARAM_C: 5,
    UNIT: 6,
    LABEL: 7,
    'comment': 8,
    'description': 9
}


class ModelLoader(object):
    def __init__(self, file, size=1):
        self.wb = load_workbook(file)
        self.size = size


    def get_row(self, name):
        i = [row[TABLE_STRUCT[NAME]] for row in self.wb].index(name)
        return self.wb[i]

    def get_val(self, name, args=None):
        """
        Apply function to arguments from excel table
         args: optional additonal args
        If no args are given, applies default size from constructor
        """
        row = self.get_row(name)
        f, p = build_distribution(row)
        if args is not None:
            ret = f(*p, **args)
            assert ret.shape == (self.size,)
            return ret
        else:
            ret = f(*p, size=self.size)
            assert ret.shape == (self.size,)
            return ret

    def get_label(self, name):
        try:
            row = self.get_row(name)
        except:
            return name
        return row[TABLE_STRUCT[LABEL]]

    def get_property(self, name, prop):
        try:
            row = self.get_row(name)
        except:
            return name
        return row[TABLE_STRUCT[prop]]

    def __getitem__(self, name):
        """
        Get the distribution for a item name from the table
        Then execute and return the result array
        """
        return self.get_val(name)


def build_distribution(row):
    module = importlib.import_module(row[TABLE_STRUCT[MODULE]])
    func = getattr(module, row[TABLE_STRUCT[TYPE]])
    if row[TABLE_STRUCT[TYPE]] == 'choice':

        cell = row[TABLE_STRUCT[PARAM_A]]
        if type(cell) in [float, int]:
            params = ([cell],)
        else:
            tokens = cell.split(',')

            params = [float(token.strip()) for token in tokens]
            params = (params, )
    elif row[TABLE_STRUCT[TYPE]] == 'Distribution':
        func = func()
        params = tuple(row[TABLE_STRUCT[i]] for i in [PARAM_A, PARAM_B, PARAM_C] if row[TABLE_STRUCT[i]])
    else:
        params = tuple(row[TABLE_STRUCT[i]] for i in [PARAM_A, PARAM_B, PARAM_C] if row[TABLE_STRUCT[i]])
    return func, params


def load_workbook(file):
    wb = xlrd.open_workbook(file)

    sh = wb.sheet_by_index(0)
    var_column = sh.col_values(TABLE_STRUCT[NAME])
    module_column = sh.col_values(TABLE_STRUCT[MODULE])
    distribution_type_column = sh.col_values(TABLE_STRUCT[TYPE])
    param_a_colum = sh.col_values(TABLE_STRUCT[PARAM_A])
    param_b_colum = sh.col_values(TABLE_STRUCT[PARAM_B])
    param_c_colum = sh.col_values(TABLE_STRUCT[PARAM_C])
    unit_colum = sh.col_values(TABLE_STRUCT[UNIT])
    label_colum = sh.col_values(TABLE_STRUCT[LABEL])

    rows_es = zip(var_column, module_column, distribution_type_column, param_a_colum, param_b_colum, param_c_colum,
                  unit_colum, label_colum)
    return rows_es

def main():
    '''
    Main function of the boilerplate code is the entry point of the 'simplemc' executable script (defined in setup.py).
    
    Use doctests, those are very helpful.
    
    >>> main()
    Hello
    >>> 2 + 2
    4
    '''
    
    print("Hello")


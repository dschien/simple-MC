Framework to build MC simulations with random variable parameters defined in excel spreadsheets
===============================================================================================

This package provides a simple framework to run MonteCarlo models based on parameters in excel spreadsheets like such:

| variable | module       | distribution | param 1 | param 2 |
|----------|--------------|--------------|---------|---------|
| A        | numpy.random | choice       | 2       |         |
|          |              |              |         |         |
|          |              |              |         |         |

For each variable a numpy random distribution is created (choice, uniform or triangular in the example) with the given parameters.
Only three parameters max at the moment, sorry.


Installation
------------

The easiest way to install most Python packages is via ``easy_install`` or ``pip``::

    $ easy_install simple_MC

Usage
-----

Here is a simple example of the use of the model::


    >> samples = 10000
    >> data = ModelLoader(path.join(data_dir, 'model_params.xlsx'), size=samples)

    >> def model(data):
            var_a = data['a']
            var_b = data['b']
            c = var_a * var_b

            res = {}
            for key, value in locals().iteritems():
                if type(value) in [np.ndarray, int, float]:
                    res[key] = value
            return res

The ModelLoader initialises numpy arrays based on the definition of random variables in the excel spreadsheet. The variable `c` is then an array of results what is a simpel Monte Carlo simulation. The code at the end collects all variables and places them into the `res` array where they can be accessed as `res[c]`, etc for analysis and plotting.

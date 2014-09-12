==================================================================
simple-MC: Framework to build MC simulations with random variable parameters defined in excel spreadsheets
==================================================================

This package provides a simple framework to run MonteCarlo models based on parameters in excel spreadsheets like such:

========    ============    ============    ======= ======= =======
variable	module	        distribution	param 1	param 2	param 3
========    ============    ============    ======= ======= =======
A       	numpy.random	choice	        10
B       	numpy.random	uniform	        3.59    2.0
C	        numpy.random	triangular	    16	    40	    137
========    ============    ============    ======= ======= =======

For each variable a numpy random distribution is created (choice, uniform or triangular in the example) with the given parameters.
Only three parameters max at the moment, sorry.

If you submit your package to PyPi, this text will be presented on the `public page <http://pypi.python.org/pypi/python_package_boilerplate>`_ of your package.

Note: This README has to be written using `reStructured Text <http://docutils.sourceforge.net/rst.html>`_, otherwise PyPi won't format it properly.

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

When the package is installed via ``easy_install`` or ``pip`` this function will be bound to the ``simple_MC`` executable in the Python installation's ``bin`` directory (on Windows - the ``Scripts`` directory).

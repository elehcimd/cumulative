# Getting started
This tutorial teaches you how to load, manipulate, and visualize time series datasets.
You can follow it sequentially or jump to specific questions as needed.

## Installation

Cumulative requires **Python 3.10+** and depends on **MLtraq 0.1.36+**, and **Pandas 1.5.3+**, which are installed as dependencies. To install:

```
pip install cumulative --upgrade
```

## Examples

The code examples are fully self-contained to reproduce the outputs.
This example shows the Cumulative version used to compile this tutorial.
Make sure to have the latest release installed.

{{include_code("mkdocs/tutorial/examples/version.py", title="Cumulative version")}}

# Key concepts

## Collections of time series

The `Cumulative` class handles collections of time series of varying length and their transformations. The data is stored as a `Pandas` dataframe, using `NumPy` arrays as cell values.

{{include_code("mkdocs/tutorial/examples/01-load-01.py", title="Example of time series collection")}}

## Dataframe columns

* The column names are organized hierarchically, using the dot as separator. Prefixes can be used as source and destination
of transformations. Naming conventions:

* The column suffixes `.x` and `.y` represent the X, Y values of the series.
* The column prefix `base.` is the default source and destination of transformations.

## Transformations

* Transformations are applied to a subset of columns with a source prefix and might result in additional columns with a destination prefix or reordered rows. One of the simplest transformation is `copy`.

{{include_code("mkdocs/tutorial/examples/01-transform-copy.py", title="Example of copy transform")}}

## Pipelines

Transformations are the base element to construct transformation pipelines. In the following example, 
we apply a `cumsum` operation to the `base.` prefix arrays `x` and `y`, saving the result to the `C` prefix.
The `C` prefix arrays are then piped as input for the minmax scaler, with destination prefix `S`.
The result is a data frame with additional columns for each step. If source or destination is omitted, 
the default prefix `base.` is used.


{{include_code("mkdocs/tutorial/examples/01-transform-pipe.py", title="Example of piped transforms")}}


!!! Tip
    By default, all destination columns with the destination prefix
    are dropped before adding the new ones, ensuring a clean and consistent state.    


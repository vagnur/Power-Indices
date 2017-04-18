# Power-Indices

Power index calculator, for the:

* Banzhaf power index.
* Shapley-Shubik power index.
* Holler-Packel power index.
* Deegan-Packel power index 
* Johnston power index.

## Installation

In order to install the power index calculator, you can just do the pip install, like this:

```
sudo pip install Power-indices-calculator
```

## Usage

```python
import calculator
```

Then you can use the functions in the file. For example, lets say that we have the weighted game [4;1,2,2,3], where 
4 is the quota of the game, and the rest of the vector is the weight of each player _i_ (this is, weight(P1) = 1, 
weight(P2) = 2, weight(P3) = 2 and weight(P4) = 3), then we can use the calculator like this:

```python
quota = 4
weights = [1,2,2,3]
banzhaf = calculator.banzhaf(weights,quota)
print banzhaf
```

The output of the example will be:

```python
[0.083, 0.25, 0.25, 0.417]
```

This is, banzhaf_index(P1) = 0.083, banzhaf_index(P2) = 0.25, banzhaf_index(P3) = 0.25 and banzhaf_index(P4) = 0.417.

One can use the rest of the functions to calculate the **shapley-shubik power index**, the **holler-packel power index**, **the
deegan-packel power index** and the **johnston power index**, like this (taking the same example as before):

```python
quota = 4
weights = [1,2,2,3]
banzhaf = calculator.banzhaf(weights,quota)
shapley = calculator.shapley(weights,quota)
holler = calculator.holler_packel(weights,quota)
deegan = calculator.deegan_packel(weights,quota)
johnston = calculator.johnston(weights,quota)
```

The output of the example, is summaried in the next table:

Data | Player 1 | Player 2 | Player 3 | Player 4
:---: | :---: | :---: | :---: | :---:
Weights | 1 | 2 | 2 | 3 
Banzhaf | 0.083 | 0.25 | 0.25 | 0.417
Shapley | 0.083 | 0.25 | 0.25 | 0.417
Deegan | 0.125 | 0.25 | 0.25 | 0.375
Holler | 0.125 | 0.25 | 0.25 | 0.375
Johnston | 0.071 | 0.214 | 0.214 | 0.5

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](../master/LICENSE) file for details.

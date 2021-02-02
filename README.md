# pddlgym-river-alt
PDDLGym (alternate) river environment

### Description
This is a [PDDLGym](https://github.com/tomsilver/pddlgym/) version of the River domain described as in [Freire and Delgado (2017)](http://www.ifaamas.org/Proceedings/aamas2017/pdfs/p741.pdf).
Note this is not the same as the River domain that comes with PDDLGym (that can be found [here](https://github.com/tomsilver/pddlgym/blob/master/pddlgym/pddl/river.pddl)).

### Usage
[This fork](https://github.com/GCrispino/pddlgym/)'s `river-alt-env` branch has PDDLGym already configured with this environment, together with 4 sample problems and a custom renderer. If you just want to use it, you can install with pip directly from git by running `$ pip install git+https://github.com/tomsilver/pddlgym` (if you have a PDDLGym installation it will be overriden by this) or by creating a virtual environment with it ([see here](https://github.com/tomsilver/pddlgym#installing-from-source-if-you-want-to-make-changes-to-pddlgym))

To configure the environment by yourself, you can register the domain by following [this instructions](https://github.com/tomsilver/pddlgym#adding-a-new-domain).

To create new problem instances, run the `river-generator.py` script like this:

`$ python river-generator.py nx ny`,

where `nx` is the width of the instance and `ny`, its height.

# Python tips and tricks

> Python tips and tricks

These are quick tips and tricks that I collected in the journey with Python.

This repository contains:

1. My codes that I've learned in [HackerRank](https://www.hackerrank.com).
2. A lot of useful notes in Python, please find them in this file.



## Table of Contents

- [Background](#background)
- [Container Types](#container-types)
- [Usage](#usage)
	- [Sort](#sort)
- [Badge](#badge)
- [Example Readmes](#example-readmes)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

From the start, I were a system engineer. I start to learn Python 3 years ago, but it was not continuous. Now when I decide to start again in a serious way, I'm at age of 30s. I always confuse about it, and it seems to be stupid when I decide to leave my current job to follow my dream...

> Note: use "more than" symbol (>) to print like that.

> Remember: the documentation, not the code, defines what a module does.


**Writing READMEs is way too hard, and keeping them maintained is difficult. By offloading this process - making writing easier, making editing easier, making it clear whether or not an edit is up to spec or not - you can spend less time worry about whether or not your initial documentation is good, and spend more time writing and using code.**

`As well, standardizing can help elsewhere. By having a standard, users can spend less time searching for the information they want. They can also build tools to gather search terms from descriptions, to automatically run example code, to check licensing, and so on.`

## Container Types

Containers are any object that holds an arbitrary number of other objects. Generally, containers provide a way to access the contained objects and to iterate over them.

Examples of containers include `tuple`, `list`, `set`, `dict`; these are the *built-in containers*. More container types are available in the [collections module](http://docs.python.org/dev/library/collections.html#module-collections)].

Strictly speaking, the [collections.abc.Container](http://docs.python.org/dev/library/collections.abc.html#collections.abc.Container) abstract base class ([collections.Container](http://docs.python.org/library/collections.html#collections.Container) in Python2) holds for any type that supports the in operator via the `__contains__` magic method; so if you can write `x in y` then `y` is usually a container, but not always: an important point of difference between containers and general iterables is that when iterated over, containers will return existing objects that they hold a reference to, while generators and e.g. `file` objects will create a new object each time. This has implications for garbage collection and deep object traversal (e.g. `deepcopy` and serialisation).

As an example, `iter(lambda: random.choice(range(6)), 0)` supports the `in` operator, but it is certainly _not_ a container!

The intent of the `Collections.abc.Container` abstract base class in only considering the `__contains__` magic method and not other ways of supporting the `in` operator is that a true container should be able to test for containment in a single operation and without observably changing internal state. Since `Collections.abc.Container` defines `__contains__` as an abstract method, you are guaranteed that if `isinstance(x, collections.abc.Container)` then `x` supports the `in` operator.

In practice, then, all containers will have the `__contains__` magic method. However, when testing whether an object is a container you should use `isinstance(x, collections.abc.Container)` for clarity and for forward compatibility should the `Container` subclass check ever be changed.

## Usage

### Sort

- To sort and deduplicate a list, use this structure:
```
# A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).
>>> rel = sorted(set(list_name))
# Or:
>>> rel = sorted(list(set(list_name)))
```

## Badge

> **It's under constructing**

If your README is compliant with Standard-Readme and you're on GitHub, it would be great if you could add the badge. This allows people to link back to this Spec, and helps adoption of the README. The badge is **not required**.

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

To add in Markdown format, use this code:

```
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
```

## Example Readmes

## Related Efforts

## Maintainers

[@salazar35](https://github.com/salazar35).

## Contributing

## License

[salazar35](LICENSE) © Hieudd

# conan-sol2

Conan package for [sol2](https://github.com/ThePhD/sol2)

The packages generated with this **conanfile** can be found on [here](https://bintray.com/zimmerk/conan).

## Reuse the packages

### Basic setup

```
conan install sol2/2.20.6@swissdotnet/stable
```

### Project setup

```
[requires]
sol2/2.20.6@swissdotnet/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io

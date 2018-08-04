# conan-sol2

Conan package for [sol2](https://github.com/ThePhD/sol2)

The packages generated with this **conanfile** can be found on [here](https://bintray.com/zimmerk/conan).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/sol2%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/sol2%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-sol2.svg?branch=release%2F2.20.4)](https://travis-ci.org/AtaLuZiK/conan-sol2)|[![Build status](https://ci.appveyor.com/api/projects/status/pry8jud72vnow8h1/branch/release/2.20.4?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-sol2/branch/release/2.20.4)|

## Reuse the packages

### Basic setup

```
conan install sol2/2.20.4@zimmerk/stable
```

### Project setup

```
[requires]
sol2/2.20.4@zimmerk/stable

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

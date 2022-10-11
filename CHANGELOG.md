# Changelog

## [6.0.0](https://github.com/LeeeeT/valtypes/compare/v5.0.2...v6.0.0) (2022-10-11)


### ⚠ BREAKING CHANGES

* reorganize errors (#22)
* rebranding (#19)
* `And` and `Or` conditions now takes a single tuple argument
* `rules` property was removed from the rules collection. Use `for` loop to iterate through the rules
* Call `add` instead of `add_to_end`
* One can no longer add rules to the top of a collection

### Features

* `FromCallable` parser is now a dataclass ([31a5887](https://github.com/LeeeeT/valtypes/commit/31a58876888627bbaab423561f56059dd166536a))
* `Rule` is now a dataclass ([19186bd](https://github.com/LeeeeT/valtypes/commit/19186bd42c92d29955e0c331ff219b4f9342445e))
* add `RecursiveParsingError` for cases when parsers call each other recursively ([bbcb208](https://github.com/LeeeeT/valtypes/commit/bbcb208c123e62b0098d76c7998fd9c5f3a86e84))
* add `register` decorator for adding parsers to a collection ([324887f](https://github.com/LeeeeT/valtypes/commit/324887f8076247814b27336bc9d9506ba1542e56))
* add more constrained sized types ([#43](https://github.com/LeeeeT/valtypes/issues/43)) ([ee3e43e](https://github.com/LeeeeT/valtypes/commit/ee3e43e1a23d8d4ab923b3e19b8469cfab582c80))
* conditions are now dataclasses ([cc8d515](https://github.com/LeeeeT/valtypes/commit/cc8d5154a7bb36efde5ceabc0361dd9b6941b10f))
* errors are now dataclasses ([301f9ef](https://github.com/LeeeeT/valtypes/commit/301f9ef0e5f0d97f0459e37db4040cf3ef413dfb))
* rebranding ([#19](https://github.com/LeeeeT/valtypes/issues/19)) ([94422e0](https://github.com/LeeeeT/valtypes/commit/94422e024e1f8e0082a58a2bc26f6069ed977848))


### Bug Fixes

* parsing errors are now constructed correctly ([ff93b0c](https://github.com/LeeeeT/valtypes/commit/ff93b0c6cf22308c815a119950ff09d81301506c))
* parsing errors are now constructed correctly when there are multiple parsers for a target type with different source types ([3f0ce88](https://github.com/LeeeeT/valtypes/commit/3f0ce885f1454f8001a99c272d7ac9ef0a86392b))


### Code Refactoring

* extract collection base class ([d9e9e1e](https://github.com/LeeeeT/valtypes/commit/d9e9e1e561cc8045a95fee836a0d33c5cc5010fd))
* remove `add_to_top` method ([e058c95](https://github.com/LeeeeT/valtypes/commit/e058c95a06da4597a8316ea6fbac17450bd82a02))
* rename `add_to_end` to `add` ([1093390](https://github.com/LeeeeT/valtypes/commit/1093390a645adb1bb2d0faced64696f36bb83530))
* reorganize errors ([#22](https://github.com/LeeeeT/valtypes/issues/22)) ([d7f7a5d](https://github.com/LeeeeT/valtypes/commit/d7f7a5da7a0da8901d972f57af88397b4e0e1576))


### Documentation

* add installation from source option ([#40](https://github.com/LeeeeT/valtypes/issues/40)) ([32f72e3](https://github.com/LeeeeT/valtypes/commit/32f72e3cc2aaf4cc151f07754bfeeea25a3bf4f2))
* change example of creating constrained types ([ee3e43e](https://github.com/LeeeeT/valtypes/commit/ee3e43e1a23d8d4ab923b3e19b8469cfab582c80))
* fix link and format code in README ([04900b6](https://github.com/LeeeeT/valtypes/commit/04900b62cac97f151693b8f8e07e6c066bc5b83d))
* fix outdated example ([cf9f950](https://github.com/LeeeeT/valtypes/commit/cf9f950ca8fb3181b0e407b508c652f8f1d75c1e))
* replace relative ref with absolute ref ([360d69f](https://github.com/LeeeeT/valtypes/commit/360d69f9f71c4ed15bf8b8738eec3b94d6bbc32b))
* rewrite README to markdown ([45ae200](https://github.com/LeeeeT/valtypes/commit/45ae200f3c4932c4c598575036bea031932267e5))

## [5.0.2](https://github.com/LeeeeT/valtypes/compare/v5.0.1...v5.0.2) (2022-10-11)


### Documentation

* add installation from source option ([#40](https://github.com/LeeeeT/valtypes/issues/40)) ([32f72e3](https://github.com/LeeeeT/valtypes/commit/32f72e3cc2aaf4cc151f07754bfeeea25a3bf4f2))
* fix outdated example ([cf9f950](https://github.com/LeeeeT/valtypes/commit/cf9f950ca8fb3181b0e407b508c652f8f1d75c1e))

## [5.0.1](https://github.com/LeeeeT/valtypes/compare/v5.0.0...v5.0.1) (2022-10-10)


### Documentation

* fix link and format code in README ([04900b6](https://github.com/LeeeeT/valtypes/commit/04900b62cac97f151693b8f8e07e6c066bc5b83d))

## [5.0.0](https://github.com/LeeeeT/valtypes/compare/v4.0.0...v5.0.0) (2022-10-07)


### ⚠ BREAKING CHANGES

* reorganize errors (#22)

### Code Refactoring

* reorganize errors ([#22](https://github.com/LeeeeT/valtypes/issues/22)) ([d7f7a5d](https://github.com/LeeeeT/valtypes/commit/d7f7a5da7a0da8901d972f57af88397b4e0e1576))

## [4.0.0](https://github.com/LeeeeT/valtypes/compare/v3.0.2...v4.0.0) (2022-10-06)


### ⚠ BREAKING CHANGES

* rebranding (#19)

### Features

* rebranding ([#19](https://github.com/LeeeeT/valtypes/issues/19)) ([94422e0](https://github.com/LeeeeT/valtypes/commit/94422e024e1f8e0082a58a2bc26f6069ed977848))

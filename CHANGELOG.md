# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## 1.1.0 (2022-02-26)


### Features

* add `Constrained`, `ConstraintError` and `static_analysis` to the `valtypes.__init__` ([7039427](https://github.com/LeeeeT/valtypes/commit/7039427f16dccfc2092138f6aabef1f5ba2ea19f))
* add `Dataclass` to the `valtypes.__init__` ([f3e4404](https://github.com/LeeeeT/valtypes/commit/f3e44042bfe07112de7d73fe88385e24bf2d623e))
* add `dict_to_dataclass` parser ([0c84d68](https://github.com/LeeeeT/valtypes/commit/0c84d6824217d7f4fc69e6ebc087e50ad1af03da))
* add `str_to_bytearray` parser and `str_to_bytes` parser ([c8a7659](https://github.com/LeeeeT/valtypes/commit/c8a7659d00c1b10c80646d711d8534efa2e445de))
* add aliases for dataclasses ([570eeb2](https://github.com/LeeeeT/valtypes/commit/570eeb260f1cee775db2183211ae045ce8a714e0))
* basic functionality ([55459e4](https://github.com/LeeeeT/valtypes/commit/55459e4c8bf9309469402a495e1ae6149707feab))
* choose the shortest chain first ([714c395](https://github.com/LeeeeT/valtypes/commit/714c3959e8ab79db6bc8fe2185642fbc2ea6ceac))
* integrate with `dataclasses.dataclass` ([5221c5c](https://github.com/LeeeeT/valtypes/commit/5221c5c57f5ba405afdf61c6a5c4792a20ec5940))
* replace `bytes_bytearray_to_bool` parser with `bytes_bytearray_to_str` parser ([4f04722](https://github.com/LeeeeT/valtypes/commit/4f0472270c4b9c63e836e2de82d520d28c765c7b))
* rework parsing system ([df6a029](https://github.com/LeeeeT/valtypes/commit/df6a029022d724693176dd33c3e00d21d360711a))
* suppress `__slots__` in `Constrained` subclasses to allow multiple inheritance ([959a36a](https://github.com/LeeeeT/valtypes/commit/959a36a5e5957df3288e5a7a0a0e71855f268558))


### Bug Fixes

* `PathFinder` now works correctly with union types and parsers chains ([f538eb2](https://github.com/LeeeeT/valtypes/commit/f538eb26507d9532b087a9167a3b1b303cf0890a))
* call `__eq__` of superclass instead of returning `NotImplemented` ([664f76c](https://github.com/LeeeeT/valtypes/commit/664f76c501b0c38bc2ce018b49cd72e86b9a7c7e))

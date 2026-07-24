# Native CST Model Access

Native `.cst` project files are not stored in ordinary Git history in this public package.

Reasons include:

- binary-file size and poor line-level diffability;
- software-version and license dependencies;
- the need to verify that each archived run corresponds to the documented final result; and
- reproducibility considerations for Learning Edition solver and mesh restrictions.

The public package provides the engineering report, LaTeX source, analytical Python scripts, selected figures, parameter tables, and numerical-limitations record. A reviewed native-model distribution may later be provided through a GitHub Release, Git LFS, or a separate archival location.

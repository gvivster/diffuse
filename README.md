IN THIS FORK: 
- I'm using Mac.
- I'm adding a branch to add line wrapping, the missing feature that dealbreaks this program otherwise perfect for my needs. 
- I've added dark mode, although I'm not sure if it'll work right for you if you download it. Feel free to experiment if you'd like. I found and implemented this: [[SOLVED] setting dark theme in gtk3 permanently / Newbie Corner / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=296231)
- Ubuntu install helper: run `chmod +x install-ubuntu.sh` once, then `./install-ubuntu.sh` from the repo root to install build deps and build/install Diffuse on Ubuntu.

Original README below.

- Evie (gvivster)

<h1 align="center">
  <img
    src="./data/icons/hicolor/scalable/apps/io.github.mightycreak.Diffuse.svg"
    alt="Diffuse"
    width="192"
    height="192"/><br/>
</h1>

<p align="center" style="margin-top: 2em">
  <a href="https://flathub.org/apps/details/io.github.mightycreak.Diffuse">
    <img width="200" alt="Download on Flathub" src="https://flathub.org/assets/badges/flathub-badge-en.png"/>
  </a>
</p>

<p align="center">
  <a href="https://github.com/MightyCreak/diffuse/actions/workflows/ci.yml">
    <img
      src="https://github.com/MightyCreak/diffuse/actions/workflows/ci.yml/badge.svg"
      alt="CI status"/>
  </a>
  <a href="https://repology.org/project/diffuse/versions">
    <img src="https://repology.org/badge/tiny-repos/diffuse.svg" alt="Packaging status">
  </a>
</p>

Diffuse is a graphical tool for merging and comparing text files. Diffuse is
able to compare an arbitrary number of files side-by-side and gives users the
ability to manually adjust line matching and directly edit files. Diffuse can
also retrieve revisions of files from several VCSs for comparison and merging.

Some key features of Diffuse:

* Ability to compare and merge an arbitrary number of files side-by-side (n-way
  merges)
* Line matching can be manually corrected by the user
* Ability to directly edit files
* Syntax highlighting
* Supports several VCS: [Bazaar][bzr], [CVS][cvs], [Darcs][darcs], [Git][git],
  [Mercurial][hg], [Monotone][mtn], [RCS][rcs] and [Subversion][svn]
* Unicode support
* Unlimited undo
* Easy keyboard navigation

[bzr]: https://bazaar.canonical.com
[cvs]: https://cvs.nongnu.org
[darcs]: http://darcs.net
[git]: https://git-scm.com
[hg]: https://www.mercurial-scm.org
[mtn]: https://www.monotone.ca
[rcs]: https://www.gnu.org/software/rcs/
[svn]: https://subversion.apache.org

## Documentation

For a more detailed documentation for users, translators and developers, see
the [documentation](docs/).

## Contact

Discuss with us on Matrix at [#diffuse:matrix.org](https://matrix.to/#/#diffuse:matrix.org).

## Licenses

Diffuse is under the [GPLv2](COPYING).

The file [io.github.mightycreak.Diffuse.appdata.xml.in](data/io.github.mightycreak.Diffuse.appdata.xml.in)
is licensed under the [FSF-AP](https://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html)
license.

Copyright (C) 2006-2019 Derrick Moser <derrick_moser@yahoo.com>  
Copyright (C) 2015-2023 Romain Failliot <romain.failliot@foolstep.com>

Icon made by [@jimmac](https://github.com/jimmac).

This repository is a fork of the original project on SourceForge, which doesn't
seem to be maintained anymore: <https://sourceforge.net/projects/diffuse/>.

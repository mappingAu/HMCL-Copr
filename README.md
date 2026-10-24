# HMCL Copr

RPM packaging for [HMCL](https://github.com/HMCL-dev/HMCL) (Hello Minecraft!
Launcher), built automatically in the
[mapping1/HMCL](https://copr.fedorainfracloud.org/coprs/mapping1/HMCL/) Copr
project and tracking the latest upstream release.

## Installation

```sh
sudo dnf copr enable mapping1/HMCL
sudo dnf install hmcl
```

Launch **HMCL** from the application menu, or run `hmcl` / `hmcl-stable` in a
terminal.

## What the package contains

| Path | Purpose |
| --- | --- |
| `/usr/share/java/hmcl/hmcl.jar` | HMCL, as published in the upstream GitHub release |
| `/usr/bin/hmcl-stable` | Launcher script (`/usr/bin/hmcl` is a symlink to it) |
| `/usr/share/applications/hmcl-stable.desktop` | Desktop entry |
| `/usr/share/icons/hicolor/256x256/apps/hmcl-stable.png` | Application icon |
| `/usr/share/licenses/hmcl/LICENSE` | GPL-3.0-or-later license text |

The package requires `java-25-openjdk` and `openjfx`; the launcher passes the
distribution JavaFX modules to the JVM with `--module-path`, so HMCL does not
have to download JavaFX into the user's home directory on first start.

HMCL keeps its data in `$XDG_DATA_HOME/hmcl` (`~/.local/share/hmcl` by
default). Set `HMCL_USER_HOME`, `HMCL_LOCAL_HOME` or `HMCL_JAVA_OPTS` to
override the defaults, exactly like the upstream `.deb` launcher.

## How it is automated

1. [`.github/workflows/update-hmcl-version.yml`](.github/workflows/update-hmcl-version.yml)
   runs once a day (and on demand). It reads the latest HMCL release from the
   GitHub API, and when the version differs from `Version:` in `hmcl.spec` it
   bumps the spec, resets `Release:` and prepends a `%changelog` entry before
   pushing to `main`.
2. The push triggers [packit](https://packit.dev) (the `commit` job in
   [`.packit.yaml`](.packit.yaml)). Packit downloads
   `HMCL-<version>.jar` from the upstream release with the `create-archive`
   action, builds an SRPM and submits it to the
   [mapping1/HMCL](https://copr.fedorainfracloud.org/coprs/mapping1/HMCL/)
   Copr project.
3. Pull requests get their own test build through the `pull_request` job.

Everything is driven by the `Version:` field in `hmcl.spec` — there is no
second, hidden version to keep in sync.

## Building locally

```sh
sudo dnf install rpm-build rpmdevtools desktop-file-utils
make srpm   # out/hmcl-<version>-1.<dist>.src.rpm
make rpm    # out/noarch/hmcl-<version>-1.<dist>.noarch.rpm
```

`make` downloads the jar referenced by `Source0` first (`make fetch`), which
needs network access. To build the SRPM manually:

```sh
spectool -g hmcl.spec
rpmbuild -bs --define "_sourcedir $PWD" --define "_srcrpmdir $PWD" hmcl.spec
```

## Repository layout

```
hmcl.spec                     RPM spec file (single source of truth for the version)
hmcl-stable                   launcher script installed as /usr/bin/hmcl-stable
hmcl-stable.desktop           desktop entry
hmcl-stable.png               256x256 application icon
Makefile                      local SRPM/RPM build helpers
.packit.yaml                  packit configuration (Copr builds)
.github/workflows/            daily upstream version tracking
LICENSE                       GPL-3.0-or-later
```

## License

The packaging files are licensed under GPL-3.0-or-later, the same license as
HMCL itself. See [LICENSE](LICENSE).

# HMCL is published by upstream as a prebuilt jar only (see Source0):
# there is no source tarball to build from.  This package repackages that
# release artifact and adds the desktop integration upstream ships in its
# .deb package (launcher, .desktop file, icon).

Name:           hmcl
Version:        3.16.4
Release:        1%{?dist}
Summary:        Hello Minecraft! Launcher
License:        GPL-3.0-or-later
URL:            https://github.com/HMCL-dev/HMCL

Source0:        https://github.com/HMCL-dev/HMCL/releases/download/v%{version}/HMCL-%{version}.jar
Source1:        hmcl-stable
Source2:        hmcl-stable.desktop
Source3:        hmcl-stable.png
Source4:        LICENSE

BuildArch:      noarch
BuildRequires:  desktop-file-utils

Requires:       java-25-openjdk
Requires:       openjfx
Requires:       hicolor-icon-theme
Recommends:     java-25-openjdk-devel

%description
HMCL (Hello Minecraft! Launcher) is an open-source, cross-platform Minecraft
launcher with a JavaFX user interface.  It can install and launch game
versions, mod loaders (Forge, NeoForge, Fabric, Quilt) and mods, create
isolated instances for different configurations, and manage Microsoft,
Mojang and third-party accounts.

%prep
# Nothing to prepare: the jar is a prebuilt upstream artifact and the
# launcher, desktop file, icon and license are shipped in this repository.

%build
# Nothing to build, upstream only ships the compiled jar.

%install
# /usr/share/java is spelled out instead of using %{_javadir}: that macro comes
# from javapackages-filesystem, which is not present in a minimal Copr
# buildroot and would otherwise remain unexpanded.
install -d %{buildroot}/usr/share/java/%{name}
install -m 644 %{SOURCE0} %{buildroot}/usr/share/java/%{name}/%{name}.jar

install -d %{buildroot}%{_bindir}
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/hmcl-stable
ln -s hmcl-stable %{buildroot}%{_bindir}/hmcl

install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE2}

install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/hmcl-stable.png

install -d %{buildroot}%{_licensedir}/%{name}
install -m 644 %{SOURCE4} %{buildroot}%{_licensedir}/%{name}/LICENSE

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/hmcl-stable.desktop

%files
%license %{_licensedir}/%{name}/LICENSE
/usr/share/java/%{name}/%{name}.jar
%{_bindir}/hmcl
%{_bindir}/hmcl-stable
%{_datadir}/applications/hmcl-stable.desktop
%{_datadir}/icons/hicolor/256x256/apps/hmcl-stable.png

%changelog
* Sun Oct 25 2026 HMCL Copr automation <noreply@github.com> - 3.16.4-1
- Update to HMCL 3.16.4

* Sat Oct 24 2026 mapping1 <apply0@outlook.com> - 3.16.4-1
- Update to HMCL 3.16.4
- Install the release jar and a launcher that actually points at it; the
  previous launcher exec'd a .sh file that the package never installed
- Use the distribution openjfx modules instead of letting HMCL download
  JavaFX into the user's home directory on first start
- Drop the duplicated usr/ tree and move the spec to the repository root so
  that packit's sourcedir contains the launcher, desktop file and icon
- Ship the GPL text and validate the desktop entry at build time

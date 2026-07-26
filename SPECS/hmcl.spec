# 3.15.2无实际作用 仅作占位
%global jar_version 3.15.2

Name:           hmcl
# 占位
Version:        3.15.2
Release:        1%{?dist}
Summary:        Hello Minecraft! Launcher

License:        GPL-3.0-or-later
URL:            https://github.com/HMCL-dev/HMCL

Source0:        %{name}-%{version}.tar.gz
Source1:        https://github.com/HMCL-dev/HMCL/releases/download/v%{jar_version}/HMCL-%{jar_version}.jar

BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  desktop-file-utils

Requires:       java-25-openjdk
Requires:       openjfx
Recommends:     java-25-openjdk-devel
Requires:       hicolor-icon-theme

%description
HMCL is an open-source, cross-platform Minecraft launcher.

%prep
%setup -q

%install
rm -rf %{buildroot}

# --- JAR ---
install -d %{buildroot}%{_javadir}/hmcl
install -m 644 %{SOURCE1} %{buildroot}%{_javadir}/hmcl/HMCL-%{jar_version}.jar

# --- 启动脚本 ---
install -d %{buildroot}%{_bindir}
install -m 755 hmcl-stable %{buildroot}%{_bindir}/hmcl-stable

# --- Desktop 文件 ---
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  hmcl-stable.desktop

# --- 图标 ---
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 hmcl-stable.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/hmcl-stable.png

%files
%{_javadir}/hmcl/HMCL-%{jar_version}.jar
%{_bindir}/hmcl-stable
%{_datadir}/applications/hmcl-stable.desktop
%{_datadir}/icons/hicolor/256x256/apps/hmcl-stable.png

%changelog
* Thu Jul 24 2025 mapping1 <apply0@outlook.com> - 3.15.2-1
- 

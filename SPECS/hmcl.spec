Name:           hmcl
Version:        1.0
Release:        1%{?dist}
Summary:        Hello Minecraft! Launcher

License:        GPL-3.0-or-later
URL:            https://github.com/HMCL-dev/HMCL

Source0:        https://github.com/HMCL-dev/HMCL/releases/download/v%{version}/HMCL-%{version}.jar
Source1:        hmcl-stable
Source2:        hmcl-stable.desktop
Source3:        hmcl-stable.png

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
# 创建编译目录
mkdir -p build

# 魔改
cp %{_specdir}/../hmcl-stable . 2>/dev/null || true
cp %{_specdir}/../hmcl-stable.desktop . 2>/dev/null || true
cp %{_specdir}/../hmcl-stable.png . 2>/dev/null || true

%build
jar tf %{SOURCE0} > /dev/null 2>&1

%install
rm -rf %{buildroot}

# --- JAR ---
install -d %{buildroot}%{_javadir}/hmcl
install -m 644 %{SOURCE0} %{buildroot}%{_javadir}/hmcl/HMCL-%{version}.jar

# --- 启动脚本 ---
install -d %{buildroot}%{_bindir}
# 优先取本地解出的，取不到则取 %{SOURCE1}
install -m 755 hmcl-stable %{buildroot}%{_bindir}/hmcl-stable 2>/dev/null || install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/hmcl-stable

# --- Desktop 文件 ---
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  hmcl-stable.desktop 2>/dev/null || desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

# --- 图标 ---
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 hmcl-stable.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/hmcl-stable.png 2>/dev/null || install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/hmcl-stable.png

%files
%{_javadir}/hmcl/HMCL-%{version}.jar
%{_bindir}/hmcl-stable
%{_datadir}/applications/hmcl-stable.desktop
%{_datadir}/icons/hicolor/256x256/apps/hmcl-stable.png

%changelog
* Thu Jul 24 2025 mapping1 <apply0@outlook.com> - 3.15.2-1
- Initial RPM packaging

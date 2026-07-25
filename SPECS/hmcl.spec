Name:           hmcl
Version:        3.15.2
Release:        1%{?dist}
Summary:        Hello Minecraft! Launcher

License:        GPL-3.0-or-later
URL:            https://hmcl.huangyuhui.net/
URL:            https://github.com/HMCL-dev/HMCL
Source0:        https://github.com/HMCL-dev/HMCL/releases/download/latest/HMCL-%{version}.jar
Source1:        hmcl-stable.desktop
Source2:        hmcl-stable
Source3:        hmcl-stable.png

BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  desktop-file-utils

# JRE作为依赖
Requires:       java-25-openjdk
Requires:       openjfx
# JDK作为弱依赖
Recommends:     java-25-openjdk-devel
Requires:       hicolor-icon-theme

%description
HMCL is an open-source, cross-platform Minecraft launcher that supports Mod Management, Game Customizing, ModLoader Installing (Forge, NeoForge, Cleanroom, Fabric, Legacy Fabric, Quilt, LiteLoader, and OptiFine), Modpack Creating, UI Customization, and more.

HMCL has amazing cross-platform capabilities. Not only does it run on different operating systems like Windows, Linux, macOS, and FreeBSD, but it also supports various CPU architectures such as x86, ARM, RISC-V, MIPS, and LoongArch. You can easily enjoy Minecraft across different platforms through HMCL.

%prep
mkdir -p build

%build
jar tf %{SOURCE0} > /dev/null 2>&1

%install
rm -rf %{buildroot}

# --- JAR ---
install -d %{buildroot}%{_javadir}/hmcl
install -m 644 %{SOURCE0} %{buildroot}%{_javadir}/hmcl/HMCL-%{version}.jar

# --- 启动脚本 ---
install -d %{buildroot}%{_bindir}
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/hmcl-stable

# --- Desktop 文件 ---
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# --- 图标 ---
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 %{SOURCE3} \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/hmcl-stable.png

%files
%{_javadir}/hmcl/HMCL-%{version}.jar
%{_bindir}/hmcl-stable
%{_datadir}/applications/hmcl-stable.desktop
%{_datadir}/icons/hicolor/256x256/apps/hmcl-stable.png

%changelog
* Thu Jul 24 2025 mapping1 <apply0@outlook.com> - 3.15.2-1
- Initial RPM packaging of HMCL 3.15.2-1

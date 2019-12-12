%global srcname sideload
%global appname io.elementary.sideload

Name:           elementary-sideload
Summary:        Sideload flatpaks on Pantheon
Version:        1.0.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/sideload
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       hicolor-icon-theme

%description
Sideload is a simple application that lets users install flatpaks on
Pantheon without needing to use a command line application.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license LICENSE
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Dec 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191128.162518.ec740aa7-1
- Initial snapshot build.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- Initial packaging.


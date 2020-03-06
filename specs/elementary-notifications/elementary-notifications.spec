%global srcname     notifications
%global appname     io.elementary.notifications

Name:           elementary-notifications
Version:        0+git%{date}.%{commit}
Release:        1%{?dist}
Summary:        GTK Notifications Server
License:        GPLv3+

URL:            https://github.com/elementary/notifications
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(granite) >= 5.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)

%description
elementary Notifications is a GTK notification server for Pantheon.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/%{appname}

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Mar 06 2020 Fabio Valentini <decathorpe@gmail.com> - 0+git200306.182133.6da7a217-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0+git200301.150907.609c650e-1
- Update to latest snapshot.

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0+git200225.220857.676c175b-1
- Initial snapshot build setup.


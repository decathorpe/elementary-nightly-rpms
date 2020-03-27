%global srcname sideload
%global appname io.elementary.sideload

Name:           elementary-sideload
Summary:        Sideload flatpaks on Pantheon
Version:        1.0.1+git%{date}.%{commit}
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
* Fri Mar 27 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200327.180947.ed36510c-1
- Update to latest snapshot.

* Tue Mar 24 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200324.180941.3ff61f62-1
- Update to latest snapshot.

* Thu Mar 19 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200319.180937.819cb590-1
- Update to latest snapshot.

* Tue Mar 17 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200317.140931.cfc6e88d-1
- Update to latest snapshot.

* Sat Mar 14 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200314.210930.a4988081-1
- Update to latest snapshot.

* Wed Mar 11 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200311.160922.f47b371b-1
- Update to latest snapshot.

* Sun Mar 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200308.110916.d7f9b25a-1
- Update to latest snapshot.

* Fri Mar 06 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200306.170916.1758c432-1
- Update to latest snapshot.

* Wed Mar 04 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200304.004859.2b6d6448-1
- Update to latest snapshot.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200302.230909.7dc865be-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200301.150928.b268895d-1
- Update to latest snapshot.

* Thu Feb 27 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200227.150913.33bf5cd3-1
- Update to latest snapshot.

* Wed Feb 26 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git200226.064147.6b9b78c6-1
- Update to version 1.0.1.

* Wed Feb 26 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git200226.064147.6b9b78c6-1
- Update to latest snapshot.

* Wed Feb 26 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git200225.230857.d56030f3-1
- Update to latest snapshot.

* Mon Feb 24 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git200224.160855.db8fe2b3-1
- Update to latest snapshot.

* Sat Feb 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git200208.190829.0c3227b0-1
- Update to latest snapshot.

* Mon Feb 03 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git200203.170819.779ea3db-1
- Update to latest snapshot.

* Sat Jan 25 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git200125.150805.a67243ff-1
- Update to latest snapshot.

* Sat Jan 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git200118.010800.41d71aa3-1
- Update to latest snapshot.

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git200108.000743.79387e13-1
- Update to latest snapshot.

* Sun Dec 29 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191229.052121.64d48a23-1
- Update to latest snapshot.

* Fri Dec 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191227.140722.c8a7d799-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191226.035155.ef70a110-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191220.004431.7f5aeadf-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191218.191209.a8e59fe2-1
- Update to latest snapshot.

* Mon Dec 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191216.192957.0cb73117-1
- Update to latest snapshot.

* Mon Dec 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191216.190014.1add77cc-1
- Update to latest snapshot.

* Mon Dec 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191215.230708.5778153b-1
- Update to latest snapshot.

* Thu Dec 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0+git191128.162518.ec740aa7-1
- Initial snapshot build.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- Initial packaging.


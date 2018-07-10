%global __provides_exclude_from ^%{_libdir}/gala/.*\\.so$

Name:           gala
Summary:        Gala window manager
Version:        0.3.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

# Include a patch to set some settings to match other fedora defaults
Patch0:         00-fedora-default-settings.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(clutter-1.0) >= 1.12.0
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon) >= 3.15.2
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(plank) >= 0.11.0

BuildRequires:  mutter-devel >= 3.18.3


Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# gala provides a generic icon (apps/multitasking-view)
Requires:       hicolor-icon-theme

# gala's multitasking view is activated via dbus
Requires:       dbus


%description
Gala is Pantheon's Window Manager, part of the elementary project.


%package        libs
Summary:        Gala window manager libraries
%description    libs
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the shared libraries.


%package        devel
Summary:        Gala window manager development files
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the development headers.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang gala


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/gala*.desktop


%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig


%files -f gala.lang
%{_bindir}/gala

%{_libdir}/gala/plugins/*

%{_datadir}/applications/gala*.desktop
%{_datadir}/gala/
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multitasking-view.svg


%files libs
%doc AUTHORS
%license COPYING

%dir %{_libdir}/gala
%dir %{_libdir}/gala/plugins

%{_libdir}/libgala.so.0
%{_libdir}/libgala.so.0.0.0


%files devel
%{_includedir}/gala/

%{_libdir}/libgala.so
%{_libdir}/pkgconfig/gala.pc

%{_datadir}/vala/vapi/gala.deps
%{_datadir}/vala/vapi/gala.vapi


%changelog
* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180710.062757.6bdc7188-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180627.173000.8e142b9e-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180607.201553.985baa08-2
- Update default settings patch to cover more settings.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180607.201553.985baa08-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180603.082106.3661cbd7-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180603.070512.da1cd0ef-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180516.055801.60478f32-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180501.175911.f02b776d-1
- Update to version 0.3.1.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180501.175911.f02b776d-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180430.060316.f1a49175-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180318.160621.a71e8c13-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180318.152529.b4537f32-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180314.153929.22f0d957-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180314.082202.95b0f2bb-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180311.212220.6d3253a5-2
- Switch from autotools to meson build.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180311.212220.6d3253a5-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180311.182603.112fc3a7-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180308.204956.b7b74f44-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180305.182210.f74a4c8b-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180214.205526.22e176a4-1
- Update to latest snapshot.

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180130.135930.c0eb426f-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180124.123948.f90fc625-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git180123.154241.d76c89b6-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171217.173134.439fdf6e-4
- Remove icon cache scriptlets.

* Tue Jan 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171217.173134.439fdf6e-3
- Add patch so window buttons match fedora's default layout.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171217.173134.439fdf6e-2
- Merge .spec file from fedora.

* Sun Dec 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171217.173134.439fdf6e-1
- Update to latest snapshot.

* Sat Nov 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171111.173922.a82bb341-1
- Update to latest snapshot.

* Thu Nov 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171109.152045.5cee3d23-1
- Update to latest snapshot.

* Sat Oct 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171007.154035.60ee8709-1
- Update to latest snapshot.

* Wed Oct 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171004.104540.69207916-1
- Update to latest snapshot.

* Sun Oct 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171001.134709.981eff84-1
- Update to latest snapshot.

* Sun Oct 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git171001.115936.1e29ce34-1
- Update to latest snapshot.

* Thu Sep 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git170928.144702.9b68c4b6-1
- Update to latest snapshot.

* Sun Sep 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git170924.154846.6d8df555-1
- Update to latest snapshot.

* Sun Sep 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git170924.082225.bb686ff2-1
- Update to latest snapshot.

* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git170919.161345.4fe5dea2-1
- Update to latest snapshot.

* Sun Sep 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git170917.110754.fb8364ca-1
- Update to latest snapshot.

* Thu Aug 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git170831.211647.cd28b8d3-1
- Update to latest snapshot.

* Thu Aug 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0+git170823.154744.85e9c124-1
- Start doing git snapshots again.

* Wed Aug 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git123.85e9.1
- Update to latest snapshot (git 123-85e9).

* Sat Aug 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git120.87f5a.1
- Update to latest snapshot (git 120-87f5a).

* Mon Jul 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git119.c7d5.1
- Update to latest snapshot (git 119-c7d5).

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.bzr567.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr567.1
- Update to latest snapshot (rev 567).
- De-remove other configurations, now the .desktop files are valid again.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr562.1
- Update to latest snapshot (rev 562).
- Filter provides to exclude internal plugins.
- Remove explicit pkgconfig BR.
- Remove unsupported / broken configurations.
- Fix build with mutter-3.24.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.bzr552.4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr552.4
- Make BR on /usr/bin/pkg-config explicit.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr552.3
- Put plugins and the plugin directory into the right respective subpackages.

* Thu Jan 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr552.2
- Make sure no *.la files are in the packages.

* Thu Jan 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr552.1
- Initial package.



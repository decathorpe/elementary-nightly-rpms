%global __provides_exclude_from ^%{_libdir}/gala/.*\\.so$

Name:           gala
Summary:        Gala window manager
Version:        0.3.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+
URL:            https://launchpad.net/gala

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libtool
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
%autosetup


%build
autoreconf -v -i
%configure
%make_build


%install
%make_install
%find_lang gala

# Remove libtool archives
find %{buildroot} -name '*.la' -print -delete


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/*.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


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



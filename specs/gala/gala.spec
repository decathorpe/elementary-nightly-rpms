%global __provides_exclude_from ^%{_libdir}/gala/.*\\.so$

Name:           gala
Summary:        Gala window manager
Version:        3.2.0+git%{date}.%{commit}
Release:        2%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

# Include a patch to set some settings to match other fedora defaults
Patch0:         00-fedora-default-settings.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  gettext-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mutter328-devel

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

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f gala.lang
%{_bindir}/gala
%{_bindir}/gala-daemon

%{_libdir}/gala/plugins/*

%{_datadir}/applications/gala*.desktop
%{_datadir}/gala/
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%{_datadir}/glib-2.0/schemas/20_elementary.pantheon.wm.gschema.override
%{_datadir}/icons/hicolor/*/apps/multitasking-view.svg
%{_datadir}/metainfo/%{name}.appdata.xml


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
* Sun Feb 23 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200222.140851.62e428a8-2
- Switch back to mutter 3.28.

* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200222.140851.62e428a8-1
- Update to latest snapshot.

* Sun Feb 16 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200216.053230.2b205099-1
- Update to latest snapshot.

* Thu Feb 06 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200206.200825.036d1484-1
- Update to latest snapshot.

* Sat Feb 01 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200201.020817.e33e43dd-1
- Update to latest snapshot.

* Sun Jan 26 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200125.150805.d17ed457-2
- Rebase downstream default settings patch.

* Sat Jan 25 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200125.150805.d17ed457-1
- Update to latest snapshot.

* Wed Jan 22 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200122.173358.c43e2d0b-1
- Update to latest snapshot.

* Mon Jan 20 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200120.200814.34577981-1
- Update to latest snapshot.

* Sun Jan 19 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200119.130803.d5d7c198-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200115.184425.2aa417cd-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200115.150813.7b4246d5-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200115.105058.07d8d6c8-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200115.004421.346e9f0b-1
- Update to latest snapshot.

* Tue Jan 14 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200114.215901.a127d09a-1
- Update to latest snapshot.

* Tue Jan 14 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200114.175852.cdd3bdcf-1
- Update to latest snapshot.

* Tue Jan 14 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200114.092227.6f41f9f6-1
- Update to latest snapshot.

* Thu Jan 09 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200109.204500.42701bf8-1
- Update to latest snapshot.

* Thu Jan 09 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200109.192634.abe5bcc8-1
- Update to latest snapshot.

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git200107.175830.548ec08d-1
- Update to version 3.2.0.

* Tue Jan 07 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git200107.175830.548ec08d-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git200106.180736.a4d51ee5-1
- Update to latest snapshot.

* Sun Dec 29 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191229.052121.b3a0aa69-1
- Update to latest snapshot.

* Fri Dec 27 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191227.130722.2a51ead3-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191226.035156.a268b8b7-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191224.200717.7cb068ce-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191220.004432.3ab1e824-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191218.223802.eca2bb1d-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191218.191211.09728e0a-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191217.231404.b2eca5be-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191217.002519.fd3af538-1
- Update to latest snapshot.

* Mon Dec 16 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191216.191132.82b1bd5d-1
- Update to latest snapshot.

* Sat Dec 14 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191214.221709.f7a89d86-1
- Update to latest snapshot.

* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191213.200704.c42b26bb-1
- Update to latest snapshot.

* Wed Dec 11 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191211.011637.4782c185-2
- Package and verify appdata file.

* Wed Dec 11 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191211.011637.4782c185-1
- Update to latest snapshot.

* Tue Dec 10 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191210.190104.8b48305d-1
- Update to latest snapshot.

* Tue Dec 10 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191210.180120.52d639ae-1
- Update to latest snapshot.

* Tue Dec 10 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191210.175928.13eef471-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191121.200052.309d594a-1
- Update to latest snapshot.

* Wed Nov 20 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191120.181332.f0d2b2d5-1
- Update to latest snapshot.

* Wed Nov 20 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191120.171051.2c22f2de-1
- Update to latest snapshot.

* Mon Nov 18 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191118.211808.7845530b-1
- Update to latest snapshot.

* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191113.205515.70cfe7e6-2
- Switch to mutter 3.3x.

* Wed Nov 13 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191113.205515.70cfe7e6-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191104.193008.8540e845-2
- Add missing BR: mesa-libEGL-devel.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191104.193008.8540e845-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191104.171825.d1d415c9-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191031.212238.0f0724c9-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191029.230921.4a07494a-1
- Update to latest snapshot.

* Mon Oct 28 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191028.163059.58988457-1
- Update to latest snapshot.

* Tue Oct 22 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191022.161957.8b2afe31-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git191001.225020.29c74411-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190924.173352.8444dd41-1
- Update to latest snapshot.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190905.201843.49d1d8ff-1
- Update to latest snapshot.

* Sun Jul 21 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190721.085523.50694796-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190716.000112.da85223f-1
- Update to latest snapshot.

* Fri Jul 12 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190712.141302.a790d2d0-1
- Update to latest snapshot.

* Tue Jul 02 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190701.233903.5f1dbf15-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190626.204303.087abfc5-1
- Update to latest snapshot.

* Tue Jun 25 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190625.002219.dd98e006-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190531.224437.10248135-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190514.123328.3ae100da-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190514.092050.903bc6c5-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190514.083749.ca32785f-1
- Update to latest snapshot.

* Sat May 11 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190511.111215.4459c591-1
- Update to latest snapshot.

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190318.134258.e50b0642-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190307.184639.2c610b3b-1
- Update to latest snapshot.

* Sat Mar 02 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190302.011216.395670ec-1
- Update to latest snapshot.

* Wed Feb 27 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190227.165409.6da349e9-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190209.212415.1a96644c-1
- Update to latest snapshot.

* Fri Feb 08 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190208.132549.bedd70d6-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190207.183659.dca99e0c-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190207.160237.df0022c4-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190207.082425.bbd5963d-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190206.124717.9493139c-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190206.001502.74e7541c-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190128.081758.6654145b-1
- Update to latest snapshot.

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git190123.205801.fe52fb12-1
- Update to latest snapshot.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181216.003635.7f1e392e-1
- Update to latest snapshot.

* Wed Dec 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181205.094419.66a95e05-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181121.232447.cf8d4556-1
- Update to latest snapshot.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181114.154410.a2a4683b-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181109.074048.f44e95d8-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181108.132635.c9c6338d-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181025.165313.be16d4a0-3
- Occasional mass rebuild.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181025.165313.be16d4a0-2
- Rebase default settings patch.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181025.165313.be16d4a0-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181020.160204.a1bad267-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181017.145641.fe9f48ae-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181003.222310.feffbf8a-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180917.225434.9747bd61-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180910.221652.1970bac8-2
- Adapt to upstream file changes.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180910.221652.1970bac8-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180910.232546.4d5a5669-2
- Adapt to upstream file changes.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180910.232546.4d5a5669-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180910.221652.1970bac8-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180910.132714.2995cd64-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180910.124542.d38aed64-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180729.015903.15f722ac-3
- Adapt for mutter328 compat package.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180729.015903.15f722ac-2
- Occasional mass rebuild.

* Sun Jul 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180729.015903.15f722ac-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180715.000058.95026778-1
- Update to latest snapshot.

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


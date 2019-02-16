%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname applications-menu
%global appname io.elementary.desktop.wingpanel.applications-menu

Name:           wingpanel-applications-menu
Summary:        Lightweight and stylish app launcher
Version:        2.4.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vala >= 0.26.2
BuildRequires:  vala-tools

BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.1
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(unity)
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       redhat-menus

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

Provides:       slingshot-launcher
Obsoletes:      slingshot-launcher


%description
The lightweight and stylish app launcher from elementary.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang slingshot


%files -f slingshot.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/menus/pantheon-applications.menu

%{_libdir}/wingpanel/libslingshot.so

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml


%changelog
* Sat Feb 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190216.181302.66a5c1b8-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190212.205219.ae95dfb7-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190211.202823.bf11edf4-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190211.070118.4171a610-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190211.051356.baa96e72-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190210.233148.93f60085-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190210.213343.63dda5ad-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190210.125832.63d7bf1d-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190210.080134.d5df6c55-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190209.172523.18162541-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190209.121545.7c194260-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190209.111112.997e1c05-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190209.083002.814ef2ce-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190209.064507.2b7657e8-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190209.021440.4b38dd37-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190209.000236.72e1cc1a-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190207.000734.d4c8c4ae-1
- Update to latest snapshot.

* Sun Jan 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190127.211728.58cd96a4-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190125.184250.c6b550c5-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190125.000227.ec81394a-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190122.190208.607d03d6-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190122.185805.97768a92-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190122.120541.353d692f-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190122.095145.1ed7bbef-1
- Update to latest snapshot.

* Wed Jan 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190116.000409.78b8feb3-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190115.133958.501bde64-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190114.001128.f5391d44-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190111.000715.2e15807e-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190109.191342.63e2d00b-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190106.181451.3c3c27ec-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190104.000924.d1533dbf-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190102.220510.7e357c0e-1
- Update to latest snapshot.

* Wed Dec 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181226.174415.6ea0fa7a-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181224.104804.2f956540-1
- Update to latest snapshot.

* Sat Dec 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181222.000941.b68e7139-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181217.105444.8c51022c-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181217.010359.a28375c7-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181215.160138.3ed8e54e-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181215.160037.e2ce585c-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181213.141404.7f3ca21d-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181212.183422.c16fa4b0-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181212.072445.c342b0f4-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181212.050741.20f47434-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181212.001216.3171ed60-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181211.235225.b96afd0b-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181211.211408.d91e9569-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181211.173422.a81f0520-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181211.145342.d6a38f51-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181211.124522.75993f99-2
- Require granite >= 5.2.1.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181211.124522.75993f99-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181211.110640.83710e6e-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181210.165520.c61816e7-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181207.184124.99898341-1
- Update to version 2.4.1.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181207.184124.99898341-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181207.171106.a04df24b-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181207.031113.06a82e86-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181206.201008.2d872b84-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181206.020430.c3e1ab06-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181202.001539.5fa09c8e-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181202.000050.0317f6f8-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181121.181044.806f20cd-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181106.165957.fc7ecfcd-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181106.154725.286a09af-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181104.221058.81f30ed3-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181103.091010.2507f84b-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181101.000332.3c20695f-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181101.000332.3c20695f-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181028.140553.cbaecfe9-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181023.190410.3ab08d35-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181023.175640.f9de4d28-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181022.165602.60ec0888-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181019.183203.316d80e2-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181018.001142.5df78a4d-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181017.000820.c07857e2-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181015.000846.cfe57d18-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git181009.225707.e6bfba4f-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git180927.211928.8bdec5ec-1
- Update to latest snapshot.

* Sat Sep 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git180922.001134.adc92080-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git180921.000746.5051c0af-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git180918.154103.b5b636b2-1
- Update to version 2.4.0.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180918.154103.b5b636b2-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180907.000701.b7c07302-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180831.000651.0a98042c-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180830.000851.aaca1962-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180829.000420.1556692c-1
- Update to latest snapshot.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180827.234322.5316955d-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180819.001020.e517d2d6-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180812.141237.3d249981-2
- Occasional mass rebuild.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180812.141237.3d249981-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180722.000426.6e00df69-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180721.183344.546fc043-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180719.000351.ada33df7-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180718.180841.2f21cd84-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180717.155007.5f25c487-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180716.192753.62979121-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180713.000449.d3e7e3bd-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180709.205554.436f4342-1
- Update to version 2.3.0.



%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname applications-menu
%global appname io.elementary.wingpanel.applications-menu

Name:           wingpanel-applications-menu
Summary:        Lightweight and stylish app launcher
Version:        2.5.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.26.2

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
BuildRequires:  pkgconfig(unity) >= 4.0.0
BuildRequires:  pkgconfig(wingpanel-2.0) >= 2.1.0
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
%meson
%meson_build


%install
%meson_install

%find_lang slingshot


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f slingshot.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/menus/pantheon-applications.menu

%{_libdir}/wingpanel/libslingshot.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.applications-menu.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Jan 24 2020 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git200124.020802.c4153a7c-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git200121.160759.5d99d16b-1
- Update to latest snapshot.

* Tue Jan 07 2020 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git200107.195351.49a6495e-1
- Update to latest snapshot.

* Fri Jan 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git200103.220734.ecfa2d55-1
- Update to latest snapshot.

* Fri Dec 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191227.111937.75740f69-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191226.181633.8849d1a6-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191226.010830.dc06432f-1
- Update to latest snapshot.

* Wed Dec 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191225.151725.36135066-1
- Update to latest snapshot.

* Wed Dec 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191224.234134.03622e05-1
- Update to latest snapshot.

* Sun Dec 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191222.113230.7c55b65b-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191220.194933.a3ddfc0b-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191219.130710.0ce22015-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191217.225401.a43dc0ee-1
- Update to latest snapshot.

* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191213.175704.f9d7b442-1
- Update to latest snapshot.

* Thu Dec 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191212.123352.64696fe4-1
- Update to latest snapshot.

* Tue Dec 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191210.124319.f190b0a7-1
- Update to latest snapshot.

* Mon Dec 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191209.212917.1d33314b-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191204.212453.3af4e0eb-1
- Update to latest snapshot.

* Thu Nov 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191128.172442.d01d74e4-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0+git191125.170700.5fe45e08-1
- Update to version 2.5.0.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191125.170700.5fe45e08-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191125.164336.665e22c9-1
- Update to latest snapshot.

* Sat Nov 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191123.052432.4656b54e-1
- Update to latest snapshot.

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191119.212427.ab967a5f-1
- Update to latest snapshot.

* Mon Nov 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191118.152422.2e4f93b6-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191116.162419.4475d84f-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191115.185420.b5fe382c-1
- Update to latest snapshot.

* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191114.152418.ef057b8d-1
- Update to latest snapshot.

* Tue Nov 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191112.152413.434cdc46-1
- Update to latest snapshot.

* Sun Nov 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191110.202411.8b9660f8-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191109.122515.abc0b69f-1
- Update to latest snapshot.

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191107.213015.68672d78-2
- Package and verify appdata file.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191107.213015.68672d78-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191106.175332.79b226df-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191106.144940.28af00c1-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191105.163030.c04ff137-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191105.132432.53243d68-1
- Update to latest snapshot.

* Mon Oct 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191014.161224.31c1e042-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191009.215254.11698800-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191008.165113.073bdc62-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191008.151735.0e32f138-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191008.062247.1556b119-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191008.054653.86273940-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191007.202453.bb11ff22-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191007.153648.086fbb20-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191007.144235.851559d8-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191005.102347.3763c4cd-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git191003.151933.f5ca305b-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190929.042341.7989a84a-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190926.000717.03d930a9-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190925.013603.2ba302e0-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190924.181244.b4d27179-1
- Update to latest snapshot.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190923.225845.81ebb7af-1
- Update to latest snapshot.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190923.162410.7da58058-1
- Update to latest snapshot.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190923.024357.fae01ee7-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190920.173817.971d294c-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190920.011958.24a5146a-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190919.173437.6f3458d8-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190917.225320.ccfba82a-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190917.092815.84bce93b-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190916.181043.f15d1343-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190916.175958.f8afdcaf-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190916.050940.b1c8a20d-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190915.231648.2647cc92-1
- Update to latest snapshot.

* Sun Sep 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190915.223658.11f3935c-1
- Update to latest snapshot.

* Sun Sep 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190915.163336.36c18e7e-1
- Update to latest snapshot.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190913.000040.c5b1c717-1
- Update to latest snapshot.

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190912.225837.ac041481-1
- Update to latest snapshot.

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190912.200732.8db9773e-1
- Update to latest snapshot.

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190912.171518.67d5f3e0-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190911.193116.c23521ac-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190911.150902.98ea1a9f-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190911.090921.a369b6b3-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190911.085042.e9c8b95b-1
- Update to latest snapshot.

* Tue Sep 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190910.194416.79384825-1
- Update to latest snapshot.

* Tue Sep 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190910.184555.4832f0d5-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190909.184624.7367435e-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190909.132323.fcf0e4ae-1
- Update to latest snapshot.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.4+git190905.152301.b9185c91-1
- Update to version 2.4.4.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190905.152301.b9185c91-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190902.132300.a09750b8-1
- Update to latest snapshot.

* Sun Sep 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190901.115153.81cc429d-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190830.062555.ba69cc92-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190829.080050.f73e867d-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190829.075951.65454e79-1
- Update to latest snapshot.

* Wed Aug 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190828.181359.2208f9d3-1
- Update to latest snapshot.

* Wed Aug 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190828.173556.0c91b256-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190826.212245.a8938a2a-1
- Update to latest snapshot.

* Sat Aug 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190823.100214.2f3f4886-2
- Static libraries were removed upstream.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190823.100214.2f3f4886-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190821.001446.b4b851ba-2
- Switch from CMake to meson.

* Wed Aug 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190821.001446.b4b851ba-1
- Update to latest snapshot.

* Wed Aug 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190820.235430.2832eb5f-1
- Update to latest snapshot.

* Fri Aug 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190802.150049.5acb5b6a-1
- Update to latest snapshot.

* Fri Aug 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190802.064003.94de4cf8-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190801.192012.d902eb65-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190801.152457.9a5e3525-1
- Update to latest snapshot.

* Tue Jul 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190723.042819.42ba002c-1
- Update to latest snapshot.

* Tue Jul 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190723.034314.1503bd14-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190626.211748.3c5ae987-1
- Update to latest snapshot.

* Sat Jun 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190615.150618.8a0e8c28-1
- Update to latest snapshot.

* Sun Jun 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190609.102105.3ac7d6b7-1
- Update to latest snapshot.

* Thu Jun 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190606.170354.9d81e6a5-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190531.045737.bb90bdc0-1
- Update to latest snapshot.

* Tue May 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190528.192133.e44ce888-1
- Update to latest snapshot.

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.3+git190516.101036.d5f9c637-1
- Update to version 2.4.3.

* Thu May 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190516.101036.d5f9c637-1
- Update to latest snapshot.

* Mon May 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190506.115246.5f419f1f-1
- Update to latest snapshot.

* Thu Apr 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190425.111430.4a3e7885-1
- Update to latest snapshot.

* Mon Apr 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190422.193206.5ba4328d-1
- Update to latest snapshot.

* Sat Apr 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190420.163325.65f1ebdd-1
- Update to latest snapshot.

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190414.102025.29d34e15-1
- Update to latest snapshot.

* Wed Apr 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190410.205327.bff69e8f-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190408.055330.8b6249ff-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190406.225310.05b89f9d-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190405.215243.ac964158-1
- Update to latest snapshot.

* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190313.162745.91a47e22-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190312.152729.8856b1c9-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190305.172717.b484e954-1
- Update to latest snapshot.

* Fri Mar 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190301.123752.e239eb7e-1
- Update to latest snapshot.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git190222.000625.77247428-1
- Update to latest snapshot.

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



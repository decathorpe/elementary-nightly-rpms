%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_name useraccounts
%global plug_type system
%global plug_rdnn io.elementary.switchboard.useraccounts

Name:           switchboard-plug-useraccounts
Summary:        Switchboard User Accounts Plug
Version:        2.3.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
Switchboard Plug for managing local user accounts.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING COPYRIGHT

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so
%{_libdir}/switchboard/system/pantheon-%{plug_name}/

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml
%{_datadir}/polkit-1/actions/%{plug_rdnn}.policy


%changelog
* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191220.160916.8357b870-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191219.130719.6fdf649f-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191217.195849.e464441f-1
- Update to latest snapshot.

* Sat Dec 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191214.150702.06458529-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191204.212554.f58bd26e-1
- Update to latest snapshot.

* Fri Nov 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191129.002520.ec525353-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191127.202527.e9dfc853-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191125.092507.c137d6f0-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191122.172500.a91a9214-1
- Update to latest snapshot.

* Wed Nov 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191120.171657.e57fcc75-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191115.222540.43249776-1
- Update to version 2.3.0.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191115.222540.43249776-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191107.182542.8072d48e-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191106.002224.7c593e89-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191031.015137.6aa4a171-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191030.164529.7f1ad94c-1
- Update to latest snapshot.

* Thu Oct 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191024.095354.62b2b2c8-1
- Update to latest snapshot.

* Thu Oct 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191017.172440.c67fb7a4-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191009.172353.0c0730c2-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191003.151129.02f93f2d-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190930.142308.2d3c7452-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190925.182830.43732e80-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190925.173419.d8bb8053-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190925.151133.55a7f312-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190924.201052.5042e0a5-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190920.042252.77d5d945-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190917.092248.e56d6982-1
- Update to latest snapshot.

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190912.142239.e99df901-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190907.212310.ee6b79a7-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190906.152230.c41945aa-1
- Update to latest snapshot.

* Sun Sep 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190901.162223.b3f77fe1-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190829.042216.c91e0867-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190827.212215.3c8c9571-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190826.062213.bdc2ec9d-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190823.220833.c1db7f2a-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190822.012207.cfad3b31-1
- Update to latest snapshot.

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190820.042204.34e18585-1
- Update to latest snapshot.

* Fri Aug 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190816.192220.f8bbd481-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190814.193146.d884018a-2
- Adapt to renamed files.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190814.193146.d884018a-1
- Update to latest snapshot.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190814.104845.26794e89-1
- Update to latest snapshot.

* Mon Aug 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190812.172221.f3b53834-1
- Update to latest snapshot.

* Sun Aug 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190811.102216.0ccfa04f-1
- Update to latest snapshot.

* Sun Aug 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190811.093938.e54b0d12-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190731.234121.951c3d55-1
- Update to latest snapshot.

* Thu Jul 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190718.182401.b440a4db-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190717.151407.0b30a9b2-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190626.204633.c9cf5b4d-1
- Update to latest snapshot.

* Sat Jun 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190601.171726.7fb59e40-1
- Update to latest snapshot.

* Sat Jun 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190601.164901.6f5bc2d4-1
- Update to latest snapshot.

* Sat Jun 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190601.111942.6276fb17-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190531.065047.8dedf6f6-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190531.050015.b4b22070-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190531.000408.a55130f0-1
- Update to latest snapshot.

* Tue May 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190528.210402.9a2d20f4-1
- Update to latest snapshot.

* Sat May 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190518.221008.8135deea-1
- Update to latest snapshot.

* Fri May 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190510.084212.0ecee8d1-2
- Adapt to new appdata file.

* Fri May 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190510.084212.0ecee8d1-1
- Update to latest snapshot.

* Tue Apr 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190423.183605.8091bbe2-1
- Update to latest snapshot.

* Sat Mar 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190315.165119.4a0f2432-1
- Update to version 2.2.1.

* Fri Mar 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190315.165119.4a0f2432-1
- Update to latest snapshot.

* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190313.182601.d0454d43-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190312.000711.dd1b871b-2
- Bump granite requirement to >= 5.2.0.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190312.000711.dd1b871b-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190311.233944.d4fcbb15-1
- Update to latest snapshot.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190222.125613.91594fb0-1
- Update to latest snapshot.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190222.000546.386afefb-1
- Update to latest snapshot.

* Tue Feb 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190219.224431.bebdff9c-1
- Update to latest snapshot.

* Mon Feb 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190218.184836.2637477c-1
- Update to latest snapshot.

* Sun Feb 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190217.202103.17b8ab8a-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190125.000159.e4bab474-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190115.000643.a045280d-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190114.001054.ca27d7e2-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190106.222707.ed4c709a-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181219.000825.a61030b4-1
- Update to latest snapshot.

* Fri Dec 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181214.221002.cafdac8d-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181211.160515.c4cc406f-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181202.065217.2e676747-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181124.121029.95f40ae6-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181116.082743.d30b9daf-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181110.220500.b2c730df-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181107.141010.9bf3c077-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181106.211843.d1683a83-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181106.064632.2fdfae91-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181031.015114.a70d2bab-2
- Occasional mass rebuild.

* Wed Oct 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181031.015114.a70d2bab-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181029.080649.5900f5dd-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181025.071815.1a760028-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181023.091642.cff00361-1
- Update to version 2.2.0.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181023.091642.cff00361-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181021.114431.3aed411c-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181020.133207.0cb137cd-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181018.001123.e03988c7-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181016.000917.486cfb37-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181015.144605.40e97ee4-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181014.001533.f0a178ea-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181013.123610.4d9ba1e2-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181012.000543.7d91cb79-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181011.175741.b4a95a11-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181011.004832.772c6dc0-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181010.211755.a64498a5-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181010.170530.8135aa1f-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181010.141856.cda3b773-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181009.155249.0c8b4c7b-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181009.134435.089a1d62-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7+git181009.092300.e3af8591-1
- Update to version 2.1.7.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git181009.092300.e3af8591-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git181009.061827.8b2221b1-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git181009.015849.c677aea8-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git181009.005919.82a60554-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git181008.204636.d1d09d74-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git181008.182019.de2c4196-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git181003.001115.5dcf1af8-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git181002.000431.cfadd178-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180920.000515.a155823e-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180919.001003.76ae3c2d-1
- Update to latest snapshot.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180912.092136.87fd35fd-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180911.190118.0d866ae3-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180910.221523.faa475ce-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180907.000642.2f529fd7-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180830.000825.e3520a99-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180829.164415.a8f4e315-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180722.120930.eab7dc80-2
- Occasional mass rebuild.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180722.120930.eab7dc80-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180711.000914.24265bc3-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180618.000618.ba35d582-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180615.001149.d5d5edf3-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180614.084502.e635df8b-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180612.073034.c94192f3-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180611.175308.7343a66a-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180605.190905.66788a06-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180605.180201.84a5c7e4-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180605.122448.c5e504df-2
- Adapt to CMake -> meson switch.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180605.122448.c5e504df-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180604.001033.ffd75e0d-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180602.000715.1dcd0407-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180601.000855.2af354a0-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180531.000354.c4b72823-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180530.000503.f422ffdd-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180528.091343.5e56c7a8-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180528.000337.0c8b8681-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180525.204643.4604ebf6-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180512.001232.aec96028-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180511.033905.706c44f0-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180510.172151.a4756cf8-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180510.000105.25e5440d-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180507.172853.c81e19b6-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180507.000340.8e22994b-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180503.000639.78ba1ee5-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180501.160737.245c41a0-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180429.142601.e7afe2f3-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180425.000401.1772b9a7-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180421.001159.6f10b266-1
- Update to latest snapshot.

* Thu Apr 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180419.191355.72b4e528-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180415.001049.53ce7a91-1
- Update to latest snapshot.

* Thu Apr 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180412.174206.cf4e8d3b-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180401.112114.f98f9aa6-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180328.000424.62084a4c-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180326.000625.46914600-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180325.170717.8eb30c7d-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180321.195347.7b454234-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180317.203707.2c53850b-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180317.001013.77b791a1-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180314.000251.dd25d4ef-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180313.025321.272b54fb-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180312.154032.ac241d9b-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180311.203437.ff214073-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180311.183651.aa5b75e5-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180311.132812.8a5a5e35-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180308.144557.6244445e-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180227.201145.762fb1fd-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180224.000458.75c2af2a-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180222.000553.85804afd-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180213.202116.c220ba63-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180212.212133.e563e14a-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180211.000746.e72053a8-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180208.225818.0366f157-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180208.203421.fba5c502-1
- Update to latest snapshot.

* Wed Feb 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git180207.101733.de3be02b-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git171220.000559.879077ac-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git171118.235431.4ae0335e-2
- Merge .spec file from elementary-stable.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git171118.235431.4ae0335e-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git171117.184014.64bba779-1
- Update to latest snapshot.

* Wed Oct 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git171018.121336.8994d2a8-1
- Update to latest snapshot.

* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.6+git171010.185656.b50cb0d1-1
- Update to version 0.1.6.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git171010.185656.b50cb0d1-1
- Update to latest snapshot.

* Mon Oct 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git171009.021907.6c3ee7b9-1
- Update to latest snapshot.

* Wed Sep 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git170913.000939.fa62aca5-1
- Update to latest snapshot.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git170912.150849.7787282a-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git170817.000753.f4347477-1
- Update to latest snapshot.

* Sun Aug 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git170813.000510.6017d2fb-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git170704.090549.3454e61b-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git170703.200256.64ff8008-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git170628.130459.d3852f36-1
- Update to version 0.1.5.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170628.130459.d3852f36-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170628.124330.bde091a9-1
- Update to latest snapshot.

* Sat Jun 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170622.221904.c672f026-1
- Update to latest snapshot.

* Thu Jun 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170622.185228.b1c7bcc6-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170617.184144.fa919161-1
- Update to latest snapshot.

* Sun Jun 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170604.173131.234545c7-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170603.180607.0f328bf1-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170603.174129.2191cf00-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170603.093000.ef32a0c5-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170602.190959.baaa387f-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170602.174636.0edab0c1-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170601.210323.d96acc5b-1
- Update to latest snapshot.

* Wed May 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170530.190955.958ebde9-2
- Adapt to upstream file changes.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170530.190955.958ebde9-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170530.170230.ea8ff941-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170529.231024.56c0ae8b-1
- Update to latest snapshot.

* Sat May 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170527.130319.4d1255d6-1
- Update to latest snapshot.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git170522.193828.bf51c456-1
- Update to version 0.1.4.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev315-1
- Update to latest snapshot.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev313-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev309-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev305-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev289-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev288-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev286-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev285-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev284-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev283-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev282-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev281-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev280-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev279-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev278-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev277-1
- Update to latest snapshot.

* Wed Feb 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev276-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev275-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev274-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev273-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev272-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev271-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev270-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev269-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev268-1
- Update to version 0.1.3.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev267-1
- Update to version 0.1.3.

* Sun Dec 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev266-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev265-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev264-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev263-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev262-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev261-1
- Update to version 0.1.3.



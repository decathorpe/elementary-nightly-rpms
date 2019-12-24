%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type network
%global plug_name bluetooth

%global appname io.elementary.switchboard.bluetooth

Name:           switchboard-plug-bluetooth
Summary:        Switchboard Bluetooth plug
Version:        2.3.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  /usr/bin/appstream-util

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       bluez
Requires:       switchboard%{?_isa}

# the bluetooth plug relies on gsettings keys from the bluetooth indicator
Requires:       wingpanel-indicator-bluetooth

Supplements:    (bluez and switchboard%{?_isa})


%description
The Bluetooth plug is a section in the Switchboard (System Settings)
that allows the user to manage bluetooth settings and connected
devices.


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
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml || :


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191224.220719.012103f4-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191220.160943.26949268-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191219.130720.b6c4d61a-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191217.185414.fe6a644e-1
- Update to latest snapshot.

* Sat Dec 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191214.090702.46e81824-1
- Update to latest snapshot.

* Thu Dec 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191205.052506.b0c72509-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191127.202526.4d2d7309-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191125.092510.5aa2f702-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191122.032522.b18a834d-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191117.202501.62b30911-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191107.102428.0255243d-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191106.081408.58e63182-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191105.162934.e06c159e-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191105.142409.c4875b85-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191105.111528.11a0b610-1
- Update to latest snapshot.

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191103.142425.c77de55d-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191101.120046.2d6862bd-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191031.173819.25561a4f-1
- Update to version 2.3.0.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191031.173819.25561a4f-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191031.153100.630c10ab-1
- Update to latest snapshot.

* Tue Oct 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191029.224309.b4722ec0-1
- Update to latest snapshot.

* Tue Oct 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191029.214855.d2aeec1c-1
- Update to latest snapshot.

* Tue Oct 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191029.184559.aa148e76-1
- Update to latest snapshot.

* Mon Oct 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191021.142351.606408c9-1
- Update to latest snapshot.

* Thu Oct 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191017.162343.f4d21df9-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191009.182328.5dce65dc-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191005.092320.e5155860-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191003.150020.7ae462e6-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190930.142321.37636ae3-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190926.150150.a43e3dcd-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190926.145359.831cc44e-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190926.013546.9c057315-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190918.172301.ff204187-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190917.092300.0e249058-1
- Update to latest snapshot.

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190912.175204.700d4d3e-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190911.122247.4ec577e1-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190907.212243.835526f4-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190906.152242.fcd59b13-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190902.202241.a412432e-1
- Update to latest snapshot.

* Sun Sep 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190901.012232.bc9214d8-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190830.212236.59d2edde-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190829.172239.758bee58-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190826.052218.a80771eb-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190823.222342.bbe90909-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190731.233357.f912aec1-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190717.131103.c9e2924c-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190626.204454.c4bb1d67-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190513.230338.ae52a1f2-1
- Update to latest snapshot.

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190409.025350.85f78a22-1
- Update to version 2.2.2.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190409.025350.85f78a22-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190408.005319.ff568ba3-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190406.170330.1b0b036c-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190406.091405.b09c0885-1
- Update to latest snapshot.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190330.225215.90ab1861-1
- Update to latest snapshot.

* Mon Feb 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190225.000049.6ac5d5e3-1
- Update to latest snapshot.

* Sun Feb 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190224.081058.35c1aba3-1
- Update to latest snapshot.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190222.000536.92886609-1
- Update to latest snapshot.

* Fri Feb 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190128.214013.0590059b-1
- Update to version 2.2.1.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190128.214013.0590059b-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190125.064914.f3a52175-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190124.134542.4673bdb3-1
- Update to version 2.2.0.

* Thu Jan 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190124.134542.4673bdb3-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190114.133622.300ed7f8-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190107.170726.5e649745-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190107.000350.c616eee3-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190106.171957.44e4edc4-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190106.162337.9550673b-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190106.123235.5da165bc-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190102.213410.49cdfc5d-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190101.200050.97d22f46-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190101.003717.04c1be0b-1
- Update to latest snapshot.

* Mon Dec 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181231.132325.678b7b79-1
- Update to latest snapshot.

* Sun Dec 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181230.142519.9151ee7d-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181228.184728.ec1b2659-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181228.091421.3f31e491-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181228.045133.6cca138a-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181228.033703.40207c4c-1
- Update to latest snapshot.

* Thu Dec 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181227.210401.ed3a6ef9-1
- Update to latest snapshot.

* Thu Dec 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181227.184558.2bb21cb2-1
- Update to latest snapshot.

* Tue Dec 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181223.190016.e0c8f6bf-2
- Adapt to renamed appdata file.

* Sun Dec 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181223.190016.e0c8f6bf-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181212.103911.00537d69-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181206.173611.08229e71-1
- Update to latest snapshot.

* Sat Dec 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181201.182412.07aef82d-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181122.154145.f49f6568-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181107.014600.911a7df6-2
- Add Requires: wingpanel-indicator-bluetooth.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181107.014600.911a7df6-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181104.151215.c5805759-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181102.084246.8c44513f-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181102.084246.8c44513f-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181030.182332.ed31877c-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181029.111014.b843d07c-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181025.140924.0a24931e-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181022.153739.a4bf4d9a-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181018.001114.07d5045c-1
- Update to version 2.1.2.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181018.001114.07d5045c-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181015.210906.236c7940-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181013.224103.456c9ea8-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181011.232135.aff80439-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181009.164023.83de7627-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181008.000545.5a016a38-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180929.000948.695a16a0-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180926.210724.a977f104-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180830.000812.d427ae17-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180829.154820.9a618924-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180829.153502.31befc42-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180819.000949.8104bfca-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180812.135700.0c50f840-2
- Occasional mass rebuild.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180812.135700.0c50f840-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180808.000154.1ff33d39-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180718.110516.4b5a93b4-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180718.000639.d68a176d-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180713.000418.ca585f7c-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180709.205353.6c8f1e87-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180704.000926.a3a077bd-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180615.001133.f1fb08b1-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180614.081325.52990312-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180613.000804.ca42df16-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180612.074959.95a6e1d4-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180608.214635.a3a79fc9-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180608.134901.5980709b-1
- Update to version 0.1.1.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180608.134901.5980709b-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180604.022926.59e6c2bc-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180601.000834.8ecde123-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180531.000333.f1e5b2fd-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180530.000442.7cb01c2a-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180529.002047.436e34fb-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180527.160656.a47b47a6-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180525.224748.50a6ca83-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180521.000941.89b18b48-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180518.000755.c134bcdd-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180516.134817.1f7f7a18-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180513.095748.3a491140-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180512.001220.866bffa4-2
- Adapt to upstream file changes.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180512.001220.866bffa4-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180510.171912.c5df587c-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180510.000934.06a72320-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180507.000330.bc49a572-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180506.164833.3e15e0ec-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180503.070150.fc42c5fa-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180429.140648.376dc2d9-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180424.202332.eb603081-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180414.231504.6001c7ef-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180414.123011.0dca80f4-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180410.000704.5a453794-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180407.180204.49301d1f-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180405.142057.34cb0897-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180404.000727.8ceb334e-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180403.143244.f7241c34-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180326.000919.c4b24786-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180324.214710.26af7488-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180321.195653.5e4b95ab-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180312.144916.97a5c57a-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180311.095406.a153f70d-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180311.000630.9c3a7674-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180309.035443.38f0cca3-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180308.192700.149b5b4e-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180308.150852.c7e16854-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180308.144040.79195263-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180308.094859.778b7e40-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180307.062339.b8d99fe3-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180306.231538.c0dd8d36-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180306.195342.edcbd660-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180306.185020.d0fd423b-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180306.172544.d4cf1348-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180303.000302.f62aec7b-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180226.203409.ab37350e-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180225.164413.853cc6b2-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180225.000953.15f2035d-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180224.113409.0d8cc756-2
- Adapt to cmake -> meson switch.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180224.113409.0d8cc756-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180221.221426.7d2e0608-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180221.145109.8827100b-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180221.074418.f7e7e019-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180205.001208.a22d0f31-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180123.170518.8c9b08dd-1
- Update to latest snapshot.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180116.193107.f647e121-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git171111.174242.a1000f53-2
- Merge .spec file from fedora.

* Thu Nov 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git171111.174242.a1000f53-1
- Switch to git snapshots.

* Sat Nov 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev82-1
- Update to latest snapshot.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev81-1
- Update to latest snapshot.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev79-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev78-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev77-1
- Update to latest snapshot.

* Mon Apr 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev57-1
- Update to latest snapshot.

* Mon Apr 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev56-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev52-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev51-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev50-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev49-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev47-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev46-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev45-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev44-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev43-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev42-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev41-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev40-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev39-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev38-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev37-1
- Update to latest snapshot.

* Thu Jan 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev36-1
- Update to version 0.1.0.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev35-1
- Update to version 0.1.0.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev34-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev33-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev31-1
- Update to latest snapshot.

* Sun Dec 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev30-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev29-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev28-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev27-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev26-2
- Make sure switchboard is new enough.
- Fix plug directory.

* Tue Dec 20 2016 Cody Garver <cody@elementary.io> - 0.1.0+rev26-1
- Initial package.



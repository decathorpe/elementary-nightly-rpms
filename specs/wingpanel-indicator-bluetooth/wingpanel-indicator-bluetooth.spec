%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

Name:           wingpanel-indicator-bluetooth
Summary:        Bluetooth Indicator for wingpanel
Version:        2.1.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       bluez

Supplements:    (bluez and wingpanel%{?_isa})


%description
A bluetooth indicator for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang bluetooth-indicator


%files -f bluetooth-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libbluetooth.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.bluetooth.gschema.xml


%changelog
* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191109.062837.0caf5bbf-1
- Update to latest snapshot.

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191108.062603.e6973fb9-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191107.221914.db0eebff-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191106.005223.564c8a5a-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191105.132417.42e72787-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191005.102331.62b5ee5c-1
- Update to latest snapshot.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191004.022328.c038e0d2-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191003.153027.3dc5fa6e-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190926.215538.35d888dd-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190924.202046.f6b562fd-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190919.183008.50a83c27-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190911.132259.e0a0cd20-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190909.132257.1bfec425-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190907.102245.0bcf5f36-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190902.132238.0cee6e1f-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190830.212258.141c97cc-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190829.172302.8904686b-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190827.172551.57711fbd-1
- Update to latest snapshot.

* Sun Aug 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190811.002202.3d9a6ab6-1
- Update to latest snapshot.

* Sun Aug 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190810.233605.622d6782-1
- Update to latest snapshot.

* Sat Jul 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190727.181816.485b6a14-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190626.204657.54f4fbf2-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190531.044945.c023c525-1
- Update to latest snapshot.

* Wed May 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190522.175503.4cc8515a-1
- Update to version 2.1.3.

* Wed May 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190522.175503.4cc8515a-1
- Update to latest snapshot.

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190418.225404.7043ed3e-1
- Update to latest snapshot.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190409.215329.735db2a4-1
- Update to latest snapshot.

* Sat Feb 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190222.000629.57a16922-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190210.221940.a93565c3-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190210.211811.1ad1942b-1
- Update to latest snapshot.

* Thu Jan 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190131.182208.a0be5e56-1
- Update to latest snapshot.

* Thu Jan 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190124.211624.4c9969b7-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190114.001131.062b2633-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190111.000725.a9db75d1-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190110.225039.d10f8772-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181221.095940.c089f51e-1
- Update to version 2.1.2.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181221.095940.c089f51e-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181206.185532.9a0d3b92-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181206.060033.0fbc6641-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181202.054928.b861c8ef-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181104.221528.384d2ac5-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181101.210208.a21ea7a2-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181101.210208.a21ea7a2-1
- Update to latest snapshot.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181101.000342.7cafe134-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181030.073957.451a535b-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181013.213815.9c63e1f4-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181003.101832.71ac479b-1
- Update to version 2.1.1.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git181003.101832.71ac479b-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180920.000546.2f0a985f-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180830.000855.f3abc0b2-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180819.001024.4ae3f1ea-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180627.164117.0f5e52b6-2
- Occasional mass rebuild.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180627.164117.0f5e52b6-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180611.184140.332cf732-1
- Update to version 2.1.0.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180611.184140.332cf732-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180609.122607.79a96371-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180606.152824.c6d5322d-2
- Adapt to upstream file changes.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180606.152824.c6d5322d-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180606.141250.afbb5799-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180531.080340.e333276d-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180529.001552.fd92da2c-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180513.001332.98c201b8-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180510.172313.e29bff95-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180507.160415.9ae24fdf-1
- Update to latest snapshot.

* Wed May 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180502.153729.63857308-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180409.231640.6aabb441-1
- Update to latest snapshot.

* Mon Apr 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180409.174655.52eb71be-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180408.095806.8985e839-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180405.210138.d2f40078-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180404.005820.ac21f7c4-1
- Adapt to CMake -> meson switch.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180403.165341.2f380096-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180325.001123.4d476f5e-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180308.142216.e283df3d-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180306.173924.2185d263-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180213.234841.1d4a841d-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180213.024026.0a121f0e-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180103.001654.63c872fe-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180103.001654.63c872fe-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180103.000111.31365cbb-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git171219.060709.bacbd1c8-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170818.222502.ca2c16ea-1
- Update to version 2.0.3.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170818.222502.ca2c16ea-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170709.011937.5d7701e1-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170702.101808.562f7a27-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170620.155347.f064927a-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170617.175639.e5aa1019-1
- Update to latest snapshot.

* Sun Jun 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170604.161730.94afb215-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170522.231337.8244c4c2-1
- Update to version 2.0.2.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev89-1
- Update to latest snapshot.

* Fri May 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev88-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev87-1
- Update to latest snapshot.

* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev86-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev85-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev82-1
- Update to latest snapshot.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev81-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev80-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev79-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev78-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev77-1
- Update to latest snapshot.

* Fri Feb 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev76-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev75-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev74-1
- Update to latest snapshot.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev73-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev72-1
- Update to version 2.0.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev71-1
- Update to version 2.0.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev70-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev69-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev68-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev67-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev66-1
- Update to version 2.0.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev66-2
- Spec file cleanups.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev66-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev65-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev63-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev62-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev61-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev61-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev60-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev59-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev58-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev57-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev56-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev55-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev54-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev53-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev52-2
- Update for packaging changes.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev48-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev47-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev46-1
- Update to latest snapshot.

* Wed Jun 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev45-1
- Update to latest snapshot.

* Tue Jun 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev43-1
- Update to latest snapshot.

* Thu Jun 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev42-1
- Update to latest snapshot.

* Wed Jun 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev41-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-2
- Update for packaging changes.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev39-1
- Update to latest snapshot.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev37-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-1
- Initial package.



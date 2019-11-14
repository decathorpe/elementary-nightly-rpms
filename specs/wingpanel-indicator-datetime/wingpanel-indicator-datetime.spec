%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global indi_name datetime
%global indi_rdnn io.elementary.wingpanel.datetime

Name:           wingpanel-indicator-datetime
Summary:        Datetime Indicator for wingpanel
Version:        2.2.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libecal-1.2)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A datetime indicator for wingpanel.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{indi_name}-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{indi_rdnn}.appdata.xml


%files -f %{indi_name}-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/lib%{indi_name}.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.datetime.gschema.xml
%{_datadir}/metainfo/%{indi_rdnn}.appdata.xml


%changelog
* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191114.152416.39c6ceca-1
- Update to latest snapshot.

* Tue Nov 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191112.152413.0164f172-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191107.202410.d239a7fc-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191106.005630.96a71e53-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191105.112323.523295f8-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191105.063010.42a79a13-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191031.203707.e6b55310-1
- Update to version 2.2.0.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191031.203707.e6b55310-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191031.170910.99f121a9-1
- Update to latest snapshot.

* Tue Oct 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191029.174338.54649ac8-1
- Update to latest snapshot.

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191016.175815.fee6bede-1
- Update to latest snapshot.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191004.032326.32d9a5cc-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191003.152114.65bf0326-1
- Update to latest snapshot.

* Fri Sep 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190926.234819.98cfa039-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190926.225306.bc28737f-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190924.171946.d69f4d4c-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190924.000108.f6214e7a-1
- Update to latest snapshot.

* Sun Sep 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190922.074127.9cd65353-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190920.210509.0ed4504c-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190920.163527.329c3657-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190917.091335.421a5b75-1
- Update to latest snapshot.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190913.105349.54f741a9-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190911.162536.a8457d59-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190909.184857.0830d2eb-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190909.132258.3c261543-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190907.102245.8852468c-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190902.202301.416fb97b-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190830.212259.6743fc1c-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190829.172300.3b91fe0a-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190827.174845.1df19b4f-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190826.134605.ab11c7eb-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190822.012222.27ca5814-1
- Update to latest snapshot.

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190820.112219.93e0b2ce-1
- Update to latest snapshot.

* Mon Aug 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190819.022215.ea3980c1-1
- Update to latest snapshot.

* Sat Aug 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190817.142218.471b46fe-1
- Update to latest snapshot.

* Fri Aug 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190816.171812.9cd3ecce-1
- Update to latest snapshot.

* Fri Aug 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190816.152614.b624f9ec-1
- Update to latest snapshot.

* Fri Aug 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190816.140221.4ded399a-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190815.182211.3857ce7f-1
- Update to latest snapshot.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190814.112336.fbc66518-1
- Update to latest snapshot.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190814.095457.65992ef1-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190801.131558.fb6281eb-1
- Update to latest snapshot.

* Wed Jul 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190731.081239.c1731862-1
- Update to latest snapshot.

* Tue Jul 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190730.154725.b423e9d7-1
- Update to latest snapshot.

* Fri Jul 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190726.172613.4d03512d-1
- Update to latest snapshot.

* Wed Jul 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190724.154258.a027c470-1
- Update to latest snapshot.

* Wed Jul 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190724.120241.b5dea142-1
- Update to latest snapshot.

* Fri Jul 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190718.234907.ffdefaf8-1
- Update to latest snapshot.

* Thu Jul 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190718.224505.d3063641-1
- Update to latest snapshot.

* Thu Jul 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190718.212053.cf97d415-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190717.203506.46b239b0-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190717.160458.1614120a-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190717.155241.eb5d286c-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190717.101337.de1a967a-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190717.075417.3f3e20c8-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190716.215313.ae00dba3-1
- Update to latest snapshot.

* Mon Jul 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190715.203453.3d141833-1
- Update to latest snapshot.

* Fri Jul 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190712.203013.8f2d42ae-1
- Update to latest snapshot.

* Fri Jul 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190712.193226.a419d637-1
- Update to latest snapshot.

* Fri Jul 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190712.184745.0a88e96e-1
- Update to latest snapshot.

* Fri Jul 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190712.011432.1f6b6560-1
- Update to latest snapshot.

* Fri Jul 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190711.233605.19637702-1
- Update to latest snapshot.

* Thu Jul 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190711.224848.6a21832e-1
- Update to latest snapshot.

* Mon Jul 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190708.213243.aa2453e2-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190626.204701.5e9ffbc6-1
- Update to latest snapshot.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190604.010323.04dcf808-2
- Remove unnecessary downstream patch.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190604.010323.04dcf808-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190405.220333.dad925ac-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190312.121549.4859e72a-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190103.180916.c647c4ee-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181221.070002.4c5a6b51-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181218.000203.bc6d4c1a-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181215.125534.7f8d29bf-2
- Adapt to downstream-patched granite.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181215.125534.7f8d29bf-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181212.010437.e4cb8984-1
- Update to version 2.1.3.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181212.010437.e4cb8984-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181130.060611.e18c4621-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181126.053801.d59cbf9d-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181121.143237.8d0266b9-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181117.174134.402c3838-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181117.090924.8b8f8994-1
- Update to latest snapshot.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181114.090641.3954d141-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181113.190307.11d9a4ae-1
- Update to latest snapshot.

* Sun Nov 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181110.233655.72fc378b-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181104.221305.7ace3ffe-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181104.182408.4aa9aaa2-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181101.000352.1e770e65-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181101.000352.1e770e65-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181029.020114.8b452055-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181025.071446.08255494-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181024.115128.e54a7bd6-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181019.180658.1d14555c-1
- Update to version 2.1.2.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181019.180658.1d14555c-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181016.023535.f663bebd-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181015.142159.66af3c85-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181014.210800.5e306070-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181014.182800.ee247ade-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181002.114006.67809d96-1
- Update to version 2.1.1.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git181002.114006.67809d96-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180930.162400.72c05731-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180928.000739.9c93c14c-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180927.045129.59bda454-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180925.000323.fed6f93b-1
- Update to latest snapshot.

* Sat Sep 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180922.001138.ed9f43d7-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180918.094209.3afc930a-2
- BuildRequire granite >= 5.0.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180918.094209.3afc930a-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180907.000708.c2a3bdf8-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180906.042221.cddcbede-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180831.185234.1d38c806-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180831.132527.76a97554-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180830.152015.1fcf85a3-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180829.160013.cc673896-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180819.001028.164dfaf4-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180818.133651.51eaf618-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180818.054631.7efd3877-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180809.161732.27afe7a5-2
- Occasional mass rebuild.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180809.161732.27afe7a5-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180809.093824.8469ed60-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180808.121323.97b9dd8d-1
- Update to latest snapshot.

* Sat Aug 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180804.135539.760e38fe-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180803.152446.b81cf69e-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180802.235010.a3684f78-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180802.175352.a5553ae0-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180731.213945.6616e9db-1
- Update to latest snapshot.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180727.115713.abc28bae-1
- Update to latest snapshot.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180727.063918.a0b3c828-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180726.210115.7dedcb12-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180726.170053.bda570e6-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180722.000430.0dca9bf4-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180721.183258.d5cd4f76-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180718.165117.1116a0de-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180717.154348.d24bd2fd-1
- Update to latest snapshot.

* Mon Jul 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180716.084627.a6f0b1dd-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180713.182213.1a674d07-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180713.172718.fa3fdbe8-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180713.014219.f62cebf8-2
- Add missing BR: gcc, gcc-c++.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180713.014219.f62cebf8-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180712.195459.f002a4c3-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180627.164729.42bcef14-1
- Update to version 2.1.0.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180627.164729.42bcef14-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180615.001310.42c67d62-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180611.172037.8730eabb-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180608.232826.a9c6a6df-2
- Adapt to upstream file changes.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180608.232826.a9c6a6df-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180608.174527.094258ca-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180606.001126.9538c45e-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180603.162154.e710741e-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180528.165635.39d3e90f-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180513.001336.60eba240-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180510.172341.bcc2d10a-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180509.102349.e6877412-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180509.090559.a859d4a8-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180507.184156.47cc93d5-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180506.001213.dc4197ac-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180417.180901.3ac469ed-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180324.225815.60fedbc5-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180320.001411.b83b687c-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180221.230213.1f4ed13c-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180209.001219.bfeaae75-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180120.183447.873e4a40-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180120.183445.e08b32c7-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git171102.121944.20def735-2
- Merge .spec file from fedora.

* Thu Nov 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git171102.121944.20def735-1
- Update to latest snapshot.

* Mon Oct 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git171016.160817.834f0ff2-2
- Try to fix build.

* Mon Oct 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git171016.160817.834f0ff2-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170925.085246.d61f05fc-1
- Update to latest snapshot.

* Thu Sep 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170907.183932.5970edea-1
- Update to latest snapshot.

* Wed Aug 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170802.173815.ab6db27d-1
- Update to latest snapshot.

* Thu Jul 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170726.222923.c8deb657-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170725.181747.8b0036f4-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170706.075304.7992707f-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170703.191910.7c8f5c24-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170630.101222.56b8e20e-1
- Update to version 2.0.2.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev197-1
- Update to latest snapshot.

* Sat Jun 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev196-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev195-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev194-1
- Update to latest snapshot.

* Sat Jun 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev193-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev192-1
- Update to latest snapshot.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev191-1
- Update to latest snapshot.

* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev190-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev189-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev188-1
- Update to latest snapshot.

* Fri Apr 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev187-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev186-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev185-1
- Update to latest snapshot.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev184-1
- Update to latest snapshot.

* Mon Mar 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev181-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev180-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev179-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev178-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev177-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev176-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev175-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev174-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev173-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev172-1
- Update to version 2.0.1.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev171-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev170-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev169-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev168-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev167-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev166-1
- Update to version 2.0.1.

* Thu Oct 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev164-1
- Update to latest snapshot.

* Wed Oct 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev163-1
- Update to latest snapshot.

* Tue Oct 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev162-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev161-2
- Spec file cleanups.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev161-1
- Update to latest snapshot.

* Tue Sep 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev160-1
- Update to version 2.0.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev159-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev158-1
- Update to latest snapshot.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev157-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev156-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev153-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev152-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev152-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev150-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev149-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev147-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev146-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev145-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev144-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev142-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev141-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev140-1
- Update to latest snapshot.

* Wed Jul 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev139-1
- Update to latest snapshot.

* Sun Jul 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev138-1
- Update to latest snapshot.

* Sat Jul 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev137-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev136-2
- Update for packaging changes.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev132-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev131-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev130-1
- Update to latest snapshot.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev129-1
- Update to latest snapshot.

* Sun Jun 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev128-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev127-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev127-2
- Update for packaging changes.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev127-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev126-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev125-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev125-1
- Initial package.



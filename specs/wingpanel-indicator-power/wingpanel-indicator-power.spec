%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.power

Name:           wingpanel-indicator-power
Summary:        Power indicator for wingpanel
Version:        2.1.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A power indicator for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang power-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f power-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libpower.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.power.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200301.140905.5bfc20b2-1
- Update to latest snapshot.

* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200222.190853.d41adc51-1
- Update to latest snapshot.

* Fri Jan 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200103.220732.ecc7d34d-1
- Update to latest snapshot.

* Wed Dec 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191225.151716.2d9e6301-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191219.130709.68c17947-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191217.225130.7a0c1987-1
- Update to latest snapshot.

* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191213.173938.6dca9210-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191204.212456.a75727bc-1
- Update to latest snapshot.

* Thu Nov 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191128.192442.aeb672ee-1
- Update to latest snapshot.

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191119.165230.4da24040-1
- Update to latest snapshot.

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191107.213626.bf39291b-2
- Package and verify appdata file.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191107.213626.bf39291b-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191107.205729.77d75773-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191106.164408.12f8a3f1-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191003.152014.38a38fbb-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191001.201822.1fbe4157-1
- Update to latest snapshot.

* Sun Sep 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190929.014539.7e02f4f8-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190919.182026.772e188a-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190830.212305.2a919ebf-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190827.175603.cb1bb288-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190626.204723.a3dbc6b5-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190531.044923.eda20fd8-1
- Update to latest snapshot.

* Mon May 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190520.000327.d83767c4-1
- Update to latest snapshot.

* Thu Apr 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190425.112631.235c5485-1
- Update to latest snapshot.

* Thu Apr 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190411.131105.25ebfd15-1
- Update to latest snapshot.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190409.093459.c01b8e14-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190312.152731.1e2e1931-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190305.022722.a5fba54c-1
- Update to latest snapshot.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190129.112347.a2a344ea-1
- Update to version 2.1.4.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190129.112347.a2a344ea-1
- Update to latest snapshot.

* Wed Jan 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190116.000420.0bab16b2-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190114.001143.d7b847f7-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190103.181220.45e9678f-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181221.072050.6293335b-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181218.000212.55c795ac-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181215.160711.e8ac1c19-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181215.133158.12638783-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181212.220316.e262f58d-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181211.110640.f15d1328-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181204.164637.e14446c9-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181204.071832.f7ed2965-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181202.192920.deb09dd1-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181202.161510.75effd5b-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181130.175920.d101f702-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181130.170116.d0be7025-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181130.111913.a2a8db2c-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181104.223801.3d3c9a2c-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181101.000345.018a525a-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181101.000345.018a525a-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181029.090717.627ab1ae-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181025.081931.b6be3480-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181025.040155.7f90ce07-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181024.134910.fd3aa482-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181023.071306.414e263a-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181021.120351.34dd3621-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181019.061937.3532ed00-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181018.001151.1219a153-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181013.215420.3b889ea2-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181009.000205.2c871563-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181002.113021.824cc733-1
- Update to version 2.1.3.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181002.113021.824cc733-1
- Update to latest snapshot.

* Sun Sep 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180923.000651.c5c4bee3-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180917.160247.e6d4090a-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180906.042320.4b81a0c0-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180830.152131.c2e29bbd-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180830.000908.58cbc47c-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180819.043201.be6d0d8e-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180812.141436.bde10c77-2
- Occasional mass rebuild.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180812.141436.bde10c77-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180808.101750.a9065796-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180808.000216.5c9069c6-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180731.230105.96bab3af-1
- Update to latest snapshot.

* Sun Jul 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180729.000221.7d5f3f83-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180720.115043.89005f7a-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180720.000746.65f1b06c-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180719.000806.de3c1b83-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180717.165953.b2cca2eb-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180709.001059.7ffdd39e-1
- Update to latest snapshot.

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180708.060315.503789e6-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180705.193104.dd16d6cd-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git180702.000744.0b6d776b-1
- Update to version 2.1.2.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180702.000744.0b6d776b-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180610.001408.6f429c26-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180607.100528.18a5abf4-2
- Adapt to upstream file changes.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180607.100528.18a5abf4-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180606.082446.ea353b56-2
- Adapt to CMake -> meson switch.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180606.082446.ea353b56-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180605.102247.808b1a78-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180530.000634.52269a9d-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180529.114205.6f77ebd2-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180507.000514.22dce21d-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180506.001226.fe55ea98-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180503.080148.9749f9cc-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180429.151244.d5d98f7c-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180415.161252.f9441536-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180405.001939.f49fc8dc-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180325.001134.c4427017-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180320.001422.5b4ba759-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180213.193649.f741c58c-1
- Update to latest snapshot.

* Sun Feb 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180204.211214.53f094bc-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180115.001619.0419504b-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180113.171806.5c4d7256-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170801.180504.e4a9c434-2
- Merge .spec file from fedora.

* Wed Aug 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170801.180504.e4a9c434-1
- Update to latest snapshot.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170801.175623.d51bdcf0-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170725.181609.38ed7b25-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170724.185518.18dfd9d1-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170723.180728.f0cec55a-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170711.232124.13d18c19-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170702.185429.b778d690-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170617.151508.e57f0542-1
- Update to latest snapshot.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170515.123700.d2e424c0-1
- Update to version 2.1.1.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git170515.123700.d2e424c0-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git170501.204149.38ee9e55-1
- Update to latest snapshot.

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git170428.232602.80f60327-1
- Update to version 2.1.0.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev216-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev215-2
- Add new BR: pkgconfig(libudev).

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev215-1
- Update to latest snapshot.

* Sun Apr 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev212-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev207-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev206-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev205-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev204-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev203-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev202-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev201-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev200-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev199-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev198-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev197-1
- Update to latest snapshot.

* Thu Jan 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev196-1
- Update to latest snapshot.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev195-1
- Update to latest snapshot.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev194-1
- Update to version 2.0.1.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev193-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev192-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev191-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev190-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev189-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev188-1
- Update to latest snapshot.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev187-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev186-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev185-1
- Update to latest snapshot.

* Fri Nov 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev184-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev183-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev182-1
- Update to version 2.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev180-2
- Spec file cleanups.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev180-1
- Update to version 2.0.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev179-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev178-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev177-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev176-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev175-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev175-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev174-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev173-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev172-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev170-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev169-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev168-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev167-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev165-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev164-1
- Update to latest snapshot.

* Mon Jul 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev163-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev156-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev155-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev154-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev153-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev152-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev152-2
- Update for packaging changes.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev152-1
- Update to latest snapshot.

* Mon May 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev151-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev149-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev148-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev148-1
- Initial package.



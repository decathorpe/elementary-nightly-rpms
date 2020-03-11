%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.session

Name:           wingpanel-indicator-session
Summary:        Session Indicator for wingpanel
Version:        2.2.7+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A session Indicator for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang session-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f session-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libsession.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed Mar 11 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200311.093524.fed901c1-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200301.140906.4da05d38-1
- Update to latest snapshot.

* Sat Feb 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200228.230904.702c919d-1
- Update to latest snapshot.

* Thu Feb 27 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200227.215045.398e9ebe-1
- Update to latest snapshot.

* Tue Feb 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200225.171437.4b0e9ec7-1
- Update to latest snapshot.

* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200222.190854.61aaf35a-1
- Update to latest snapshot.

* Tue Feb 18 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200218.160823.6ed27a09-1
- Update to latest snapshot.

* Sat Feb 15 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200215.091907.9f843f5a-1
- Update to latest snapshot.

* Fri Feb 14 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200214.180558.7894afce-1
- Update to latest snapshot.

* Fri Feb 14 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200214.084110.ce73c628-1
- Update to latest snapshot.

* Sat Feb 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200201.020815.b54c92fd-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200121.160800.d9152047-1
- Update to latest snapshot.

* Sat Jan 18 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.7+git200117.223639.9c8b1418-1
- Update to version 2.2.7.

* Fri Jan 17 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git200117.223639.9c8b1418-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git200115.172258.237043fe-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git200106.190736.85b5ee6f-1
- Update to latest snapshot.

* Fri Jan 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git200103.210732.20ed4fc7-1
- Update to latest snapshot.

* Fri Dec 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191227.111936.bb8c2778-1
- Update to latest snapshot.

* Wed Dec 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191225.151715.279ab591-1
- Update to latest snapshot.

* Sat Dec 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191221.000712.09532be3-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191218.083156.646131eb-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191217.225106.7dd944d5-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191217.210214.bb8206f1-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191217.210026.490a4a6a-1
- Update to latest snapshot.

* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191213.172225.0d9bb541-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191125.164548.3cb90c16-1
- Update to version 2.2.6.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191125.164548.3cb90c16-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191122.032430.d892ed2f-1
- Update to latest snapshot.

* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191114.152422.9f6ea395-1
- Update to latest snapshot.

* Tue Nov 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191112.182416.9e8a4588-1
- Update to latest snapshot.

* Sun Nov 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191110.202414.38b1e942-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191109.152412.a0a2d7b6-1
- Update to latest snapshot.

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191107.213844.7e408222-2
- Package and verify appdata file.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191107.213844.7e408222-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191107.205750.09ddad39-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191106.161930.13383fa0-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191003.154121.7a0a101d-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190925.170816.6722e4ad-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190925.165907.2fcdb31d-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190924.210225.bb1a5682-1
- Update to latest snapshot.

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190912.180825.e3684bc3-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190902.132243.a9613aff-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190830.212306.0112f7d5-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190827.172452.edfeaf78-1
- Update to latest snapshot.

* Mon Jul 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190719.134700.943cbab0-1
- Update to version 2.2.5.

* Fri Jul 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190719.134700.943cbab0-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190716.154243.2a8657bc-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190715.235253.d6b1ce1f-1
- Update to latest snapshot.

* Wed Jul 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190709.213236.0040c866-1
- Update to version 2.2.4.

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190709.213236.0040c866-1
- Update to latest snapshot.

* Tue Jul 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190702.211106.edb17a4d-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190626.204731.ba2d2abf-1
- Update to latest snapshot.

* Mon Jun 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190603.074113.b08a8c8d-1
- Update to latest snapshot.

* Wed Apr 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190417.205414.273d6501-1
- Update to latest snapshot.

* Wed Apr 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190410.115330.20df46e5-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190406.165228.7140a6f1-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190305.000727.8610dfc8-1
- Update to version 2.2.3.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190305.000727.8610dfc8-1
- Update to latest snapshot.

* Tue Feb 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190219.150512.01b792c3-1
- Update to latest snapshot.

* Tue Feb 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190218.210207.da5fac92-2
- Bump granite requirement to >= 5.2.0.

* Mon Feb 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190218.210207.da5fac92-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190114.001149.86611041-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190111.000739.3c341443-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190103.181327.cd27e381-1
- Update to latest snapshot.

* Sat Dec 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181222.000948.5913abfb-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181221.124630.b7b5e1ea-1
- Update to version 2.2.2.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181221.124630.b7b5e1ea-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181221.063240.de3477f6-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181217.113217.6220282e-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181217.010356.a9522692-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181211.151040.9824eabc-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181121.181039.8945eba2-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181117.174456.eef8a2bc-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181104.224233.adbd1947-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181027.181151.ad8e4f40-2
- Occasional mass rebuild.

* Sat Oct 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181027.181151.ad8e4f40-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181025.165145.9ca67cd3-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181025.040151.9162485d-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181024.134932.213a1977-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181019.180126.9557ce2e-1
- Update to version 2.2.1.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181019.180126.9557ce2e-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181018.001155.d5add0bd-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181016.081301.9d1b0edb-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181013.215641.9fca4c78-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181009.000209.c22f3a1f-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181002.111219.4b0ab3ab-1
- Update to version 2.2.0.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git181002.111219.4b0ab3ab-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180921.000801.28cdf1a0-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180906.132009.2d44144b-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180830.000916.33bcdcbb-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180829.053957.d3524159-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180819.001041.1dae7d1a-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180812.141503.d2be25bc-2
- Occasional mass rebuild.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180812.141503.d2be25bc-1
- Update to latest snapshot.

* Fri Aug 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180809.211537.69748b43-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180720.000750.c180730d-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180717.000350.f9c82591-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180704.232108.bd7fef1c-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180701.213950.d04747ae-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180615.001318.22efacb0-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180613.154050.a215c3eb-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180610.001413.1972cac8-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180607.095713.4a5812bb-1
- Update to version 2.1.0.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180607.095713.4a5812bb-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180604.000346.2096ba94-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180531.081743.181532be-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180530.034646.699d234d-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180529.115159.ba81c936-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180525.164732.870eed77-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180512.001416.24843f05-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180511.030335.302390a6-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180510.172430.1be6b5b8-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180504.090424.e288a5f6-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180429.145950.8f45e04c-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180425.163935.7d7ec4d8-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180424.201602.1f5a004b-1
- Update to latest snapshot.

* Mon Apr 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180423.170053.c2e940e3-1
- Update to latest snapshot.

* Wed Apr 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180417.214539.967de52f-1
- Update to latest snapshot.

* Wed Apr 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180411.171818.b381ce38-1
- Update to latest snapshot.

* Wed Apr 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180411.001950.fb275c57-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180405.170632.70057b44-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180403.143317.dcdb3e18-2
- Adapt to CMake -> meson switch.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180403.143317.dcdb3e18-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180327.213632.1d84f5fc-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180326.072008.84e99d98-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180325.185409.77053c3b-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180320.001426.634e9774-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180318.034051.556dfc17-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180308.143131.632e617d-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180214.185959.1dcbbb2f-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180211.001121.c4abed55-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180209.001228.95a0bfb3-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180129.000538.7da71c02-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180127.000945.a0995a72-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180120.033545.b71f41a0-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180102.160012.5a490533-2
- Merge .spec file from fedora.

* Tue Jan 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180102.160012.5a490533-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171219.060826.dabdf868-1
- Update to latest snapshot.

* Mon Dec 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171217.230910.a3f1274b-1
- Update to latest snapshot.

* Sat Dec 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171128.182354.95e34584-1
- Update to version 2.0.4.

* Tue Nov 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git171128.182354.95e34584-1
- Update to latest snapshot.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170907.224657.33a0c45a-1
- Update to latest snapshot.

* Mon Aug 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170814.011201.c45639df-1
- Update to version 2.0.3.

* Mon Aug 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170814.011201.c45639df-1
- Update to latest snapshot.

* Thu Jul 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170706.182218.a25e4766-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170702.103057.1d46c17e-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170628.105957.7916b12a-1
- Update to version 2.0.2.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev190-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev189-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev163-1
- Update to latest snapshot.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev162-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev161-1
- Update to latest snapshot.

* Fri Apr 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev160-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev149-1
- Update to latest snapshot.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev148-1
- Update to latest snapshot.

* Thu Apr 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev133-1
- Update to latest snapshot.

* Wed Apr 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev131-1
- Update to latest snapshot.

* Mon Apr 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev130-1
- Update to latest snapshot.

* Mon Mar 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev129-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev130-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev128-1
- Update to latest snapshot.

* Sun Mar 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev123-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev122-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev121-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev120-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev119-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev118-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev117-1
- Update to latest snapshot.

* Wed Feb 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev116-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev115-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev114-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev113-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev112-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev111-1
- Update to latest snapshot.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev110-1
- Update to version 2.0.1.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev109-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev108-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev107-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev106-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev105-1
- Update to version 2.0.1.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev105-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev104-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev103-1
- Update to latest snapshot.

* Sun Oct 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev102-1
- Update to version 2.0.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev101-1
- Update to latest snapshot.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev100-1
- Update to latest snapshot.

* Thu Sep 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev99-1
- Update to latest snapshot.

* Wed Aug 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev98-1
- Update to latest snapshot.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev97-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev96-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev94-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev90-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev89-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev88-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev87-1
- Update to latest snapshot.

* Tue Jul 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev84-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev83-2
- Update for packaging changes.

* Tue Jul 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev83-1
- Update to latest snapshot.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev82-1
- Update to latest snapshot.

* Mon Jun 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev81-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev80-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev79-1
- Update to latest snapshot.

* Wed Jun 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev78-1
- Update to latest snapshot.

* Tue Jun 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev77-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev76-2
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev76-1
- Update to latest snapshot.

* Mon May 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev75-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev74-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev73-1
- Update to latest snapshot.

* Mon May 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev72-2
- Update for packaging changes.

* Mon May 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev72-1
- Initial package.



%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

Name:           wingpanel-indicator-session
Summary:        Session Indicator for wingpanel
Version:        2.1.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
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


%files -f session-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libsession.so


%changelog
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



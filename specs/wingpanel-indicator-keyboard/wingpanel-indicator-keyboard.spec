%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.keyboard

Name:           wingpanel-indicator-keyboard
Summary:        Keyboard Indicator for wingpanel
Version:        2.2.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A keyboard indicator for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang keyboard-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f keyboard-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libkeyboard.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Jan 05 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git200105.170735.6d56fe6a-1
- Update to latest snapshot.

* Fri Jan 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git200103.210732.d1c5a378-1
- Update to latest snapshot.

* Wed Dec 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191225.151720.92e4bbda-1
- Update to latest snapshot.

* Sat Dec 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191221.010711.234a9261-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191219.130710.24c58123-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191217.225302.493fabce-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191204.212450.8c5b98b8-1
- Update to latest snapshot.

* Sat Nov 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191123.022430.800d493d-1
- Update to latest snapshot.

* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191114.152416.f24b9821-1
- Update to latest snapshot.

* Tue Nov 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191112.162413.cfaa52e5-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191107.202407.ed94bf1a-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191106.132404.f4c4eee0-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191106.005705.7f22776a-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191105.112322.4c35dde5-1
- Update to version 2.2.0.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191105.112322.4c35dde5-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191105.063750.6df1c0e7-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191104.170343.04f84477-2
- Package and verify appdata file.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191104.170343.04f84477-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191104.165404.be906864-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191104.150348.180a5e2e-1
- Update to latest snapshot.

* Mon Oct 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191014.151545.f40dc85e-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191003.163248.feb3eef5-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191003.152000.62b0d9bb-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191001.213721.f457be7e-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git191001.202802.9aa41978-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190909.132259.fcbb9b53-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190902.132239.7f9d148f-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190827.174912.97e37029-1
- Update to latest snapshot.

* Tue Aug 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190813.161240.51057e91-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190626.204705.a0d82305-1
- Update to latest snapshot.

* Wed Mar 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190306.075917.5a1bfcba-1
- Update to version 2.1.2.

* Wed Mar 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git190306.075917.5a1bfcba-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git190125.000231.0b7f950e-1
- Update to latest snapshot.

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git190123.102536.8d5ba630-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git190103.180819.d4b30126-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181215.134521.181f1aca-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181211.110336.f0e73f62-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181206.060030.0e285675-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181202.055034.cfd50744-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181104.221635.de38fef6-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181026.010613.7abe8de9-2
- Occasional mass rebuild.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181026.010613.7abe8de9-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181024.132152.1ef86341-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181023.190415.3f1c60c7-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181019.180602.8b28e7b6-1
- Update to version 2.1.1.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git181019.180602.8b28e7b6-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git181016.083138.24e05a4b-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git181013.211717.e7fbd1cd-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180921.000751.8195bba4-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180829.054233.8e01a3ee-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180720.195637.dacf4aea-2
- Occasional mass rebuild.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180720.195637.dacf4aea-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180627.164828.d42e530a-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180613.154356.5667d21f-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180610.001357.81a48468-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180608.143539.42350108-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180607.093931.7c733921-1
- Update to version 2.1.0.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180607.093931.7c733921-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180531.081004.2e45389a-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180528.170143.df3d7c12-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180525.202218.b2f96177-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180429.150007.d19c9e09-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180420.001410.eec71a81-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180416.204622.4659c771-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180414.230333.21a87456-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180329.233608.b294f018-2
- Adapt to CMake -> meson switch.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180329.233608.b294f018-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180325.001127.094c7faf-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180320.001414.7bd892f9-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180310.000620.8d831baf-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180309.000755.514f0266-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180222.161116.69f3c609-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180218.201541.c53100df-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180213.200056.f6c7d51d-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180211.001110.638fdf84-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180209.001221.684cc672-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180206.202531.640306b1-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180205.001353.67e463cd-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180118.180122.d53c0da0-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180105.085319.1f52cbd4-2
- Merge .spec file from fedora.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180105.085319.1f52cbd4-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180104.220732.a2805961-1
- Update to latest snapshot.

* Thu Dec 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git171228.215358.730bbbd3-1
- Update to latest snapshot.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git171011.173150.0369cc30-1
- Update to latest snapshot.

* Wed Aug 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170829.215012.2844c257-1
- Update to latest snapshot.

* Fri Jul 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170709.024955.de992315-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170702.180442.134f279f-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170617.151454.cd4ba404-1
- Update to latest snapshot.

* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170514.131906.ef6139f9-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170508.121656.f441632c-1
- Update to latest snapshot.

* Thu May 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170503.171235.7e9d9ee8-1
- Update to version 2.0.2.

* Thu May 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev87-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev86-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev85-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev73-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev72-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev70-1
- Update to latest snapshot.

* Sat Mar 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev69-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev68-1
- Update to latest snapshot.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev67-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev66-2
- Add BR: pkgconfig(libxml-2.0).

* Sun Feb 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev66-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev65-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev64-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev63-1
- Update to version 2.0.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev62-1
- Update to version 2.0.1.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev61-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev60-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev59-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev58-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev57-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev56-1
- Update to version 2.0.1.



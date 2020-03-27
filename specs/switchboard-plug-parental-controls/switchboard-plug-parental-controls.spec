%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_name parental-controls
%global plug_type system

%global plug_rdnn io.elementary.switchboard.parental-controls

Name:           switchboard-plug-%{plug_name}
Summary:        Switchboard Parental Controls plug
Version:        2.1.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  systemd
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

%{?systemd_requires}

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
An easy parental controls plug.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/pantheon-parental-controls-client.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%post
%systemd_post pantheon-parental-controls.service

%preun
%systemd_preun pantheon-parental-controls.service

%postun
%systemd_postun_with_restart pantheon-parental-controls.service


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%dir %{_sysconfdir}/pantheon-%{plug_name}
%config(noreplace) %{_sysconfdir}/pantheon-%{plug_name}/daemon.conf

%{_bindir}/pantheon-%{plug_name}-daemon

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_libexecdir}/pantheon-%{plug_name}-client

%{_datadir}/applications/pantheon-%{plug_name}-client.desktop
%{_datadir}/dbus-1/system.d/org.pantheon.ParentalControls.conf
%{_datadir}/dbus-1/system-services/org.pantheon.ParentalControls.service
%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.%{plug_name}.policy

%{_unitdir}/pantheon-%{plug_name}.service


%changelog
* Fri Mar 27 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200326.230949.f59dad5a-1
- Update to latest snapshot.

* Thu Mar 19 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200319.190949.7c006199-1
- Update to latest snapshot.

* Wed Mar 11 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200311.180928.49ddd975-1
- Update to latest snapshot.

* Tue Mar 10 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200310.170926.75d89238-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200301.140928.ebdf8911-1
- Update to latest snapshot.

* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200222.140905.2fce8287-1
- Update to latest snapshot.

* Fri Feb 07 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200206.230825.cfabe082-1
- Update to latest snapshot.

* Sat Jan 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200125.150811.ddab3b6d-1
- Update to latest snapshot.

* Sun Jan 05 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200105.170739.917e6322-1
- Update to latest snapshot.

* Sat Jan 04 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200104.090734.7bf19f6f-1
- Update to latest snapshot.

* Wed Jan 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200101.160731.f1069d3e-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191224.220721.6929cdd0-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191220.160927.c2621978-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191219.130721.006a80e2-1
- Update to latest snapshot.

* Thu Dec 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191205.184404.ecea8078-1
- Update to latest snapshot.

* Thu Dec 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191205.085615.54a21476-1
- Update to latest snapshot.

* Mon Dec 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191202.204207.66d3b5ed-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191127.202534.3c869a9f-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191125.092517.5e7551e3-1
- Update to latest snapshot.

* Sat Nov 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191123.072509.5656f854-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191117.202506.2fd7e7ee-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191111.122458.55cee9e9-1
- Update to latest snapshot.

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191108.192421.f7a08d1f-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191107.171117.200d0d57-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191106.234132.989fb0b5-1
- Update to latest snapshot.

* Tue Oct 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191009.172336.c7c8f6ae-2
- Adapt to renamed file.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191009.172336.c7c8f6ae-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191008.150643.edee6228-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191007.152411.18306846-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191003.150246.dda4bb2d-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190928.192318.cc4e18fc-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190924.202136.eef419ea-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190919.182724.851152b8-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190919.173654.613beb3f-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190917.092309.a428fb8f-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190907.212252.53222bc8-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190906.152253.d97a1ff3-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190902.202250.385aac6f-1
- Update to latest snapshot.

* Sun Sep 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190901.162237.abe2a8fc-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190830.212245.e130b49e-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190829.042228.deb7a5f5-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190826.062230.f7883e38-1
- Update to latest snapshot.

* Sat Aug 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190824.082226.41bead2f-1
- Update to latest snapshot.

* Sat Aug 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190824.074944.e6964fc6-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190731.233859.49bdde17-1
- Update to latest snapshot.

* Fri Jul 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190726.101317.55cc777a-1
- Update to latest snapshot.

* Sun Jul 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190721.032446.985658eb-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190717.140846.612af547-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190626.204555.9a279fe8-1
- Update to latest snapshot.

* Thu Jun 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190606.083010.468d5762-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190531.045703.022bb7d0-1
- Update to latest snapshot.

* Tue May 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190528.182937.6d8f1ea0-1
- Update to latest snapshot.

* Wed May 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190515.171438.dddcce2e-1
- Update to latest snapshot.

* Mon Apr 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190422.185921.66912b7f-1
- Update to latest snapshot.

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190413.183214.aa7b806e-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190408.055319.73a00f4f-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190405.220321.2234a64b-1
- Update to latest snapshot.

* Tue Apr 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190402.175218.f2fb4ded-1
- Update to latest snapshot.

* Fri Mar 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190329.024947.bb11c126-1
- Update to latest snapshot.

* Thu Mar 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190320.235824.33fd2a6c-1
- Update to latest snapshot.

* Sun Mar 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190317.172718.dbf955dc-1
- Update to latest snapshot.

* Sat Mar 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190309.133105.5a687045-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190305.032654.e113c92d-1
- Update to latest snapshot.

* Fri Mar 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190301.121452.66ecd97b-1
- Update to latest snapshot.

* Wed Feb 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190227.211812.73d58c52-1
- Update to latest snapshot.

* Wed Feb 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190226.234452.b6022f20-1
- Update to latest snapshot.

* Sun Feb 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190224.055408.1a531baa-1
- Update to latest snapshot.

* Sat Feb 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190223.083810.47f2d96e-1
- Update to latest snapshot.

* Tue Feb 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190219.085514.1a80489d-1
- Update to latest snapshot.

* Sat Feb 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190216.181031.c8421d6b-1
- Update to latest snapshot.

* Fri Feb 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190215.000821.7cf5323b-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190211.214607.73597499-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190211.051150.6c72bb13-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190210.233223.96436b85-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190209.105344.b5c63f1a-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190209.083031.a914b111-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190209.000621.97355a98-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190207.173334.4d91dda1-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190207.142303.19748cd7-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190207.131246.55627b7a-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190207.111228.d5b7c953-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190207.075335.7bb46430-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190207.012528.661051df-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190206.220329.dc8287be-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190206.215922.330affa9-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190206.155605.bedf8a69-1
- Update to latest snapshot.

* Tue Feb 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190205.085926.cf32ffb4-1
- Update to latest snapshot.

* Tue Feb 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190205.010705.9a094071-1
- Update to latest snapshot.

* Sat Feb 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190202.140344.dc624dff-1
- Update to latest snapshot.

* Sat Feb 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190202.091332.4ab4f3b7-1
- Update to latest snapshot.

* Sat Feb 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190202.084540.227f92af-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190125.000146.cd43dea0-1
- Update to latest snapshot.

* Sat Jan 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190119.001013.c6df1bf6-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190114.133121.8a6ac7ea-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190114.001012.3027ce3f-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190106.172254.ca555d20-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190102.214606.607d014e-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181224.000710.139fa257-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.184647.c3b1c5cc-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.173702.db1a9f17-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.151048.81f76cfd-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.065839.4186f6ae-2
- Adapt to added appdata file.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.065839.4186f6ae-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181202.064718.46709aef-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181124.130836.bc4e6b06-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181116.083225.6be1849b-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181108.143058.9ef9b91c-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181107.145426.909d85f2-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181107.134425.aa7d4638-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181107.101314.bb547e33-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181105.233133.a4adbaf2-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181102.100616.a096faff-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181102.100616.a096faff-1
- Update to latest snapshot.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181101.000349.8923e140-1
- Update to latest snapshot.

* Wed Oct 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181031.015249.407745e0-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181027.232032.691be233-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181026.150254.2eacd90c-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181025.160340.57956545-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181025.081651.a6ce2a6c-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181021.114419.16967551-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181018.001059.672bd765-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181017.000739.8824dd39-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181015.164219.3d16b2d8-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181015.145217.42fe41df-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181014.002321.8bbd6179-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181013.145014.f8cd220f-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181013.010321.35d3b463-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181012.000530.2a8df545-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181011.211904.5f48c4ac-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181011.175701.b14db1ce-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181011.135427.b983496c-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181011.121055.4e15d75c-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181011.043649.6b29d421-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181011.014937.afc4fccb-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181011.001305.973c1031-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181009.164104.91f054cb-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181009.154201.3861eb6a-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181009.091942.f5e6fee1-1
- Update to version 2.1.5.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181009.091942.f5e6fee1-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181008.185415.c2d04cd7-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181008.000536.705ce27e-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181007.024006.adb5da33-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181002.043917.b224a07b-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181002.000419.ff8e3707-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180920.000456.63833f7c-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180917.143318.ae43e307-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180908.000811.3f4efedf-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180907.000617.3c09da2f-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180905.233113.62fb681a-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180901.000856.1709eddd-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180830.000759.45dea96d-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180829.163419.a79580c0-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180829.063843.1cc0eb08-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180826.000450.bed1c2cb-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180822.000913.5277ff8b-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180818.135637.d57081f8-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180813.000354.3f3d00b4-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180813.000354.3f3d00b4-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180803.000437.95a5c501-1
- Update to latest snapshot.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180727.000930.99878371-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180724.000546.90a7bb4c-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180722.121131.9253fc08-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180722.000356.8230cd53-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180713.000410.0bbfd594-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180709.201419.68e1f12f-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180623.001155.f8c1d69c-1
- Update to version 0.1.4.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180623.001155.f8c1d69c-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180615.001120.de3ab5db-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180614.000920.7fc46655-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180612.072854.eab128e9-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180610.001215.3b6fa787-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180608.081423.239155ff-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180607.000939.52d71c71-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180606.000924.6858641b-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180605.041109.0383e05d-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180604.175728.71f09f67-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180604.164615.80cfbe61-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180604.123302.c90cee70-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180603.115223.464e77c4-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180602.000633.29f35b8e-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180601.000820.f658aac0-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180531.000317.94b8e8e3-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180530.000419.a40ba02a-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180529.001250.7fde0106-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180528.000047.50d2f63a-2
- Adapt to upstream file changes.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180528.000047.50d2f63a-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180525.203912.1fa082ff-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180513.001142.e8e88bef-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180512.001204.7877111f-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180511.000642.7f0bdf74-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180507.000317.32e89360-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180504.000642.b68b16de-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180429.131912.c396426b-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180425.204053.bbba4a67-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180415.001029.f5fc7c17-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180403.000600.f4c769e1-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180328.192610.9e722115-2
- Adapt to upstream fixes.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180328.192610.9e722115-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180327.202202.06db5f3d-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180325.000933.669ee27d-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180322.170111.5087a6e2-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180314.000232.95a33998-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180310.000436.b6fba9b9-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180309.000615.86adea31-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180305.114726.2d7c2bd4-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180227.000419.0e3200f9-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180226.170923.8611c8e3-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180226.000848.ef7ca2d4-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180225.000935.57fd3e5c-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180224.000426.716b1252-2
- Adapt to cmake -> meson switch.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180224.000426.716b1252-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180223.192854.0018c4d2-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180223.063429.4cbf94d1-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180222.004739.68037202-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180221.011751.96c418a7-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180213.095538.4356d371-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180211.000859.d5bd5de5-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180209.001023.dd96eb69-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180205.001155.c715f5a8-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171215.001210.194fff86-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171118.233833.bf0e2f2e-2
- Merge .spec file from elementary-stable.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171118.233833.bf0e2f2e-1
- Update to latest snapshot.

* Wed Nov 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171108.084632.c50d23f7-1
- Update to latest snapshot.

* Sat Oct 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171027.230032.eb643fc2-1
- Update to latest snapshot.

* Sat Oct 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171007.070544.c2a88230-1
- Update to latest snapshot.

* Tue Sep 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170926.000820.17cb39cd-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170925.094259.25517e83-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170731.085116.57c4571a-1
- Update to version 0.1.3.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev315-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev314-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev312-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev310-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev309-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev307-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev306-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev284-2
- Adapt to upstream file changes.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev284-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev283-1
- Update to latest snapshot.

* Sun Apr 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev282-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev279-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev278-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev277-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev276-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev275-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev274-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev273-1
- Update to latest snapshot.

* Fri Feb 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev272-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev271-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev270-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev269-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev268-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev267-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev266-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev264-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev263-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev262-1
- Update to latest snapshot.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev261-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev260-1
- Update to latest snapshot.

* Sun Feb 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev259-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev258-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev256-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev255-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev254-1
- Update to version 0.1.2.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev253-1
- Update to version 0.1.2.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev252-1
- Update to version 0.1.2.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev252-1
- Update to version 0.1.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev249-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev248-2
- Fix systemd service installation.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev248-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev246-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev245-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev244-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev243-2
- Include new config file.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev243-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev242-1
- Update to version 0.1.1.



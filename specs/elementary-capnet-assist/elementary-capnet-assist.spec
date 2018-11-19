%global appname io.elementary.capnet-assist

Name:           elementary-capnet-assist
Summary:        Captive Portal Assistant for elementary
Version:        2.2.2+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-ui-3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       NetworkManager

Provides:       capnet-assist = %{version}-%{release}
Obsoletes:      capnet-assist < 0.2.2-1


%description
Assists users in connective to Captive Portals such as those found on
public access points in train stations, coffee shops, universities,
etc.

Upon detection, the assistant appears showing the captive portal. Once
a connection is known to have been established, it dismisses itself.

Written in Vala and using WebkitGtk+.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_sysconfdir}/NetworkManager/dispatcher.d/90captive_portal_test

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181119.091231.da274950-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181119.044952.516e645f-1
- Update to latest snapshot.

* Sun Nov 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181118.102440.a8cdd1e8-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181117.000149.5ae3d6a1-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181115.084427.ef6ff317-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181109.131253.d03d9bc9-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181109.073829.f1144c6a-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181108.130526.27998cae-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181108.031937.4387b071-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181107.231031.97d2d31b-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181107.172207.f710c42e-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181107.112252.5bd03685-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181107.104933.70f91ce1-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181107.081035.3ac49bb1-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181107.001656.ccc73fa4-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181104.000310.d68cd7be-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181103.131409.38641918-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181103.130016.88377307-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181030.173058.d98e7fda-2
- Occasional mass rebuild.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181030.173058.d98e7fda-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181028.161857.ac6c2d31-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181026.221211.6708a39c-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181025.071138.ee79716b-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181022.000310.d8df3c33-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181021.094908.5c5fd002-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181020.001029.1b0e1668-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181016.102029.e026ec84-1
- Update to version 2.2.2.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181016.102029.e026ec84-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181015.231938.a8497d18-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181015.160541.dbed6ab9-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181015.145604.cab3f711-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181014.021222.b930d649-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181014.000312.7d04554f-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181013.204419.3f3d3340-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181013.172252.3b567bba-2
- Adapt to upstream file changes.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181013.172252.3b567bba-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181013.123745.c189db33-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181013.082628.8433be34-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181013.005222.324dcf63-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181012.231312.becc6b68-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181012.224522.a8bbfdad-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181012.210558.beb5f189-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181012.205552.1253c81b-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181012.193029.04d79296-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181012.174642.69d26bed-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181012.000450.eabaed1c-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181009.181026.3a850752-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181008.192713.43939eb0-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181007.023705.c467b507-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181005.101404.2e49e2c3-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181003.115905.7205fa27-1
- Update to version 2.2.1.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git181003.115905.7205fa27-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180921.000620.5646bc72-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180906.043026.3347dd93-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180831.000436.a4f98330-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180830.000651.13540736-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180829.060452.3c8c6314-1
- Update to latest snapshot.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180828.183235.054c9384-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180826.000415.0c4d3146-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180822.000842.900373ea-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180818.124545.d5090432-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180812.120121.35c08eb5-2
- Occasional mass rebuild.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180812.120121.35c08eb5-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180720.111411.552d4be2-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180718.000542.44abc781-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180716.214233.b869a547-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180710.000329.4e03e93d-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180709.200041.185cf071-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180705.000702.6686dc59-2
- Adapt to upstream file changes.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180705.000702.6686dc59-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180703.190346.f1fbb7b4-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180613.000652.07fe8155-1
- Update to version 0.2.2.


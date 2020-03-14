%global appname io.elementary.capnet-assist

Name:           elementary-capnet-assist
Summary:        Captive Portal Assistant for elementary
Version:        2.2.4+git%{date}.%{commit}
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
* Sat Mar 14 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git200314.130930.53994754-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git200301.150927.c39f6791-1
- Update to latest snapshot.

* Tue Feb 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git200225.220858.d385bdf8-1
- Update to latest snapshot.

* Sun Feb 16 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git200216.053231.1ecc082b-1
- Update to latest snapshot.

* Sat Jan 18 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git200118.010801.d0f5a897-1
- Update to latest snapshot.

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git200108.000744.830a4245-1
- Update to latest snapshot.

* Sun Dec 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191229.052124.ad764cd8-1
- Update to latest snapshot.

* Fri Dec 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191227.100721.5aa701d8-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191226.035200.70550ad2-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191218.191214.85fedb67-1
- Update to latest snapshot.

* Sun Dec 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191215.020707.c314c7e7-1
- Update to latest snapshot.

* Mon Dec 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191209.215002.341d668e-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191204.212603.d28667a9-1
- Update to latest snapshot.

* Tue Dec 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191203.092533.b49cfb6e-1
- Update to latest snapshot.

* Thu Nov 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191128.162447.8217261a-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git191122.032434.d3667867-1
- Update to version 2.2.4.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191122.032434.d3667867-1
- Update to latest snapshot.

* Wed Nov 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191120.164039.47735371-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191115.232452.85f1dae4-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191115.220049.b0f0828d-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191111.122417.8610b4eb-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191109.112414.a9fc19ba-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191106.164342.656f2470-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191030.234459.0dea517c-1
- Update to latest snapshot.

* Sun Oct 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191006.142346.beed8b23-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191003.165059.d3230d30-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git191001.203044.5643b240-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190919.182658.830c09f6-1
- Update to latest snapshot.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190913.032242.d972aa03-1
- Update to latest snapshot.

* Tue Sep 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190910.172319.2a2a22ae-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190909.170125.066a8dd1-1
- Update to latest snapshot.

* Thu Jul 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190711.204634.c09880de-1
- Update to latest snapshot.

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190703.144518.a0010094-1
- Update to latest snapshot.

* Thu Jun 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190627.214634.6a40f845-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190626.204234.af2d4665-1
- Update to latest snapshot.

* Wed Apr 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190417.205339.a63bbe16-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190406.185211.06c619ae-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190312.202651.884ffeb8-1
- Update to latest snapshot.

* Mon Mar 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190311.202148.2e09e249-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190206.180921.fb494a82-1
- Update to latest snapshot.

* Mon Feb 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190201.150729.8c46d87c-1
- Update to version 2.2.3.

* Fri Feb 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190201.150729.8c46d87c-1
- Update to latest snapshot.

* Thu Jan 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190131.215547.0476e58b-1
- Update to latest snapshot.

* Sat Jan 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190112.000853.1ce7c420-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190111.125636.8a9fdada-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190104.212339.9790f7b6-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190103.000411.5c7ba311-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181208.000428.e37b52c2-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181202.201456.83076780-1
- Update to latest snapshot.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181129.120343.5643698c-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181128.142057.2e04b935-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181122.083854.7c043a2f-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181122.000209.dfb17b76-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181121.080058.f227b9a4-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181120.180735.c5e824ba-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181120.161936.153adaab-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181120.121441.8d4efa9b-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181120.000312.b0b35233-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181119.171244.0d3d4f1f-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181119.154338.76863851-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git181119.100550.9c9f3a46-1
- Update to latest snapshot.

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


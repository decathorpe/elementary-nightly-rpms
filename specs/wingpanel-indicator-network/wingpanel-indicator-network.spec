%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.network

Name:           wingpanel-indicator-network
Summary:        Network Indicator for wingpanel
Version:        2.2.2+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel%{?_isa}


%description
A network indicator for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang network-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f network-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libnetwork.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191114.062559.3a7bf5f1-1
- Update to latest snapshot.

* Tue Nov 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191112.162414.12171a01-1
- Update to latest snapshot.

* Sun Nov 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191110.202414.9d4a1322-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191109.152415.4f18250e-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191109.063554.6d99c3d7-1
- Update to latest snapshot.

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191107.214110.dc5ac8ec-2
- Package and verify appdata file.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191107.214110.dc5ac8ec-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191107.205619.d7613d83-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191106.004315.46c6bd5b-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191003.153042.72408cd4-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190925.201935.cf511cf2-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190925.190738.c28c3011-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190924.205515.7c5e0d1c-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190911.144851.405d9825-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190827.174802.13cbb48a-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190626.204711.8b0b18f1-1
- Update to latest snapshot.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190409.215330.36d451d9-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190125.133358.c080cb04-1
- Update to version 2.2.2.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190125.133358.c080cb04-1
- Update to latest snapshot.

* Wed Jan 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190116.000413.d8becd20-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190115.134158.ab736bab-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190103.181104.98284666-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181218.000208.73671139-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181215.144320.d4777a0f-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181211.110340.06d548a3-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181206.050539.dc93e721-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181204.201537.e49aee51-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181204.182241.57a2b252-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181204.174243.a035a042-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181204.070627.a26e8eb2-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181202.065532.85b38c40-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181202.050150.5d5f7972-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181202.050047.a8166b45-1
- Update to latest snapshot.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181129.120658.df6fbe51-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181124.111048.b871fb31-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181121.142039.739775ae-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181120.084543.ce10f927-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181104.222316.397fbc9e-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181026.014825.ec85ad69-2
- Occasional mass rebuild.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181026.014825.ec85ad69-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181024.132759.d7d7b149-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181019.180529.9aa6034f-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181013.172020.c1f44d74-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181003.080351.c7579507-1
- Update to version 2.2.1.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181003.080351.c7579507-1
- Update to latest snapshot.

* Sat Sep 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180922.001144.d8ae0885-1
- Update to latest snapshot.

* Fri Sep 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180914.133546.906f6816-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180906.042000.305abb5a-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180829.054213.9cb21506-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180813.000431.ea3c400f-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180813.000431.ea3c400f-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180721.183208.b7834918-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180721.000812.c80474f5-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180720.192159.3c005aae-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180703.190609.b67512a7-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180613.154841.418fef62-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180607.092446.ed75529b-1
- Update to version 2.2.0.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180607.092446.ed75529b-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180604.132804.b38eccfd-2
- Adapt to CMake -> meson switch.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180604.132804.b38eccfd-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180603.061507.9a217bea-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180602.195955.7c980988-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180601.001114.216eff24-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180531.082653.31a1730f-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180529.001558.aed5b925-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180525.163707.967c21ba-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180520.151009.dbc6f8bc-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180515.182521.c0dfab14-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180511.171240.ac56b5f7-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180511.000727.5ce2ba84-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180510.172407.1c4ac19e-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180510.091229.90110d06-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180509.193546.258ffa47-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180509.000937.bd6b6dc9-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180508.092316.2c0ee2d3-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180506.001217.85c5f37e-1
- Update to latest snapshot.

* Wed May 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180502.181048.30b0fb21-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180501.180435.1c8caaa5-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180428.233634.6257ee6a-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180407.211419.56e25686-2
- Adapt to upstream file changes.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180407.211419.56e25686-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180329.194905.258c958c-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180328.000600.4cf0a80a-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180325.001130.3f3960c3-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180322.021430.27cf3620-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180321.191751.4e24b36c-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180314.000420.c0256e27-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180312.001152.41efda0e-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180308.142523.558fed3f-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180213.233558.4d60c33b-1
- Update to latest snapshot.

* Wed Feb 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180207.034654.1960ed8d-1
- Update to latest snapshot.

* Sun Feb 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180204.000911.17434f6b-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180117.001254.7a085efc-1
- Update to latest snapshot.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180116.192304.2954c6b9-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git171229.012743.d2b05bfb-2
- Merge .spec file from fedora.

* Fri Dec 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git171229.012743.d2b05bfb-1
- Update to latest snapshot.

* Thu Dec 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git171228.151037.ab3ae06e-1
- Update to latest snapshot.

* Thu Dec 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git171228.141715.736190be-1
- Update to latest snapshot.

* Mon Dec 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git171218.222946.b44f9956-1
- Update to latest snapshot.

* Mon Dec 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git171218.000956.635e25d5-2
- Adapt to upstream dependency changes.

* Mon Dec 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git171218.000956.635e25d5-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git171117.184237.afa62679-1
- Update to latest snapshot.

* Thu Oct 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git171025.222657.f2a19ff3-1
- Update to latest snapshot.

* Thu Sep 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170920.201119.4332e2c2-1
- Update to latest snapshot.

* Wed Sep 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170920.164220.35032b96-1
- Update to latest snapshot.

* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git170918.171045.93e6e131-1
- Update to version 2.1.1.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git170918.171045.93e6e131-1
- Update to latest snapshot.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git170917.193502.56cfdfd1-1
- Update to latest snapshot.

* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git170915.162115.1b3a3da2-1
- Update to latest snapshot.

* Wed Sep 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git170913.000954.7db07b75-1
- Update to version 2.1.0.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev298-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev291-1
- Update to latest snapshot.

* Tue Jul 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev289-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev286-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev285-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev282-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev254-1
- Update to latest snapshot.

* Fri May 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev252-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev236-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev235-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev234-1
- Update to latest snapshot.

* Mon Apr 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev233-1
- Update to latest snapshot.

* Wed Apr 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev232-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev231-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev230-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev229-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev228-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev227-1
- Update to latest snapshot.

* Wed Mar 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev226-1
- Update to latest snapshot.

* Sun Mar 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev225-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev224-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev223-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev222-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev221-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev220-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev219-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev218-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev217-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev216-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev215-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev214-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev213-1
- Update to version 2.0.2.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev212-1
- Update to version 2.0.2.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev212-1
- Update to version 2.0.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev211-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev210-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev209-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev208-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev207-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev206-1
- Update to latest snapshot.

* Mon Nov 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev205-1
- Update to latest snapshot.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev204-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev203-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev202-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev201-1
- Update to latest snapshot.

* Fri Nov 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev200-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev199-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev198-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev197-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev196-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev195-1
- Update to latest snapshot.

* Sat Oct 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev194-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev193-1
- Update to version 2.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev193-2
- Spec file cleanups.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev193-1
- Update to version 2.0.1.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev192-1
- Update to latest snapshot.

* Thu Aug 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev190-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev189-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev188-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev187-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev186-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev185-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev185-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev184-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev183-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev182-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev180-1
- Update to latest snapshot.

* Fri Jul 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev179-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev178-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev177-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev176-1
- Update to latest snapshot.

* Mon Jul 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev175-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev174-2
- Update for packaging changes.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev174-1
- Update to latest snapshot.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev173-1
- Update to latest snapshot.

* Sun Jul 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev172-1
- Update to latest snapshot.

* Sat Jul 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev171-1
- Update to latest snapshot.

* Fri Jul 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev170-1
- Update to latest snapshot.

* Tue Jun 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev169-1
- Update to latest snapshot.

* Thu Jun 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev168-1
- Update to latest snapshot.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev167-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev166-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev165-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev164-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev163-1
- Update to latest snapshot.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev162-1
- Update to latest snapshot.

* Sat Jun 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev161-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev160-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev160-2
- Update for packaging changes.

* Sat May 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev160-1
- Update to latest snapshot.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev159-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev158-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev158-1
- Initial package.



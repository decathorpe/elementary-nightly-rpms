%global srcname videos
%global appname io.elementary.videos

Name:           elementary-videos
Summary:        Video player and library app from elementary
Version:        2.6.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  /usr/bin/appstream-util

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.4.1
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)

Obsoletes:      audience
Provides:       audience


%description
A modern video player that brings the lessons learned from the web home
to the desktop.


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

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml || :


%files -f %{appname}.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3+git190313.163147.2bf66ce0-1
- Update to latest snapshot.

* Sun Mar 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3+git190303.211355.f8a128f1-1
- Update to latest snapshot.

* Tue Feb 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3+git190226.203312.a52849ed-1
- Update to latest snapshot.

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3+git190123.063856.4ab18aea-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3+git190122.083055.f2399a8e-1
- Update to latest snapshot.

* Wed Jan 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3+git190116.000251.4c4c2390-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3+git190115.133916.2978939d-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3+git190114.001108.9fe509f3-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3+git190109.101908.03f48410-1
- Update to version 2.6.3.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git190109.101908.03f48410-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git190107.000359.09358a42-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git190106.115027.d50c8ee3-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git190105.032530.9e68efe9-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git190102.190929.635073a2-1
- Update to latest snapshot.

* Sun Dec 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181223.060253.ae65561b-1
- Update to latest snapshot.

* Sun Dec 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181223.055815.d827c02c-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181218.104953.d56f5e9e-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181218.000146.1e20c666-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181215.145511.9e06f3f3-1
- Update to latest snapshot.

* Fri Dec 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181214.220644.a0a58e09-1
- Update to latest snapshot.

* Fri Dec 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181214.210953.017a10a9-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181212.060621.cefb440c-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181206.080521.b65756f5-1
- Update to latest snapshot.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181129.120639.42c913a1-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181124.121037.25165e3a-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181108.190151.0fcc58d7-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181108.141505.67a7c678-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181104.183350.9c2772db-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181101.200144.c64b1e84-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181101.200144.c64b1e84-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181024.141252.b2fedcbf-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181021.081407.43497896-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181013.000932.c11ccae0-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181012.000547.ab3ca0d2-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181009.000148.a4d46860-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181008.000606.bbb2324b-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181007.024043.43e925fc-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2+git181001.065212.beb0c225-1
- Update to version 2.6.2.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git181001.065212.beb0c225-1
- Update to latest snapshot.

* Sun Sep 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180923.104050.99750aa2-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180919.001011.4bfd6b59-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180906.132114.8f0b50ac-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180906.000937.c2668daf-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180901.000925.0e635134-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180830.181414.efb9fe04-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180830.000339.72336f98-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180829.053512.687ab674-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180826.000217.8f5f2360-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180822.000923.b208a153-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180819.000253.4eb5f1eb-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180818.144603.6e9aad70-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180803.000450.b2aa977a-2
- Occasional mass rebuild.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git180803.000450.b2aa977a-1
- Update to version 2.6.1.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180731.091604.f6358c33-1
- Update to latest snapshot.

* Wed Jul 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180725.000054.cd3922e7-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180724.000558.7c87ff6c-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180722.000412.2ec26b27-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180720.124114.f231d45c-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180719.000745.9ea1a23d-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180718.000552.074f3141-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180717.152106.73e931a2-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180717.113156.83131ad2-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180717.094115.1b73defd-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180717.012849.4d33d3af-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180713.000434.a8a76e21-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180710.000403.6ed5f948-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180704.181848.b6ea7100-1
- Update to version 0.2.6.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180704.181848.b6ea7100-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180627.170451.d4953c5e-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180615.000106.9257d777-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180614.164800.7836bc60-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180614.085243.90fa56ee-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180613.000825.75c7f9ee-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180610.001238.286e4856-1
- Update to version 0.2.5.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180610.001238.286e4856-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180608.001257.ee0bf3f5-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180605.000606.60cb4128-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180604.001001.b6efb2a4-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180603.061649.62bf0584-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180602.165941.06dcaff7-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180602.100834.75f75ff2-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180601.000215.bd1bee8c-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180531.080035.9249fc0c-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180530.035506.1492662b-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180525.211157.c2cc0c40-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180523.033235.b0e05b89-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180518.000811.504c49cd-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180517.000450.bf81cfb9-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180516.120445.6b56559b-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180516.095151.6f15912a-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180516.075811.be8b0819-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180510.172239.429c4dd9-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180505.054646.dba9f209-2
- Adapt to CMake -> meson switch.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180505.054646.dba9f209-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180420.024025.a95d3fdf-1
- Update to latest snapshot.

* Thu Apr 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180419.030443.7aff27df-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180416.184456.9a9dc42b-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180416.161119.7548fb7e-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180416.155605.8db92d62-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180328.182557.decf16f8-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180318.000939.8ca8dcd9-2
- Adapt to upstream file changes.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180318.000939.8ca8dcd9-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180220.202921.4531749a-1
- Initial package.



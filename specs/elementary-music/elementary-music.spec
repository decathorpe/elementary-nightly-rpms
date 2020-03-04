%global srcname music
%global appname io.elementary.music

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-music
Summary:        Music player and library from elementary
Version:        5.0.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.39
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
#BuildRequires:  pkgconfig(json-glib-1.0)
#BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libgpod-1.0)
#BuildRequires:  pkgconfig(libsignon-glib) >= 2.0
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
#BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       hicolor-icon-theme

# elementary-music explicitly requires the sqlite libgda database provider
Requires:       libgda-sqlite%{?_isa}


Provides:       noise
Obsoletes:      noise


%description
Music is a fast and beautiful GTK3 audio player with a focus on music
and libraries. It handles external devices, CDs, and album art. Music
utilizes Granite for a consistent and slick UI.


%package        devel
Summary:        The official elementary music player (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Music is a fast and beautiful GTK3 audio player with a focus on music
and libraries. It handles external devices, CDs, and album art. Music
utilizes Granite for a consistent and slick UI.

This package contains files needed for developing with Music.


%prep
%autosetup


%build
%meson -Dplugins="audioplayer,cdrom,ipod"
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/lib%{appname}-core.so.0
%{_libdir}/lib%{appname}-core.so.0.1

%{_libdir}/%{appname}/

#%%{_datadir}/accounts/applications/noise-lastfm.application
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multimedia-audio-player.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%files devel
%{_libdir}/lib%%{appname}-core.so
%{_libdir}/pkgconfig/%{appname}-core.pc

%{_includedir}/%{appname}-core.h

%{_datadir}/vala/vapi/%{appname}-core.deps
%{_datadir}/vala/vapi/%{appname}-core.vapi


%changelog
* Wed Mar 04 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200304.225004.ce88ec3e-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200301.130906.0ac20c0d-1
- Update to latest snapshot.

* Thu Feb 27 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200227.134048.7aefb05e-1
- Update to latest snapshot.

* Tue Feb 25 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200225.184352.30f62cfb-1
- Update to latest snapshot.

* Tue Feb 25 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200225.144008.7ebaef7d-1
- Update to latest snapshot.

* Tue Feb 25 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200225.130904.39291b13-1
- Update to latest snapshot.

* Fri Feb 14 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200214.170841.126370fe-1
- Update to latest snapshot.

* Sat Jan 25 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200125.150810.df558a8d-1
- Update to latest snapshot.

* Fri Jan 24 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200124.010804.82436cdd-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200121.160800.40134b15-1
- Update to latest snapshot.

* Sun Jan 19 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200119.130758.6989678a-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200115.215753.b8d52bf1-1
- Update to latest snapshot.

* Sun Jan 12 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200112.150748.b10d6e4c-1
- Update to latest snapshot.

* Sun Jan 05 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200105.141802.c89ca76f-1
- Update to latest snapshot.

* Fri Jan 03 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git200103.160731.8240471e-1
- Update to latest snapshot.

* Mon Dec 30 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191230.131426.7afcc035-1
- Update to latest snapshot.

* Sat Dec 28 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191228.101111.d99ac1ca-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191218.202911.ea597cc3-1
- Update to latest snapshot.

* Sun Dec 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191215.020703.eaa6af96-1
- Update to latest snapshot.

* Fri Dec 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191206.205609.8f6cf0a1-1
- Update to latest snapshot.

* Fri Dec 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191206.091357.71c9b94f-1
- Update to latest snapshot.

* Thu Dec 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191205.214123.19fed8a1-1
- Update to latest snapshot.

* Sun Dec 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191201.102452.e8752191-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191125.092441.7c9b58c4-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191122.082434.2edf3597-1
- Update to latest snapshot.

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191119.164540.5daae976-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191117.202428.9599ef88-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191116.172426.d92d6580-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191111.122420.1bc936a3-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191109.122419.da34b8bc-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191106.005108.7e62dae2-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191105.160800.dd94ba72-1
- Update to latest snapshot.

* Sun Oct 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191027.192359.77218061-1
- Update to latest snapshot.

* Fri Oct 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191011.152331.0b9809ea-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191005.151115.714609cf-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191005.112319.4fba5999-1
- Update to latest snapshot.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191004.171731.b8745195-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191003.214615.c7bed9ab-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191002.213942.48af7b3a-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191002.172944.86ed923e-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191001.203231.b71f8d10-1
- Update to latest snapshot.

* Sun Sep 22 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190922.192301.ab9c7031-1
- Update to latest snapshot.

* Sat Sep 21 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190921.103450.4c134452-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190918.185241.e6802967-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190918.164542.16a7d097-1
- Update to latest snapshot.

* Sat Sep 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190914.203511.2d7e0788-1
- Update to latest snapshot.

* Sat Sep 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190914.122253.1cb5c1a0-1
- Update to latest snapshot.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190913.183724.6247a60c-1
- Update to latest snapshot.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190913.174801.aba23eb6-1
- Update to latest snapshot.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190913.164619.bf29959c-1
- Update to latest snapshot.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190913.155219.96dfe089-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190907.043725.77ac20b7-1
- Update to latest snapshot.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190905.220347.125d3f8e-1
- Update to latest snapshot.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190905.163542.8b5036ab-1
- Update to latest snapshot.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190905.053409.94888d75-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190829.152223.4d4b8151-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190827.222241.7df9fb09-1
- Update to latest snapshot.

* Wed Jul 24 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190724.122639.c277aa76-1
- Update to latest snapshot.

* Sun Jul 21 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190721.102430.ad54e098-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190716.161513.62f2cce5-1
- Update to latest snapshot.

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190703.131717.3fa9ec36-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190626.204347.28bba6d9-1
- Update to latest snapshot.

* Mon Jun 10 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190610.063010.11fc2d18-1
- Update to latest snapshot.

* Wed May 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190515.020253.dd0da778-1
- Update to latest snapshot.

* Sat Apr 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190427.165142.6719bba4-1
- Update to latest snapshot.

* Tue Apr 23 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190423.223145.b759f4ba-1
- Update to latest snapshot.

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190418.003147.a6eca03b-1
- Update to version 5.0.4.

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190418.003147.a6eca03b-1
- Update to latest snapshot.

* Wed Apr 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190417.084655.e75ec609-1
- Update to latest snapshot.

* Wed Apr 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190417.001505.7046476b-1
- Update to latest snapshot.

* Thu Apr 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190411.225329.af6fa11c-1
- Update to latest snapshot.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190409.204616.586122e4-1
- Update to latest snapshot.

* Sun Apr 07 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190407.190617.c4f92b16-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190405.215215.95a86d33-1
- Update to latest snapshot.

* Fri Mar 29 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190329.025243.52d8b5aa-1
- Update to latest snapshot.

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190318.134832.80bcdfda-1
- Update to latest snapshot.

* Sun Mar 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190317.012709.808b6812-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190312.212702.a6b80613-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190312.153105.881af416-1
- Update to latest snapshot.

* Sun Mar 03 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190303.082642.2e87f042-1
- Update to latest snapshot.

* Sat Mar 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190302.225959.b320ecb4-1
- Update to latest snapshot.

* Sat Mar 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190302.210352.701454c8-1
- Update to latest snapshot.

* Thu Feb 28 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190226.193946.91273478-1
- Update to version 5.0.3.

* Tue Feb 26 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190226.193946.91273478-1
- Update to latest snapshot.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190222.000442.f88c5ba2-1
- Update to latest snapshot.

* Wed Feb 20 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190220.215517.3f18fc0c-1
- Update to latest snapshot.

* Mon Feb 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190218.205205.03f89d20-1
- Update to latest snapshot.

* Sun Feb 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190217.133803.a18edd73-1
- Update to latest snapshot.

* Sun Feb 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190217.115111.69bd0830-1
- Update to latest snapshot.

* Sun Feb 17 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190217.105304.b1c6094f-1
- Update to latest snapshot.

* Wed Feb 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190213.074532.983e2191-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190212.000649.22724031-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190207.000626.723d3075-1
- Update to latest snapshot.

* Tue Feb 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190205.201632.81d0edad-1
- Update to latest snapshot.

* Wed Jan 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190116.212853.5db553f7-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190115.130959.4a952215-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190115.000545.a513ecaf-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190114.000901.003dbeb7-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190109.134909.e93a77cd-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190109.000630.8ac75043-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190106.171703.3bbffe88-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190105.175639.97ecf642-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190105.031145.fd1ff34e-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190105.030021.ca67e106-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190102.191546.c49dd991-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190102.180115.d3440901-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git181224.000651.1b101cba-1
- Update to latest snapshot.

* Sun Dec 23 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git181223.065526.e52c23c7-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git181218.120714.9965f3f3-1
- Update to version 5.0.2.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181218.120714.9965f3f3-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181218.053537.9f1e34e6-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181213.143735.305ed7ee-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181212.230213.77d05b07-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181208.214318.bcaa4c28-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181204.012459.b30c3077-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181203.150113.60b216ed-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181203.134117.b0b6f485-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181203.091448.58cf17e7-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181202.062729.8c0a7ef6-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181130.201535.52af19c1-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181130.104932.cdf95cf4-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181127.214018.65ebfc5f-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181127.125537.246e4175-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181124.121020.03b01508-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181115.183200.dbb9f759-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181109.165041.598eb7d6-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181109.072801.15f4d926-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181109.064858.600b59a8-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181108.031647.cd3d7ed9-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181107.163812.81921e11-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181107.014005.d1e8e6b7-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181106.204745.39fac62d-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181106.165318.ce308a2a-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181106.130950.9e223e82-2
- Require granite >= 5.2.0.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181106.130950.9e223e82-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181106.100348.d5565f12-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181106.045308.c37054a3-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181106.034815.db43a8dc-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181106.021520.44ac0755-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181106.015716.21bb408c-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181105.212347.86597b48-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181104.191936.59ae469e-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181029.194612.5a842c79-2
- Occasional mass rebuild.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181029.194612.5a842c79-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181025.075816.5f5287cb-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181021.140246.4bad5c6f-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181021.093052.c8223cf0-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181020.140023.6be15a67-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181020.085155.face49b3-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181020.021057.6293ae4f-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181018.115400.419daddb-1
- Update to version 5.0.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181018.115400.419daddb-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181018.001011.0d8d56bf-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181016.084210.2eea3779-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181015.000610.02bb1161-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181012.192628.c5ef0080-2
- Adapt to upstream dependency changes.
- Disable last.fm plugin for now.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181012.192628.c5ef0080-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181012.130404.0ab55a73-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181011.140211.5f27827d-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181011.050149.c8d1f6b6-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181009.000125.69699a4f-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181008.000435.1edd13e2-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181005.070054.3bd473c2-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181005.065943.a2bedee2-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181005.000817.f54ebc96-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181003.001049.f70f7c24-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181002.131418.95c2093b-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181002.124521.58cd5add-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181002.000403.1f1da4e5-1
- Update to latest snapshot.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181001.000842.fe1135f3-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180930.205339.352225ce-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180930.081329.78f7be76-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180930.000946.e189feaf-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180929.000924.846f3292-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180928.000709.30245d3f-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180927.001013.4f197b75-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180925.000214.ea1938ca-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180919.000855.c31e2342-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180918.224304.26470407-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180918.210005.1c01beae-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180918.171505.738925b7-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180917.151428.7f5ba85e-1
- Update to latest snapshot.

* Thu Sep 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180913.210929.2972fd13-1
- Update to latest snapshot.

* Thu Sep 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180913.162546.bc4bcf18-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180910.173857.5b7f42f2-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180906.132555.92c91519-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180906.000909.a8024428-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180905.000947.981d60f6-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180901.065231.ccede369-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180831.121003.7548c7c7-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180831.054334.3bc6be43-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180830.000715.dd4eb91a-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180829.193716.6deb8072-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180829.000344.ad6e167f-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180823.000302.67265b0f-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180822.163134.ec424461-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180821.084543.d812b0f1-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180819.000909.fa37145e-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180818.145755.091b82fd-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180816.161302.6a0a3034-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180816.150555.ce5bc1c9-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180815.173724.98f7d32e-2
- Occasional mass rebuild.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180815.173724.98f7d32e-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180814.223603.fc1753de-1
- Update to latest snapshot.

* Tue Aug 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180814.093409.93400863-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180812.132415.185a86ca-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180809.175524.2373b667-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180808.000146.a46112b0-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180803.000418.e0003383-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180730.153133.72b16a00-1
- Update to latest snapshot.

* Sun Jul 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180729.103315.8966822b-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180724.000531.388cc837-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180722.000340.d3f8bf27-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180720.155502.a4de6857-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180720.113526.a0e61f1e-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180720.000709.3a174554-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180718.000548.fb5aaae9-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180717.152406.6cbc1e70-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180716.210834.bd48d6c7-1
- Update to latest snapshot.

* Mon Jul 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180716.085839.47fc42bf-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180715.200621.b2617447-1
- Update to latest snapshot.

* Sat Jul 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.205953.4ceb9f73-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.181351.0476632c-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.172808.6dc2688c-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.083410.5860f3fb-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.065647.4fc72ec6-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180710.150453.e7c8443c-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180709.202319.25b77108-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180709.001022.ec2f96eb-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180705.195011.ae6a30b2-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180705.000718.5a18847f-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180703.000632.449d9f02-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180614.153456.e4d57cfa-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180608.001159.c44d0942-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180606.000847.61bc85dd-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180602.000548.169d58bc-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180601.150419.c7d55442-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180601.000739.964d790c-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180529.001150.616f4863-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180528.105715.7f4cf490-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180527.085147.e0ba7451-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180526.110058.0d0bb4f6-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180525.000818.e74e6a24-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180524.001018.7a90c493-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180514.000221.8725ec4b-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180513.001118.b52faaa1-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180510.171609.d283d094-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180509.071452.da7397aa-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180505.001051.9dbf2cf8-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180429.170404.e85f6131-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180425.000322.c1aa9808-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180424.072921.6d085db0-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180420.165225.93b45982-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180420.001148.93b4c8c3-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180416.165436.d5d8bcba-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180410.154903.33f06372-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180404.234812.3ce84c92-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180401.175353.1aca3514-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180324.210744.56387fab-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180322.190826.51d96059-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180322.172750.4a177a77-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180320.181230.24f7f5cb-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180320.174527.3bfaa27e-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180320.001135.aac483a0-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180316.000359.ca9823d9-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180310.000407.ed7fef59-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180308.163436.b22c5d82-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180308.055720.e1a4a7aa-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180307.000949.701b40f3-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180303.184658.d05f01d4-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180301.000333.1568807b-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180228.105253.2014f665-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180226.000835.c6f9c138-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180225.000921.6753f5c7-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180222.000814.4bc138bc-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180221.000748.8a313c30-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180218.194010.6dcb0030-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180218.144516.38a3fff3-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180217.085028.49610203-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180216.072758.03db7ca8-1
- Update to latest snapshot.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180215.211035.78ae9127-1
- Update to latest snapshot.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180215.074732.4011544c-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180214.105255.73c23e77-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180213.095443.f2e6c45e-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180212.212448.aedb510d-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180211.072649.a71606ed-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.190328.99fed119-2
- Adapt to upstream file changes.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.190328.99fed119-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.174354.e443a1b4-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.154545.6cddd85c-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.063023.1bfc27f9-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180206.205106.116b5497-2
- Adapt to upstream file changes.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180206.205106.116b5497-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180206.001054.91ad20f9-2
- Adapt to cmake -> meson switch.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180206.001054.91ad20f9-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180205.193157.99d7c302-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180205.154515.e8cb1611-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180205.001129.34dc472f-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180129.000226.e57fd5df-2
- Be lazy about undefined symbols in plugins.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180129.000226.e57fd5df-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180128.000820.e83d5432-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180118.191215.f51a1caf-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180115.162712.65746c64-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180114.203828.063d3ef8-1
- Initial package.



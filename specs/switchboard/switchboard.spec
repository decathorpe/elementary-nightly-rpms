%global appname io.elementary.switchboard

Name:           switchboard
Summary:        Modular Desktop Settings Hub
Version:        2.3.8+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  /usr/bin/appstream-util

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Requires:       hicolor-icon-theme


%description
This project is about the container app only and its library. For
plugins that handle the settings, please refer to
https://launchpad.net/pantheon-plugs.


%package        libs
Summary:        Modular Desktop Settings Hub (shared library)
%description    libs
This project is about the container app only and its library. For
plugins that handle the settings, please refer to
https://launchpad.net/pantheon-plugs.

This package contains the shared library.


%package        devel
Summary:        Modular Desktop Settings Hub (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
This project is about the container app only and its library. For
plugins that handle the settings, please refer to
https://launchpad.net/pantheon-plugs.

This package contains the files required for developing plugs for
switchboard.


%prep
%autosetup


%build
%if 0%{?fedora}
%meson -Dlibunity=true
%else
%meson -Dlibunity=false
%endif

%meson_build


%install
%meson_install

# Create plug directories
mkdir -p %{buildroot}/%{_libdir}/%{name}
mkdir -p %{buildroot}/%{_libdir}/%{name}/hardware
mkdir -p %{buildroot}/%{_libdir}/%{name}/network
mkdir -p %{buildroot}/%{_libdir}/%{name}/personal
mkdir -p %{buildroot}/%{_libdir}/%{name}/system

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%if 0%{?suse_version}
%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%endif

%if 0%{?fedora}
%ldconfig_scriptlets libs
%endif


%files -f %{appname}.lang
%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%files libs
%doc README.md
%license COPYING

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/*

%{_libdir}/lib%{name}-2.0.so.0
%{_libdir}/lib%{name}-2.0.so.2.0


%files devel
%{_includedir}/%{name}-2.0/

%{_libdir}/lib%{name}-2.0.so
%{_libdir}/pkgconfig/%{name}-2.0.pc

%{_datadir}/vala/vapi/%{name}-2.0.deps
%{_datadir}/vala/vapi/%{name}-2.0.vapi


%changelog
* Fri Feb 14 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.8+git200214.170848.f3347b2d-1
- Update to latest snapshot.

* Thu Feb 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.8+git200206.200827.6513af46-1
- Update to latest snapshot.

* Fri Jan 24 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.8+git200124.020804.5c7e6a09-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.8+git200121.160805.1302c752-1
- Update to latest snapshot.

* Sun Jan 19 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.8+git200119.130804.4eeb44ef-1
- Update to latest snapshot.

* Thu Jan 16 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.8+git200116.090751.65165a3d-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.8+git200114.231714.78ad08d8-1
- Update to version 2.3.8.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git200114.231714.78ad08d8-1
- Update to latest snapshot.

* Sat Jan 11 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git200111.120744.bceaa643-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git200106.210737.34501ca9-1
- Update to latest snapshot.

* Wed Jan 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git200101.160728.aecd84ae-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191224.220720.453b584f-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191220.160922.6feb3fbf-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191219.130712.bbf241a3-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191217.190032.b9aba901-1
- Update to latest snapshot.

* Mon Dec 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191209.084042.ed243ead-1
- Update to latest snapshot.

* Sun Dec 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191208.180216.ec1725d0-1
- Update to latest snapshot.

* Sun Dec 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191201.102501.218ca9b9-1
- Update to latest snapshot.

* Fri Nov 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191129.002504.db7cd777-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191127.202507.15f53924-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191125.102451.d57629d7-1
- Update to latest snapshot.

* Sat Nov 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191123.072453.f5d90e48-1
- Update to latest snapshot.

* Wed Nov 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191120.174838.b7ee46e9-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191117.212439.e127068c-1
- Update to latest snapshot.

* Wed Nov 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191113.184304.3e261eb8-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191109.002419.bc87f2e6-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191107.102416.a6c39ea5-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191106.161349.73fbb4ad-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7+git191105.111527.76907654-1
- Update to version 2.3.7.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191105.111527.76907654-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191105.005935.6edda4ea-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191104.220838.62187522-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191104.212427.94f11c77-1
- Update to latest snapshot.

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191103.152413.4174448a-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191101.142412.3f630b84-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191030.162218.9c729372-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191030.023815.c61570d2-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191030.011529.76883d70-1
- Update to latest snapshot.

* Wed Oct 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191023.171547.0f756afa-1
- Update to latest snapshot.

* Wed Oct 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191023.162356.cfa47b86-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191007.152341.da771479-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git191003.162045.986b31d6-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190930.142339.a2d07775-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190919.182830.ae2e708e-1
- Update to latest snapshot.

* Wed Jul 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190730.230044.ff1c0033-1
- Update to latest snapshot.

* Tue Jul 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190730.203543.15c0656d-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190717.125941.ff331c4a-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190626.204433.febc4eea-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190531.044630.7a78a3cc-1
- Update to latest snapshot.

* Mon May 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190513.060641.03c4cc6b-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190407.235311.8eb9f32e-1
- Update to latest snapshot.

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6+git190123.081824.66f829e4-1
- Update to version 2.3.6.

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190123.081824.66f829e4-1
- Update to latest snapshot.

* Wed Jan 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190116.000351.fb3bf7a8-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190115.000630.7a7d25af-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190114.001030.7af4560a-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190110.000735.793da229-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190109.113923.56b36826-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190109.000647.0241d1d9-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190105.032152.5a674b3a-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190104.000840.e5c1d023-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190102.182857.d2d17b64-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190102.115739.e396d903-1
- Update to latest snapshot.

* Sun Dec 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git181223.184329.03852665-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git181219.000754.62b6fb4d-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git181210.193628.209eb936-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git181204.072127.86bc5169-2
- Bump granite requirement to >= 5.2.0.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git181204.072127.86bc5169-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git181129.154840.a2fbb906-1
- Update to version 2.3.5.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181129.154840.a2fbb906-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181116.181512.b33494ca-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181113.204205.07d20df6-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181105.010749.2ebde5a8-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181104.150038.2d85e95c-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181101.193650.a2734c97-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181101.193650.a2734c97-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181030.080845.b077ef8a-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181025.071359.5c223a92-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181022.200323.0720b31c-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181022.181817.9198159a-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181021.112913.1ce7ba85-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181018.103317.600ebccb-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181018.082935.af665e56-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181018.001035.78a4f166-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181008.160313.40905463-1
- Update to version 2.3.4.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.3+git181008.160313.40905463-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.3+git181008.141119.c46ceba7-1
- Update to latest snapshot.

* Sat Oct 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.3+git181004.115654.6682a0cf-1
- Update to version 2.3.3.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git181004.115654.6682a0cf-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180925.000236.9c3388be-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180919.000945.096afa30-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180906.132638.232bda24-1
- Update to latest snapshot.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180902.000848.c324395e-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180831.141222.d7822d90-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180830.000745.3308435e-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180829.063311.63ae4591-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180826.000442.fa141a0d-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180823.000319.2baaa5d9-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180822.165922.9ee45a29-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180818.133627.7c1c62ee-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180814.172549.0fc05c54-2
- Occasional mass rebuild.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180814.172549.0fc05c54-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180812.135133.1c283da0-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180808.150056.ded19539-2
- Adapt to upstream file changes.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180808.150056.ded19539-1
- Update to latest snapshot.

* Mon Aug 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180804.135558.b306c7db-2
- Temporarily create plug directories downstream.

* Sat Aug 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180804.135558.b306c7db-1
- Update to latest snapshot.

* Sat Aug 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180803.213259.eebd6925-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180803.000431.2151be11-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180731.220416.8108bdff-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180730.083339.ccf88cf2-1
- Update to latest snapshot.

* Sun Jul 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2+git180729.103021.100182ce-1
- Update to version 2.3.2.

* Sun Jul 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180729.103021.100182ce-1
- Update to latest snapshot.

* Sat Jul 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180728.125638.0279a081-1
- Update to latest snapshot.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180727.082305.cd4124ea-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180724.030738.924b9bd0-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180721.150903.ff85ad71-2
- Add missing BR: gcc, gcc-c++.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180721.150903.ff85ad71-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180704.005355.40b1a6e4-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180614.081606.46ca0351-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180608.001228.57f7b9db-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git180606.092140.612dbd88-1
- Update to version 2.3.1.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180606.092140.612dbd88-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180602.000652.ceedfdbc-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180601.000805.1ada968a-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180530.000437.08096b02-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180527.161301.af009a29-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180515.000627.2f84a127-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180514.000232.a2c22c33-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180512.001149.cae0da92-1
- Update to latest snapshot.

* Wed May 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180501.204356.84ea59bb-2
- Adapt to upstream file changes.

* Wed May 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180501.204356.84ea59bb-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180425.000350.821e70b4-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180321.193212.da62a1dc-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180318.034729.64476ea8-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180226.183446.ed97cec0-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180226.165135.142c0bc4-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180219.190602.2e7eac14-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180217.101019.dd577936-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180209.001017.e32403ac-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180119.115123.0d9d2882-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180119.115108.c580f502-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180103.020349.e2ba68da-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180103.020349.e2ba68da-1
- Update to latest snapshot.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git171112.174251.07bacd7e-1
- Update to latest snapshot.

* Wed Nov 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git171107.234007.d55c2d30-1
- Update to latest snapshot.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git171104.071514.9d0fa5f7-1
- Update to latest snapshot.

* Wed Oct 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git171018.163924.eaf7e1d6-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git170925.064740.d4e4aadf-1
- Update to latest snapshot.

* Tue Aug 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git170815.003440.d85c4f99-1
- Update to latest snapshot.

* Sun Aug 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git170812.233712.f378ba1f-1
- Update to latest snapshot.

* Fri Aug 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git170811.095450.66be53e1-1
- Update to latest snapshot.

* Fri Jul 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git170728.013904.4953b380-1
- Update to version 2.3.0.

* Fri Jul 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev801-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev797-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev796-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev795-1
- Update to latest snapshot.

* Sun May 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev788-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev783-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev782-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev781-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev780-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev777-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev775-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev772-1
- Update to latest snapshot.

* Fri Apr 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev770-1
- Update to latest snapshot.

* Thu Apr 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev767-2
- Adapt to upstream changes.

* Wed Apr 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev767-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev763-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev762-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev761-1
- Update to latest snapshot.

* Thu Mar 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev760-1
- Update to latest snapshot.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev759-1
- Update to latest snapshot.

* Sun Mar 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev758-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev757-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev756-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev755-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev754-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev753-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev752-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev751-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev750-1
- Update to latest snapshot.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev749-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev748-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev747-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev746-1
- Update to latest snapshot.

* Wed Feb 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev745-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev743-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev742-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev741-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev740-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev739-1
- Update to latest snapshot.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev737-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev736-1
- Update to latest snapshot.

* Thu Jan 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev735-1
- Update to latest snapshot.

* Fri Jan 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev734-1
- Update to version 2.2.0.

* Thu Jan 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev733-1
- Update to version 2.2.0.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev732-1
- Update to version 2.2.0.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev731-1
- Update to version 2.2.0.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev730-1
- Update to version 2.2.0.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev729-1
- Update to version 2.2.0.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev728-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev727-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev726-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev725-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev724-2
- Enable libunity support.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev724-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev723-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev722-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev720-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev719-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev718-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev717-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev716-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev715-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev714-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev713-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+rev712-1
- Update to version 2.2.0.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev712-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev711-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev710-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev709-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev708-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev707-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev706-1
- Update to latest snapshot.

* Tue Nov 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev705-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev704-1
- Update to latest snapshot.

* Fri Nov 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev703-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev702-1
- Update to latest snapshot.

* Fri Nov 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev701-1
- Update to latest snapshot.

* Tue Nov 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev700-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev699-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev698-1
- Update to latest snapshot.

* Sat Nov 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev697-2
- Adapt spec to changed .desktop file name.

* Sat Nov 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev697-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev695-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev693-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev692-1
- Update to latest snapshot.

* Wed Nov 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev690-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev689-2
- Plug directories are now included upstream.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev689-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev686-1
- Update to latest snapshot.

* Thu Oct 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev685-1
- Update to latest snapshot.

* Wed Oct 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev684-1
- Update to latest snapshot.

* Tue Oct 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev683-1
- Update to latest snapshot.

* Tue Oct 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev682-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev681-2
- Add missing BR: libappstream-glib.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+rev681-1
- Update to version 2.1.0.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev681-2
- Spec file cosmetics.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev681-1
- Update to latest snapshot.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev680-1
- Update to latest snapshot.

* Mon Sep 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev679-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev678-1
- Update to latest snapshot.

* Fri Sep 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev677-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev676-1
- Update to latest snapshot.

* Thu Aug 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev675-1
- Update to latest snapshot.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev674-1
- Update to latest snapshot.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev673-1
- Update to latest snapshot.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev672-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev671-1
- Update to version 2.1.0.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev670-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev669-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev667-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev666-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev666-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev665-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev664-3
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com>
- Add new appdata file to spec.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev664-2
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com>
- Add BR: intltool to fix build.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev664-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev663-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev656-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev655-1
- Update to latest snapshot.

* Sat Jul 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev654-1
- Update to latest snapshot.

* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev653-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev652-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev650-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev649-1
- Update to latest snapshot.

* Thu Jul 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev648-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev647-2
- Update for packaging changes.

* Sun Jun 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev639-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev638-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev637-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev636-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev635-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev633-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev632-1
- Update to latest snapshot.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev631-2
- Update for packaging changes.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev631-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev630-1
- Update to latest snapshot.

* Sat May 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev629-1
- Update to latest snapshot.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev628-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev627-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev626-1
- Update to latest snapshot.

* Sun May 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev625-1
- Update to latest snapshot.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev624-1
- Update for packaging changes.



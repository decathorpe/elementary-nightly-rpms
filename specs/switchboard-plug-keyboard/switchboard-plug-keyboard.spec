%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_name keyboard
%global plug_type hardware

%global appname io.elementary.switchboard.%{plug_name}

Name:           switchboard-plug-keyboard
Summary:        Switchboard Keyboard plug
Version:        2.3.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnomekbd)
BuildRequires:  pkgconfig(libgnomekbdui)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(xkeyboard-config)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
This plug can be used to change several keyboard settings, for example
the delay and speed of the key repetition, or the cursor blinking speed.
You can change your keyboard layout, and use multiple layouts at the
same time. Keyboard shortcuts are also part of this plug.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon Feb 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200203.170823.ffa45f9b-1
- Update to latest snapshot.

* Fri Jan 24 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200124.010805.b454d13a-1
- Update to latest snapshot.

* Wed Jan 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200122.101952.b2c1f6bf-2
- Add missing BR: xkeyboard-config.pc.

* Wed Jan 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200122.101952.b2c1f6bf-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200121.160801.04a93411-1
- Update to latest snapshot.

* Thu Jan 16 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200116.020751.36f647c7-1
- Update to latest snapshot.

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200108.130740.5a90b68d-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200106.180738.e45860fd-1
- Update to latest snapshot.

* Sun Jan 05 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200105.130739.6641dd94-1
- Update to latest snapshot.

* Fri Jan 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200103.012759.d4259864-1
- Update to latest snapshot.

* Thu Jan 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200102.184831.1a67e84c-1
- Update to latest snapshot.

* Thu Jan 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git200101.230845.0c0cdc51-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191224.220723.eb6eaae8-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191220.160937.10e62733-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191219.130725.58f77c3e-1
- Update to latest snapshot.

* Thu Dec 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191205.052510.f9162001-1
- Update to latest snapshot.

* Thu Nov 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191128.162545.69ba211b-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191125.092522.3807ff7f-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191122.032539.895c81c8-1
- Update to latest snapshot.

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191119.212511.781cf133-1
- Update to latest snapshot.

* Mon Nov 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191118.002457.b35a9d2c-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191115.204040.d0720832-1
- Update to latest snapshot.

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191108.042414.13c855f1-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191106.171552.b239cf05-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191106.163638.dedd6dc1-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191106.092413.20167fcd-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191031.233733.7ee7f440-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191031.005904.0508ab7b-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191030.234543.3d88ccb9-1
- Update to latest snapshot.

* Thu Oct 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191017.172348.34cba8b6-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191005.032323.d73a47d0-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191003.145823.1df75315-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190929.011548.ad9bf0a7-1
- Update to latest snapshot.

* Sun Sep 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190929.011544.e8815b0a-1
- Update to latest snapshot.

* Fri Sep 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190927.171543.ffff896c-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190926.222959.8364563e-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190924.201946.64b01359-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190919.183225.6ff2a156-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190919.173451.b38a1909-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190918.132336.604037f3-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190911.225615.ce3da257-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190911.132249.881a408d-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190906.152248.ca64f699-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190830.212239.ac8673d5-1
- Update to latest snapshot.

* Wed Aug 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190828.092222.7ee2fa39-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190826.201659.71160258-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190826.062227.09f300c4-1
- Update to latest snapshot.

* Sat Aug 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190824.223540.79d745c1-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190823.222229.7d9d2531-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190822.142215.bb8fb4b7-1
- Update to latest snapshot.

* Wed Aug 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190821.195757.9f903a20-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190801.055310.71282e30-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190731.234722.98e826c5-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190717.131802.ea6360b4-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190626.204516.87fc02c3-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190531.045836.eff600e5-1
- Update to latest snapshot.

* Thu May 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190530.130400.d4340d7f-1
- Update to latest snapshot.

* Sat May 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190518.191450.f9225ba6-1
- Update to latest snapshot.

* Tue Apr 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190423.184317.1a74273d-1
- Update to latest snapshot.

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190318.135125.28fa960f-1
- Update to latest snapshot.

* Wed Mar 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190306.090316.d95e9e3a-1
- Update to version 2.3.5.

* Wed Mar 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190306.090316.d95e9e3a-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190305.084135.6bf46c8e-2
- Adapt to renamed appdata file.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190305.084135.6bf46c8e-1
- Update to latest snapshot.

* Mon Mar 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190304.101000.51e76747-1
- Update to latest snapshot.

* Tue Feb 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190225.235636.12931e24-1
- Update to latest snapshot.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190222.000506.32bcc367-1
- Update to latest snapshot.

* Sat Feb 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190216.180811.97076be9-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190211.051058.23bea5b6-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190210.233241.e05fbfcd-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190209.105314.99220cfa-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190209.083111.ebb3f537-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190207.000634.d2d1a2db-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190206.160252.39a592f9-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190206.155622.f8474331-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190206.133902.1dc9bb1a-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190206.125617.3d904a75-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190206.083504.ac931254-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190206.024639.183bcadb-1
- Update to latest snapshot.

* Tue Feb 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190205.204746.d7fa82bb-1
- Update to latest snapshot.

* Sun Jan 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190127.000120.2eba427e-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190125.000135.c900ceab-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190115.000603.e3618658-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190114.132741.d4615eb6-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190114.000952.4926630e-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190109.000651.c5f2b991-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190107.000330.73be8335-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190106.143430.d35ae838-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190102.194420.59ee7f98-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190102.001031.f6d89102-1
- Update to latest snapshot.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181229.000116.9693de32-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181224.000700.8708a971-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181219.000800.0498e2ba-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181218.000117.38b99506-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181217.000452.8d774a2f-1
- Update to latest snapshot.

* Fri Dec 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181214.221019.52b3a977-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181211.160521.b68e32bd-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181206.165043.90274cd2-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181202.063659.98c4f22a-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181124.130904.05fa5c40-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181116.083911.a043c107-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181113.212024.5f04285d-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181113.184114.0b941e48-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181110.220504.af0f6a3f-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181109.230711.f1682813-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181107.141014.31984d9d-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181106.220015.9e9ebca1-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181104.143818.c33675e9-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181102.040450.8ddbb5cd-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181102.040450.8ddbb5cd-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181030.080759.2f22e3c7-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181026.150257.65435407-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181025.150942.23dc70cf-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181025.140919.80545d7d-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181025.120331.c5b013f0-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181025.110557.09f2dc0a-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181025.082358.8b8697be-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181022.041134.086a1f69-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181021.132805.4ff4d5a7-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181021.115711.5f2a3d33-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181020.025756.46cfa55a-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181018.070608.bf2c1682-1
- Update to version 2.3.4.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181018.070608.bf2c1682-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181018.001040.3ffeba61-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.194926.3efea361-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.175532.edb1679a-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.163959.e81cde7e-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.133953.5002288c-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.124455.b0ba8e47-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.100845.946a45b7-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.094421.eb902e89-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.083553.5eb7e187-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.015125.f2f4ae70-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181016.004716.d653e5cd-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181014.000334.a202ece3-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181010.165357.52a841ef-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181009.164827.53173eca-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181008.000530.9681551f-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181004.163456.e33d199e-2
- Adapt to upstream file changes.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181004.163456.e33d199e-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181003.144257.354f549e-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181003.001100.b09cf8fd-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180929.000938.5f3977a4-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180925.000235.133cdd37-1
- Update to latest snapshot.

* Sat Sep 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180922.001057.4cde04e8-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180920.103221.127df7ab-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180919.000917.3bb50537-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180918.095444.fed44481-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180907.000612.1757ad53-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180906.000920.484d6580-1
- Update to latest snapshot.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180902.075119.2eb5ba97-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180901.000843.465d246b-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180831.120059.7ca91e38-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180830.000743.467a9b44-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180829.162835.77b6d697-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180829.155512.b81d724f-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180829.094110.7370cbd5-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180829.064411.b9fd6c61-1
- Update to latest snapshot.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180828.162330.67f3a24c-1
- Update to latest snapshot.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180828.154541.76c7e459-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180821.000219.1e98b10f-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180818.134459.3c069144-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180813.000340.03cf9b02-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180813.000340.03cf9b02-1
- Update to latest snapshot.

* Mon Jul 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180723.000414.e982b2d9-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180717.000318.0de36acc-1
- Update to latest snapshot.

* Mon Jul 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180716.000401.16cb5c6a-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180709.205635.45813ee5-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180709.074935.efb63a8d-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180709.001028.dbd67a2d-1
- Update to latest snapshot.

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180708.144424.e02052b8-1
- Update to latest snapshot.

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180708.000916.532baa96-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180707.000454.931013ed-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180706.191958.71035c95-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180705.000727.3af937c1-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180704.000916.575d4bc5-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180615.001100.4008675c-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180614.085727.16ddceb4-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180613.000741.8651ffd3-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180610.001201.46726520-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180608.163932.440fc5df-1
- Update to version 0.3.3.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180608.163932.440fc5df-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180608.001232.121d9140-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180606.000917.bb2ed945-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180602.000614.7750ba27-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180601.000802.5421d654-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180531.000256.0503c961-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180530.000359.c009be7c-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180529.001232.f385e24c-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180528.062109.155df392-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180527.000542.e2fa2511-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180518.000742.17db3b95-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180517.000418.fc2b173b-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180513.090616.124d47b7-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180512.001146.ac679b2e-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180511.115800.36895d2c-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180511.000622.78632fd6-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180510.071750.1d2148cc-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180508.170516.a8af0a79-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180508.001103.d20a1583-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180507.000259.5d19bd2e-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180505.023031.8501a607-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180503.194042.6caf6c9c-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180503.171140.acc181a0-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180503.165122.5397d09e-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180429.133714.1edd7cf4-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180425.102311.38db8232-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180425.000338.6a57d892-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180421.001121.b961ffa0-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180414.122620.ea75705a-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180406.000352.ffa190eb-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180405.142849.eea2195f-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180402.000457.e58efd47-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180326.000903.9d478e53-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180324.205025.e6445b7c-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180322.000538.6522f87b-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180320.001152.e6d66746-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180319.151229.8638d1d5-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180318.000825.2e25a50f-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180317.100407.e186fe86-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180316.191630.9af40792-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180316.091050.09ee3b05-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180315.184505.e3a7960b-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180315.155900.1fac235f-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180313.025715.410d19e7-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180312.155636.fe03846b-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180312.145300.73e72838-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180311.205622.c39a5032-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180311.095446.a10811d7-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180311.000621.177ae1f4-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180310.122141.d922082e-2
- Adapt to CMake -> meson switch.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180310.122141.d922082e-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180310.002302.fb5cc9a1-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180309.185959.895cdfd1-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180309.000602.4c328529-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180306.130436.ce9a01c5-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180303.030918.626374ca-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180227.194715.52e0adce-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180227.070023.3d96eefd-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180226.201015.d9bab9b2-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180226.173626.c606b888-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180225.213219.ef02d6fa-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180225.122819.f12833dc-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180224.232100.42a1d6d3-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180224.194912.e89c83fa-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180224.175219.d33765c0-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180224.135921.4d2d1419-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180224.000418.bc2aa90d-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180223.193518.102a536e-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180223.124615.e626b25e-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180223.120137.f6051c51-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180218.110920.31efe888-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180211.000844.ac859ebd-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.000629.c12e152e-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171110.205845.234458c7-2
- Merge .spec file from fedora.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171110.205845.234458c7-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171025.121231.78ae5466-1
- Update to latest snapshot.

* Tue Oct 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171023.232349.2cc20383-1
- Update to latest snapshot.

* Sun Oct 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171022.115936.5a7f1a5e-1
- Update to latest snapshot.

* Mon Oct 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171009.044104.d9a760ea-1
- Update to latest snapshot.

* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170919.133419.4768b15d-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170915.174240.565ea57e-1
- Update to version 0.3.2.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev604-1
- Update to latest snapshot.

* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev602-1
- Update to latest snapshot.

* Thu Sep 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev599-1
- Update to latest snapshot.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev598-2
- Adapt to upstream dependency changes.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev598-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev592-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev591-1
- Update to latest snapshot.

* Tue Jun 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev586-1
- Update to latest snapshot.

* Tue Jun 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev585-1
- Update to latest snapshot.

* Thu Jun 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev583-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev582-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev580-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev543-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev530-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev529-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev528-1
- Update to latest snapshot.

* Sun Mar 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev527-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev526-2
- Add BR: pkgconfig(libxml-2.0).

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev526-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev525-1
- Update to latest snapshot.

* Sun Feb 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev524-1
- Update to latest snapshot.

* Sun Feb 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev523-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev521-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev520-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev518-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev516-1
- Update to latest snapshot.

* Fri Feb 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev515-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev514-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev513-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev512-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev510-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev509-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev508-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev503-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev501-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev500-1
- Update to latest snapshot.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev499-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev498-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev497-1
- Update to version 0.3.1.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev496-1
- Update to version 0.3.1.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev495-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev494-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev493-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev492-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev491-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev490-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev489-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev488-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev487-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+rev486-1
- Update to version 0.3.1.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev486-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev485-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev484-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev483-1
- Update to version 0.3.



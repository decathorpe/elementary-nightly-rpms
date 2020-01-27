%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type hardware
%global plug_name mouse-touchpad

%global appname io.elementary.switchboard.mouse-touchpad

Name:           switchboard-plug-mouse-touchpad
Summary:        Switchboard Mouse and Touchpad plug
Version:        2.4.0+git%{date}.%{commit}
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
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
A switchboard plug to configure the behavior of mice and touchpads.


%prep
%autosetup -p1


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
* Mon Jan 27 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git200127.200812.579ca336-1
- Update to latest snapshot.

* Sat Jan 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git200125.150830.70316ddb-1
- Update to latest snapshot.

* Thu Jan 23 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git200123.032532.7f3b8f63-1
- Update to latest snapshot.

* Wed Jan 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git200121.200123.6d3d7606-1
- Update to version 2.4.0.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200121.200123.6d3d7606-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200121.195940.5175aab7-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200121.185155.e2997112-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200121.170802.2bb23ded-1
- Update to latest snapshot.

* Sun Jan 19 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200119.130808.4ee5b575-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200115.162043.342b0c4c-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200114.235350.e46f6604-1
- Update to latest snapshot.

* Sun Jan 12 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200112.190747.2c940c96-1
- Update to latest snapshot.

* Fri Jan 10 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200110.225204.68acb761-1
- Update to latest snapshot.

* Fri Jan 10 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200110.193843.fb27de22-1
- Update to latest snapshot.

* Fri Jan 10 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200110.100010.d65ed85e-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200106.210738.e44735c7-1
- Update to latest snapshot.

* Wed Jan 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git200101.160730.9ba62bcb-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git191224.220722.08365583-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git191220.160934.37d97a04-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git191219.130722.b2ee166a-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git191218.220506.6c65f445-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git191218.220024.6eb9479c-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git191218.184524.f6a7d121-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git191218.180025.5b06a266-1
- Update to latest snapshot.

* Thu Dec 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git191205.184942.1b9440eb-1
- Update to latest snapshot.

* Tue Dec 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.1+git191201.215425.e6a35084-1
- Update to version 2.3.1.

* Sun Dec 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191201.215425.e6a35084-1
- Update to latest snapshot.

* Sat Nov 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191130.172301.2eaa0250-1
- Update to latest snapshot.

* Fri Nov 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191129.182345.4b9e6b07-1
- Update to latest snapshot.

* Fri Nov 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191129.002459.af73ffc8-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191127.202529.7a9b5de8-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191125.102507.277229d2-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191122.032525.cb28971c-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191117.202504.4d6a25dd-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git191116.172454.34db2bfe-1
- Update to version 2.3.0.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191116.172454.34db2bfe-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191115.224024.16163088-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191111.122453.6e953f7b-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191109.152449.e3033faa-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191107.182518.c2162765-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191105.165040.b9add639-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191105.132410.b25991b6-1
- Update to latest snapshot.

* Mon Oct 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191021.180354.4a07b2b4-1
- Update to latest snapshot.

* Fri Oct 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191016.223929.33c816fc-2
- Remove removed icon file.

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191016.223929.33c816fc-1
- Update to latest snapshot.

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191016.163302.ecb82534-1
- Update to latest snapshot.

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191016.153429.d00bef5a-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191009.172334.15642313-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191007.152408.9a1c699f-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191005.092327.f171e7be-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191003.145942.f6285155-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191002.203914.a80277aa-1
- Update to latest snapshot.

* Sat Sep 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190925.232656.6ec4bb01-2
- Add new icon files.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190925.232656.6ec4bb01-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190925.201749.5928c23e-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190925.171835.066fa0ca-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190925.155900.8287d41e-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190924.194252.2a6b1134-1
- Update to latest snapshot.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190923.164823.8e51e77a-1
- Update to latest snapshot.

* Sun Sep 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190922.192314.b1b9c7bb-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190920.172308.2a33dabe-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190919.180043.37cf4c28-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190919.165247.1dd1b686-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190918.132306.86d90420-1
- Update to latest snapshot.

* Sat Sep 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190913.234851.382e2a38-1
- Update to latest snapshot.

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190912.142254.5d190f73-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190907.202245.b15afd91-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190906.152250.8d3fc866-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190902.202248.bf640338-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190830.212241.d16b865e-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190829.172246.d07d8dd3-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190826.052222.3a6713d2-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190823.222226.66846501-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190731.234529.7476c5ce-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190717.133452.5d667101-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190626.204527.ec908c64-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190531.044812.b1d55b84-1
- Update to latest snapshot.

* Sun May 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190516.091459.d9ffde1b-1
- Update to latest snapshot.

* Mon Apr 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190422.185919.f90dc10b-1
- Update to latest snapshot.

* Tue Apr 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190416.215349.bfce405f-1
- Update to latest snapshot.

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190412.182532.a823ad9c-1
- Update to version 2.2.0.

* Fri Apr 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190412.182532.a823ad9c-1
- Update to latest snapshot.

* Thu Apr 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190411.034758.2a21b7d4-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190408.195320.8eb26533-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190405.115220.33839015-1
- Update to latest snapshot.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190330.225209.655a923b-1
- Update to latest snapshot.

* Fri Mar 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190329.025243.178d92c7-1
- Update to latest snapshot.

* Tue Mar 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190326.170417.1c257d0f-1
- Update to latest snapshot.

* Sat Mar 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190309.182700.e552eb12-1
- Update to latest snapshot.

* Sun Mar 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190303.122647.736e703d-1
- Update to latest snapshot.

* Thu Feb 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190228.043923.76c934fd-1
- Update to latest snapshot.

* Tue Feb 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190225.232801.0f4cb36d-1
- Update to latest snapshot.

* Sun Feb 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190224.000203.63b498b8-1
- Update to latest snapshot.

* Sun Feb 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190223.231700.d8d4ba76-1
- Update to latest snapshot.

* Sat Feb 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190223.152626.cb5d767d-1
- Update to latest snapshot.

* Sat Feb 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190223.101203.714ec204-1
- Update to latest snapshot.

* Sat Feb 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190223.025754.80e54409-1
- Update to latest snapshot.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190222.150035.affe957f-1
- Update to latest snapshot.

* Mon Feb 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190218.191717.c969483e-1
- Update to latest snapshot.

* Mon Feb 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190218.145044.87a8f253-1
- Update to latest snapshot.

* Mon Feb 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190218.114319.c8fa68da-1
- Update to latest snapshot.

* Mon Feb 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190218.000358.65522857-1
- Update to latest snapshot.

* Sun Feb 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190217.145431.3f79ba8a-1
- Update to latest snapshot.

* Sun Feb 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190217.040019.dd7f2710-1
- Update to latest snapshot.

* Sun Feb 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190217.021403.7b4fedbd-1
- Update to latest snapshot.

* Sat Feb 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190216.185914.4cb0dae1-1
- Update to latest snapshot.

* Sat Feb 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190216.103106.006aab22-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190212.000659.bd56a25d-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190211.160833.90d398f9-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190211.144707.e7b96008-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190211.062153.9e03cd29-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190211.054933.45271e4d-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190211.001055.87c64264-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190210.220453.51ec9e70-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190210.215110.15745a03-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190209.105110.62a2c0ae-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190125.000139.efe7ad19-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190115.000614.ef4e4623-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190114.131111.8e38f321-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190114.001000.f22acf9e-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190110.000720.3639f436-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190107.000334.e66157f3-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190106.114025.c65cccb0-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190103.000439.88fbdee3-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190102.205315.3bfba272-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190102.001035.de3139d1-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181219.000811.e232f177-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181217.150720.edfbdec0-1
- Update to latest snapshot.

* Fri Dec 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181214.221008.bde451cf-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181213.143144.960265d2-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181212.220402.25408ee4-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181211.070808.095adcf4-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181207.053729.4b333346-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181205.235300.75238d71-2
- Adapt to upstream file changes.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181205.235300.75238d71-1
- Update to latest snapshot.

* Wed Dec 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181205.194520.67569d4c-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181203.225644.0fa2a653-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181203.163734.a3bfc108-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181203.122724.a19be313-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181203.080409.298dbfdb-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181202.095559.f30de6c9-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181202.063902.7b15ae5b-1
- Update to latest snapshot.

* Sat Dec 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181201.060056.5a612efa-1
- Update to latest snapshot.

* Sat Dec 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181201.011827.fa0d9587-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181130.201356.6a949f08-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181130.194413.1a3d016d-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181130.065514.7742b848-1
- Update to latest snapshot.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181129.091546.7bad22f0-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181128.142814.c790e3ce-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181128.125425.dd6dfe1f-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181128.101151.dfe02bc2-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181128.001136.6879b46e-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181127.232052.a730c23f-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181127.210913.9dbd2ff2-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181127.175624.98ad7e90-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181127.165101.b5a19ec9-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181127.102606.94e96d1c-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181127.064027.f3fbc2fc-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181127.030900.8e965548-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181126.235616.cf982ed9-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181126.220008.f545d126-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181126.205902.96c0e5e0-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181126.200031.f21fb3f4-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181126.172439.6c0e8247-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181124.130853.2085727e-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181120.090729.763962be-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181116.081558.786bbf6b-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181107.000948.f3b093fa-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181106.213609.a8a95816-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181105.234408.1945dc97-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181101.100739.a20ffcfd-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181101.100739.a20ffcfd-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181029.030039.dfd6bed3-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181025.071553.29256cc0-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181024.221024.dfc7415d-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181023.231001.6227a39f-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181021.155448.ff1f583e-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181020.030025.eedf1335-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181018.203429.4833b591-1
- Update to version 2.1.4.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181018.203429.4833b591-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181018.065828.cf654af9-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181017.000734.9e28d483-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.195140.11da7a7e-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.181206.ad511220-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.164105.74e7f54f-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.134314.108495af-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.124905.c0639f22-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.102857.c38366cb-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.091946.2e2a9a86-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.005750.c1a6699e-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181015.215110.cb4d0eef-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181013.220355.c24b0757-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181009.154142.2f8cb6eb-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181007.000955.618ca98a-1
- Update to latest snapshot.

* Sat Oct 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181006.034139.da18ba44-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180919.000922.84eb7078-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180906.043521.42e46854-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180901.000851.b00a4f06-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180829.162527.121f1e7d-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180825.000317.9860d543-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180823.185915.c54e7468-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180813.000347.07691471-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180813.000347.07691471-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180722.120635.cec99ed1-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180722.000349.d1848581-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180718.000623.f614e4a7-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180709.205729.48586e39-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180702.000706.126b4b14-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180615.001109.c0b6fb68-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180614.000911.3ed8e375-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180613.000746.21967c73-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180609.125902.ce56e6f6-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180607.140200.b2574562-1
- Update to version 0.1.3.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180607.140200.b2574562-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180604.000933.2aca6764-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180603.070506.5d272b74-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180601.000809.24ca3acc-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180531.000305.ece22c72-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180530.113541.37f98533-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180530.000409.86227ae0-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180527.190937.01a8ff68-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180527.000547.c54bd491-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180520.000458.bf48daa7-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180512.001155.20217fea-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180511.113739.a5c6e91c-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180511.000627.e356424b-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180508.171058.3de59574-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180507.000308.c324634d-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180504.000625.232072ac-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180501.165916.abcbe31e-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180429.115401.3372c970-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180426.000340.725807bc-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180425.103212.d5f14cf9-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180421.001127.a343f429-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180416.204812.d35b2931-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180414.123403.999c27b1-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180405.143536.1cd0a0c2-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180403.142515.2111a8d4-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180328.195954.b2b65ee1-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180327.000229.b0377d7f-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180326.102640.505e2e7c-2
- Adapt to CMake -> meson switch.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180326.102640.505e2e7c-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180322.134135.567df840-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180314.231543.5157d3c5-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180309.000608.2eed8d9a-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180303.000250.89f4699c-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180218.191214.ff9b15dd-2
- Adapt patch to upstream changes.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180218.191214.ff9b15dd-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180217.101024.fbbc5743-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180211.000850.8c6d0019-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180109.001810.bc910226-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.015919.d8633d55-2
- Merge .spec file from fedora.

* Sat Nov 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.015919.d8633d55-1
- Update to latest snapshot.

* Wed Nov 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171115.173431.25cff6b6-1
- Update to latest snapshot.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171112.174349.189cbb64-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170925.083359.6fbb3e6d-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170707.025535.d81c25aa-1
- Update to version 0.1.2.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev191-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev190-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev187-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev186-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev166-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev165-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev164-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev163-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev162-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev161-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev160-1
- Update to latest snapshot.

* Fri Feb 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev159-1
- Update to latest snapshot.

* Thu Feb 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev158-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev157-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev156-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev155-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev154-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev153-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev152-1
- Update to latest snapshot.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev151-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev149-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev148-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev147-1
- Update to version 0.1.1.2.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev146-1
- Update to version 0.1.1.2.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev145-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev144-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev143-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev142-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev141-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev140-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev139-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev138-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev136-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev135-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev134-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev133-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev132-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev131-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev130-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev129-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev128-3
- Fix patch.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev128-2
- Port patch to new upstream changes.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev128-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev127-1
- Update to latest snapshot.

* Wed Nov 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev126-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev125-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev124-1
- Update to latest snapshot.

* Wed Nov 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev123-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev122-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev121-1
- Update to version 0.1.1.2.

* Wed Oct 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev118-2
- Adapt patch to upstream changes.

* Mon Oct 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev118-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev117-1
- Update to latest snapshot.

* Thu Oct 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev116-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev114-1
- Update to latest snapshot.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev113-1
- Update to version 0.1.1.1.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev113-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev112-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev110-1
- Update to latest snapshot.

* Thu Sep 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev107-1
- Update to latest snapshot.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-4
- Update for packaging changes.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com>
- Fix applying patch.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-3
- Update for packaging changes.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com>
- Fix applying patch.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-2
- Update for packaging changes.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com>
- Add patch to fix SEGFAULT (wrong gsettings path).

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev96-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev95-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev94-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev93-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev92-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev92-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev91-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev90-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev88-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev87-1
- Update to latest snapshot.

* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev83-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev82-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev81-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev78-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev77-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev75-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev74-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev73-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev72-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev71-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev70-2
- Update for packaging changes.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev65-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev64-1
- Update to latest snapshot.

* Sun Jun 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev63-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev60-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev59-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev58-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev57-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-4
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-3
- Update for packaging changes.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev56-1
- Initial package.



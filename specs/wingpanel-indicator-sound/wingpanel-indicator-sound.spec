%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global appname io.elementary.wingpanel.sound

Name:           wingpanel-indicator-sound
Summary:        Sound Indicator for wingpanel
Version:        2.1.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel%{?_isa}


%description
A sound indicator for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang sound-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f sound-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libsound.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.sound.gschema.xml

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Mar 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200329.193053.44f8308a-1
- Update to latest snapshot.

* Thu Mar 26 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200326.220945.425b228a-1
- Update to latest snapshot.

* Thu Mar 19 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200319.200935.697aa569-1
- Update to latest snapshot.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200303.135322.bac092f2-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200301.140904.862beefc-1
- Update to latest snapshot.

* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200222.190853.77553ccb-1
- Update to latest snapshot.

* Sat Feb 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200201.020816.aba0018e-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200121.160759.9517e866-1
- Update to latest snapshot.

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200108.000743.0669f9e9-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200106.190736.71b164d1-1
- Update to latest snapshot.

* Sun Jan 05 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200105.170741.862f2f56-1
- Update to latest snapshot.

* Fri Jan 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git200103.210731.62888816-1
- Update to latest snapshot.

* Wed Dec 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191225.151714.fb37e453-1
- Update to latest snapshot.

* Sat Dec 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191221.010711.78858d25-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191219.130709.40404cbd-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191217.225043.cad23fea-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191217.191725.476ddec7-1
- Update to latest snapshot.

* Sun Dec 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191215.202922.f7910b13-1
- Update to latest snapshot.

* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191213.173125.45399955-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191125.165525.002003d8-1
- Update to version 2.1.4.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191125.165525.002003d8-1
- Update to latest snapshot.

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191119.212428.51f80643-1
- Update to latest snapshot.

* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191114.152422.f4bd93c1-1
- Update to latest snapshot.

* Tue Nov 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191112.182416.b17f9a2c-1
- Update to latest snapshot.

* Sun Nov 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191110.202413.62482847-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191109.122410.44a82b90-1
- Update to latest snapshot.

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191107.213331.b8cca17e-2
- Package and validate appdata file.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191107.213331.b8cca17e-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191106.174625.92829f2a-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191106.164700.58440777-1
- Update to latest snapshot.

* Mon Oct 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191021.180117.3357812b-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191003.152850.e3ef74e5-1
- Update to latest snapshot.

* Sun Sep 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190929.015610.057c808b-1
- Update to latest snapshot.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190923.163902.e1ac8807-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190920.012524.06f3d7b5-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190918.143246.f5e93a86-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190827.172229.36f99444-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190827.165021.0e1e8883-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190626.204735.3f569588-1
- Update to latest snapshot.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190409.225336.4b2319b2-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190312.112139.4eb4dd01-1
- Update to latest snapshot.

* Mon Mar 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190311.124234.96e48985-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190307.070756.8d12b10c-1
- Update to version 2.1.3.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190307.070756.8d12b10c-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190305.093455.5b0a7ae4-1
- Update to latest snapshot.

* Wed Feb 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190213.052642.605d6d3e-1
- Update to latest snapshot.

* Wed Feb 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190213.043930.9113a51d-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190210.220109.022d06f4-1
- Update to latest snapshot.

* Fri Feb 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190207.231138.833d86bb-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190207.155757.35a66866-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190207.131832.2e06c1ca-1
- Update to latest snapshot.

* Wed Jan 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190130.114139.cbf0c9dd-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190114.001153.f159c87e-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181219.120005.eb745e68-1
- Update to version 2.1.2.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181219.120005.eb745e68-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181206.060040.98dbbe42-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181202.053723.339c1af0-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181121.144058.db99ef2e-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181115.184110.00f18d05-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181109.111621.16396235-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181104.224345.260a9126-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181101.000335.6fdf4c67-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181101.000335.6fdf4c67-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181030.080932.51f15a1c-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181028.191101.3990f5dc-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181001.114107.74b7425e-1
- Update to version 2.1.1.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git181001.114107.74b7425e-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180830.000921.f80fa337-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180808.104835.c74ff97f-2
- Occasional mass rebuild.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180808.104835.c74ff97f-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180802.201435.be3c50e3-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180802.170941.074de478-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180724.142641.136d7143-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180724.031003.66598dd2-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180719.000811.cdac4c3d-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180716.165339.d1cc8e34-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180627.165748.672c526b-1
- Update to version 2.1.0.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180627.165748.672c526b-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180615.001322.47376e33-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180610.001417.9b6ccfe6-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180609.114848.99a6c9a0-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180607.091029.3f8484ba-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180606.153529.6c693a6d-2
- Adapt to upstream file changes.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180606.153529.6c693a6d-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180606.143247.495696cb-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180531.080841.54caffad-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180529.115818.a4f06448-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180410.170402.a5fb639f-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180410.161224.283112f0-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180405.002012.5cd33075-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180404.222909.b67f5005-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180330.003404.181c9396-2
- Adapt to CMake -> meson switch.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180330.003404.181c9396-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180325.001141.1a97e8d7-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180320.001429.ef4f1fbc-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180318.004917.7265f693-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180213.170713.50d031aa-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180213.162224.190f18f7-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180213.023227.691542b5-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180209.001231.88009646-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180103.001605.5631feac-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git180103.001605.5631feac-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git171219.003558.edf7c0e8-1
- Update to latest snapshot.

* Thu Nov 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git171102.164358.ac5d8dba-1
- Update to latest snapshot.

* Sun Oct 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git171008.022538.d46474d4-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git170709.011937.994dc582-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git170703.192647.7b574b0d-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git170617.151951.664ad1a6-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git170530.192414.5bcf64af-1
- Update to latest snapshot.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git170515.192144.324cefbe-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.5+git170502.211051.0cfdd22a-1
- Update to version 2.0.5.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git170502.211051.0cfdd22a-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git170501.203903.9feef997-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git170427.124955.b4ec8a16-1
- Update to version 2.0.4.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev161-1
- Update to latest snapshot.

* Fri Apr 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev160-1
- Update to latest snapshot.

* Sun Apr 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev159-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev155-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev154-1
- Update to latest snapshot.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev153-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev152-1
- Update to latest snapshot.

* Sun Mar 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev151-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev150-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev149-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev148-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev147-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev146-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev145-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev144-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev143-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev142-1
- Update to version 2.0.3.

* Thu Jan 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev141-1
- Update to version 2.0.3.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev140-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev139-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev138-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev137-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev136-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev135-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev134-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev133-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev132-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev131-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev130-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev129-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev128-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev127-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev126-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev125-1
- Update to version 2.0.3.

* Mon Oct 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev123-1
- Update to latest snapshot.

* Sun Oct 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev121-1
- Update to latest snapshot.

* Thu Oct 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev120-1
- Update to latest snapshot.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev119-1
- Update to version 2.0.2.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev119-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev118-2
- Spec file cleanups.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev118-1
- Update to latest snapshot.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev117-1
- Update to version 2.0.1.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev116-1
- Update to version 2.0.1.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev115-1
- Update to latest snapshot.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev114-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev113-1
- Update to latest snapshot.

* Sat Sep 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev112-1
- Update to latest snapshot.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev111-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev110-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev109-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev108-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev108-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev107-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev106-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev105-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev103-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev102-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev101-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev100-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev98-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev97-1
- Update to latest snapshot.

* Fri Jul 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev96-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev95-2
- Update for packaging changes.

* Sun Jun 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev90-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev89-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev88-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev87-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev87-2
- Update for packaging changes.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev87-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev86-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-1
- Initial package.



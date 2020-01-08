%global srcname icons

%global appname io.elementary.icons

Name:           elementary-icon-theme
Summary:        Icons from the Elementary Project
Version:        5.1.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson


%description
This is an icon theme designed to be smooth, sexy, clear, and efficient.

%package        gimp-palette
Summary:        Icons from the Elementary Project (GIMP palette)
Requires:       %{name} = %{version}-%{release}
Requires:       gimp

%description    gimp-palette
This is an icon theme designed to be smooth, sexy, clear, and efficient.

This package contains a palette file for the GIMP.


%package        inkscape-palette
Summary:        Icons from the Elementary Project (inkscape palette)
Requires:       %{name} = %{version}-%{release}
Requires:       inkscape

%description    inkscape-palette
This is an icon theme designed to be smooth, sexy, clear, and efficient.

This package contains a palette file for inkscape.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

# Clean up weird stuff
rm %{buildroot}/.VolumeIcon.png
rm %{buildroot}/.VolumeIcon.icns

# Create icon cache file
touch %{buildroot}/%{_datadir}/icons/elementary/icon-theme.cache


%transfiletriggerin -- %{_datadir}/icons/elementary
gtk-update-icon-cache --force %{_datadir}/icons/elementary &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/elementary
gtk-update-icon-cache --force %{_datadir}/icons/elementary &>/dev/null || :


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml || :


%files
%doc README.md
%license COPYING

%dir %{_datadir}/icons/elementary
%ghost %{_datadir}/icons/elementary/icon-theme.cache

%{_datadir}/icons/elementary/*/
%{_datadir}/icons/elementary/*@2x
%{_datadir}/icons/elementary/*@3x

%{_datadir}/icons/elementary/cursor.theme
%{_datadir}/icons/elementary/index.theme

%{_datadir}/metainfo/%{appname}.appdata.xml

%files gimp-palette
%{_datadir}/gimp/2.0/palettes/elementary.gpl

%files inkscape-palette
%{_datadir}/inkscape/palettes/elementary.gpl


%changelog
* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git200107.232024.309b4ae0-1
- Update to latest snapshot.

* Tue Jan 07 2020 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git200107.201755.2369c8c8-1
- Update to latest snapshot.

* Tue Jan 07 2020 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git200107.194355.58ec0722-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git200106.180554.8d11ef4f-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git200106.173514.9abd3008-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git200105.231250.a3036323-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git191121.191753.1d0a04b4-1
- Update to latest snapshot.

* Mon Nov 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git191118.212102.233baa49-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git191101.170755.a5537e63-3
- Package and verify appdata file.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git191101.170755.a5537e63-2
- Add missing BR: gettext.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git191101.170755.a5537e63-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git191101.043351.a8215b94-1
- Update to version 5.1.0.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191101.043351.a8215b94-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191031.225407.4b324554-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191031.214403.14a3de28-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191030.192413.4f80dc2c-1
- Update to latest snapshot.

* Thu Oct 24 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191023.235343.20b5edd0-1
- Update to latest snapshot.

* Thu Oct 10 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191009.231733.5f4c6b3d-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191009.174209.d5610878-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git191009.152927.a076dce3-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190919.182824.9cb0837c-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190823.230003.5ac788c8-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190822.033452.88f3774e-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190815.153011.95c943ee-1
- Update to latest snapshot.

* Fri Jul 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git190712.141954.e4a131ff-1
- Update to version 5.0.4.

* Fri Jul 12 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190712.141954.e4a131ff-1
- Update to latest snapshot.

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190703.192850.7a975634-1
- Update to latest snapshot.

* Tue Jun 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190611.190202.75c26c6e-1
- Update to latest snapshot.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190604.144208.65e6d6cf-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190531.045620.eb1d92f5-1
- Update to latest snapshot.

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190413.234741.52f74cf2-1
- Update to latest snapshot.

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190413.172325.b5c012af-1
- Update to latest snapshot.

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190412.234514.feb95336-1
- Update to latest snapshot.

* Fri Apr 12 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190412.184453.fb9d7423-1
- Update to latest snapshot.

* Mon Mar 25 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190325.221031.294a2c0b-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190307.225401.8333483b-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190305.044859.2fbb88e1-1
- Update to latest snapshot.

* Sat Mar 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190301.232351.a4c84090-1
- Update to latest snapshot.

* Fri Mar 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190301.224654.621ec3e6-1
- Update to latest snapshot.

* Wed Feb 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git190211.213822.a73315c4-1
- Update to version 5.0.3.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190211.213822.a73315c4-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190210.225537.fcf9beeb-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190210.021819.bc8b3350-1
- Update to latest snapshot.

* Fri Feb 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190201.002849.d9fe8bc7-1
- Update to latest snapshot.

* Thu Jan 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190131.195221.e034aca7-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190125.031043.c5b548b0-1
- Update to latest snapshot.

* Thu Jan 24 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190124.183705.e1faa69f-1
- Update to latest snapshot.

* Thu Jan 24 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190123.235404.e19f6dce-1
- Update to latest snapshot.

* Sun Jan 20 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190120.181812.2455290b-1
- Update to latest snapshot.

* Sat Jan 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190119.180607.26e98b33-1
- Update to latest snapshot.

* Sat Jan 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190118.235636.39529103-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190111.173449.208220cd-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190111.004837.d9937d3b-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git190109.191258.17647bf2-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git181229.033312.8295109a-1
- Update to version 5.0.2.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git181229.033312.8295109a-1
- Update to latest snapshot.

* Thu Dec 27 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git181227.180031.593be687-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git181220.170315.c2ee034f-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git181206.165316.2d234a91-1
- Update to version 5.0.1.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181206.165316.2d234a91-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181206.155417.47a877a9-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181204.172515.653189f8-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181204.165050.2264b023-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181130.175531.51ba48fc-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181115.004050.f7fdebd6-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181107.215141.00df0e80-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181105.194726.9bdda2c6-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181102.202424.0fbe5acb-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181101.212213.557cde35-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181101.212213.557cde35-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181026.165836.5ad65dd6-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181025.195440.8253ea2a-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git181016.051818.6de088de-1
- Update to version 5.0.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181016.051818.6de088de-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181015.202622.d55ff860-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181015.173336.cdbeca7e-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181014.154930.c768f69b-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181012.210449.a40627ee-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181011.231157.876097de-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181011.133957.bc7d246e-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181003.202443.8afc3260-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181003.164202.78e8a686-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181002.215735.309e54a6-1
- Update to latest snapshot.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git181001.223437.1d23b93d-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180927.205616.27c45b54-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180926.185523.56e639a0-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180924.175000.03d5e3b9-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180924.160439.3889811e-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180924.145946.d1cb2ce4-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180918.183121.bc9ae7e5-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180917.165303.93f119d0-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180911.184031.3ac4f807-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180908.175117.95571d65-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180908.054054.ba7712a4-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180907.171521.e8495034-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180906.224845.9bef60c9-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180906.183706.71067813-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180831.232305.60e5c906-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180831.215024.7d14e25e-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180824.212731.a31e99aa-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180822.164805.04afc98d-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180816.025856.ee6a3fc5-2
- Occasional mass rebuild.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180816.025856.ee6a3fc5-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180815.162418.acc95631-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180814.225347.b1fa0e20-1
- Update to latest snapshot.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180813.025327.22f1eccf-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180803.153510.58e86849-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180802.015859.c393935e-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180730.182513.f9ec67ab-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180720.163551.77706ef6-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180719.222720.65cd2288-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180708.231119.f315b284-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180621.232430.d8a8d41e-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180614.160230.998c963b-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180612.031320.c8054634-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180607.153040.fafd94a7-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180604.000648.ff2c231e-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180601.180302.2cea0ebd-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180529.235312.15976fc8-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180527.021028.86f9d498-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180521.021749.4cdca93d-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180518.074441.07c948a9-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180517.190909.d7d8fc81-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180517.184941.856214d0-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180517.174121.fe4da1f7-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180517.030839.ccf1d674-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180516.215510.077d8cf6-2
- Adapt to upstream file changes (GIMP and inkscape palette files).

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180516.215510.077d8cf6-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180516.215510.077d8cf6-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180516.170709.daccaca2-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180516.132611.90268d68-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180516.111050.adf21c17-2
- Adapt to CMake -> meson switch.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180516.111050.adf21c17-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180516.012128.c4461e9e-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180515.154346.68f9fbc9-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180514.190357.8e9b956c-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180514.163308.99dd95d7-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180514.154810.8eb9a777-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180514.143049.1e58278e-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180514.013953.0337ef32-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180512.235105.a8a5ff22-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180511.214224.988be3cb-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180511.042113.9eb32de8-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180510.183247.64362c50-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180510.175149.5abfd621-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180510.161413.d213a945-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180510.042047.c0672a2a-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180509.012231.3377cd3a-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180501.174929.840e3fcf-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180429.174457.b7716139-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180425.181137.1fa393b7-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180424.020339.c9746037-1
- Update to latest snapshot.

* Mon Apr 23 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180423.180027.459c75be-1
- Update to latest snapshot.

* Thu Apr 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180418.234934.ba20bf50-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180416.163430.b1844a2b-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180415.182746.228381a0-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180413.005110.c048cf1b-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180407.011658.ae20e2c8-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180329.203254.d9014b6e-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180326.150021.22235cb7-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180321.001854.6e66f7b6-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180319.211306.3f2fb255-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180318.032138.18016953-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180315.222021.e6f048c8-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180314.195041.a83db7aa-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180313.200744.a7377781-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180313.031143.2591cc01-2
- Adapt to upstream file changes.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180313.031143.2591cc01-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180312.151335.f2ce749a-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180305.183205.f7452fc8-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180227.181652.0e87a5cc-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180226.175745.93516571-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180221.050244.b99c58e4-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180219.185342.c9d445e2-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180218.190435.f172e0ca-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180214.181007.468da09d-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180210.015211.c1b2131c-1
- Update to latest snapshot.

* Wed Feb 07 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180206.222211.57d1af67-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180131.142301.9391aac6-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180129.064209.f3622e15-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180129.000020.750e7410-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180127.014852.0f321f16-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180126.211435.291c9e8e-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180126.195523.8b5856be-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180126.183836.064acb94-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180126.172307.7ed6d9e9-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180126.032426.aa57e90d-1
- Update to latest snapshot.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180125.161708.24337e7f-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180124.224820.0c2a92d2-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180118.180400.8d7f12fd-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180118.175321.c1240167-1
- Update to latest snapshot.

* Wed Jan 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180117.011854.6d103e7c-1
- Update to latest snapshot.

* Wed Jan 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180116.235722.423f5e19-1
- Update to latest snapshot.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180116.183750.e7d96855-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180114.161110.d37ba2d1-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180104.200132.842f5c35-2
- Add file triggers to replace scriptlets.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180104.200132.842f5c35-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171217.012202.430d3efe-2
- Merge .spec file from fedora.

* Sun Dec 17 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171217.012202.430d3efe-1
- Update to latest snapshot.

* Mon Dec 04 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171204.174803.abee5f0d-1
- Update to latest snapshot.

* Fri Dec 01 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171130.221733.f307c80e-1
- Update to latest snapshot.

* Tue Nov 28 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171127.232552.330a640b-1
- Update to latest snapshot.

* Sat Nov 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171118.192425.17e40d31-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171117.041239.0a372227-1
- Update to latest snapshot.

* Sun Nov 05 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171105.212540.eff997c8-1
- Update to latest snapshot.

* Tue Oct 31 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171031.165154.01a6384e-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171024.202106.bc9d5b1e-1
- Update to version 4.3.1.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git171024.202106.bc9d5b1e-1
- Update to latest snapshot.

* Mon Oct 23 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git171023.175241.f00a2f1d-1
- Update to latest snapshot.

* Sun Oct 22 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git171021.200313.29f12915-1
- Update to latest snapshot.

* Tue Sep 26 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170926.163628.008fb75e-1
- Update to latest snapshot.

* Sun Sep 24 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170924.142954.4bb1abfc-1
- Update to latest snapshot.

* Thu Sep 21 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170920.201212.339182ad-1
- Update to latest snapshot.

* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170918.235930.5a2c9a69-1
- Update to latest snapshot.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170917.200704.44e643ac-1
- Update to latest snapshot.

* Wed Aug 30 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170829.210813.59c65c10-1
- Update to latest snapshot.

* Mon Aug 28 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170828.172704.13f083de-1
- Update to latest snapshot.

* Wed Aug 02 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170801.230140.4db8a471-1
- Update to latest snapshot.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170801.180037.ab2f6dd4-1
- Update to latest snapshot.

* Wed Jul 26 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170726.043211.a99da6e8-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170725.165823.846f65b9-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170725.000617.73a04048-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170724.171630.0159920a-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170723.180712.42616d9d-1
- Update to latest snapshot.

* Thu Jul 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170720.175004.9bc143c7-1
- Update to latest snapshot.

* Thu Jul 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170719.224345.b77e4bbb-1
- Update to latest snapshot.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170719.165009.88ab6509-1
- Update to version 4.2.0.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170719.165009.88ab6509-1
- Update to latest snapshot.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170719.005923.c09f5307-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170711.191425.dc5703a1-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170630.014303.36f3efa5-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170628.033332.28ab75a3-1
- Update to latest snapshot.

* Sun Jun 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170624.205141.f074ae50-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170618.021742.1b82f02e-1
- Update to latest snapshot.

* Sat Jun 17 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170617.032943.cec13040-1
- Update to latest snapshot.

* Fri Jun 16 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170616.185512.7bce970d-1
- Update to latest snapshot.

* Fri Jun 16 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170616.032948.3433c01d-1
- Update to latest snapshot.

* Thu Jun 15 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170615.182938.4680e317-1
- Update to latest snapshot.

* Wed Jun 14 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170614.201622.fffd5678-1
- Update to latest snapshot.

* Mon Jun 12 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170612.155214.ede84605-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170603.164225.de764cb8-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170530.161436.39bb46c5-1
- Update to latest snapshot.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170515.032734.b9521515-1
- Update to version 4.1.0.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170515.032734.b9521515-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170510.120627.b10695b2-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170509.114442.2b4de6ea-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170507.114259.bd97bca8-1
- Update to latest snapshot.

* Fri May 05 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170504.225855.1f24c818-1
- Update to latest snapshot.

* Thu May 04 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170504.121945.37f345e3-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170503.155115.b3aa4e2c-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170503.115336.5a241a59-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170502.134849.6e3679ff-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170501.172536.2b901ccd-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170425.165220.c27c0112-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170320.103314.77291de6-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170227.130409.6c5effa8-1
- Update to version 4.0.3.

* Sat Mar 04 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170227.130409.6c5effa8-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170202.220804.fdbcf47b-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170116.125315.83c6f271-2
- Sync spec with fedora package.

* Thu Jan 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170116.125315.83c6f271-1
- Update to version 4.0.2.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git170116.125315.83c6f271-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161221.100345.7e9575f6-1
- Update to version 4.0.1.1.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161221.100345.7e9575f6-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161218.084045.bacf93dc-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161216.191803.a6743da8-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161215.100355.c2e60822-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161214.122150.7d0c52c6-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161201.145742.c646545c-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161130.143018.f751b03b-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161025.124600.181998c1-1
- Update to version 4.0.1.1.

* Tue Oct 25 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161025.124600.181998c1-1
- Update to latest snapshot.

* Tue Oct 18 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161018.124244.8e52e9b7-1
- Update to latest snapshot.

* Wed Oct 12 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161011.215041.c95cfe62-1
- Update to latest snapshot.

* Tue Oct 11 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161011.103850.0e1a7d60-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git160920.130844.24a317fc-1
- Update to version 4.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160920.130844~24a317fc-2
- Spec file cleanups.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160920.130844~24a317fc-1
- Update to latest snapshot.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160919.212218~47f10bd5-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160911.193229~1d70ea96-1
- Update to version 4.0.1.



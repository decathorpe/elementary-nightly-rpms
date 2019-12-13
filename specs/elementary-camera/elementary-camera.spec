%global srcname camera
%global appname io.elementary.camera

Name:           elementary-camera
Summary:        Fast and beautiful camera app
Version:        1.0.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.24

BuildRequires:  /usr/bin/appstreamcli
BuildRequires:  /usr/bin/appstream-util

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)

Provides:       snap-photobooth
Obsoletes:      snap-photobooth


%description
A fast and beautiful camera app.


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
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191213.130700.7a34a04e-1
- Update to latest snapshot.

* Mon Dec 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191209.192505.39a5968b-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191204.212512.96b6559c-1
- Update to latest snapshot.

* Fri Nov 29 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191129.002445.a8410989-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191127.202443.3f22b90d-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191125.112503.7a86ec19-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191122.172503.58a683e7-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191121.001157.6344d480-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191115.210721.613d2fa8-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191106.181548.56822371-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191106.175940.4da75733-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191106.165631.193b2674-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191001.160056.97e91f76-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191001.160052.b135874c-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191001.121154.962bc644-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git191001.013457.e144cfeb-1
- Update to latest snapshot.

* Sat Sep 28 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git190924.151038.a16793d5-1
- Update to version 1.0.5.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190924.151038.a16793d5-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190920.102253.0274f365-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190919.183121.c4d1f067-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190907.182316.428803a8-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190906.173319.a5a5ebc2-1
- Update to latest snapshot.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190814.023243.7bc642e2-1
- Update to latest snapshot.

* Mon Jul 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190722.002411.2030b727-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190626.204227.0abd6bd9-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190531.044658.eac800ee-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190514.203936.93a16216-1
- Update to latest snapshot.

* Tue May 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190507.221431.11e1b897-1
- Update to latest snapshot.

* Thu Apr 25 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190425.164817.001de48b-1
- Update to latest snapshot.

* Wed Apr 24 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190424.184639.e70fc0d9-1
- Update to latest snapshot.

* Fri Apr 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190412.095319.23badaee-1
- Update to latest snapshot.

* Tue Apr 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190402.135158.99b62737-1
- Update to latest snapshot.

* Sun Mar 31 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190331.225158.333b39c1-1
- Update to latest snapshot.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.4+git190327.203204.0df5320f-1
- Update to version 1.0.4.

* Wed Mar 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git190327.203204.0df5320f-1
- Update to latest snapshot.

* Wed Mar 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git190327.082212.90e6cd62-1
- Update to latest snapshot.

* Sat Mar 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git190316.212659.0884e280-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git190312.163458.069b1648-1
- Update to latest snapshot.

* Mon Mar 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git190311.200834.36a41df6-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git190212.160341.9084f0c1-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git190212.000631.d32b1b6a-1
- Update to latest snapshot.

* Sat Jan 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git190126.070029.9c0bc480-1
- Update to latest snapshot.

* Thu Jan 24 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3+git190124.065257.7bd10839-1
- Update to version 1.0.3.

* Thu Jan 24 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git190124.065257.7bd10839-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git190115.000526.622d3d1b-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git190114.000815.7a34695f-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git190109.115121.25934ed9-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git190108.000043.816a4c35-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git190103.220552.df33c06a-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git190102.180753.cc80db9b-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181211.064516.168aaa49-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181211.043744.9b9bfe16-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181211.022423.4ab8d352-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181211.000520.d545d569-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181210.205627.919c0479-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181119.000657.9ec5a35e-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181103.225846.ce977d92-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181103.000731.d07b8bb7-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181101.083812.9c05803d-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181101.083812.9c05803d-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181030.000431.303e3119-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181029.000938.df06e9ac-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181025.075128.a846029f-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181024.000743.b0e1ca22-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181020.001017.d0342921-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181019.061334.f7cac3bc-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181019.000725.8a5dca3e-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181018.115546.18a3d5ac-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.2+git181015.205836.e530212c-1
- Update to version 1.0.2.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181015.205836.e530212c-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181015.132939.c1521556-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181012.000444.5c21add1-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181008.000406.a81eb133-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181007.023619.459ba752-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181005.000759.65562711-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git181004.093311.72173d08-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180928.185651.0c7c583b-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180924.000453.00002c6a-1
- Update to latest snapshot.

* Sun Sep 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180923.023706.d81e15bc-1
- Update to latest snapshot.

* Sun Sep 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180916.000832.5af26ca2-1
- Update to latest snapshot.

* Thu Sep 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180913.000210.137923c0-1
- Update to latest snapshot.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180912.002559.b0c54a03-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180907.000547.19c14b73-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180906.022744.93cfdf0a-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180905.000929.6966fb20-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180831.115422.ad93bc01-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180830.153101.0c77e0ef-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180830.000645.11cae7ea-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180829.034021.b52708a9-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180826.000401.e74a5326-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180822.000835.038cd195-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180819.000839.71e98070-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180818.113251.9b4f277e-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180813.000243.b9a992a7-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180813.000243.b9a992a7-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180812.111219.e23cf6e4-1
- Update to latest snapshot.

* Sat Aug 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180811.000919.9a8f0ee7-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180803.000344.ea6721ce-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180730.000713.68fd4f8e-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180724.030601.acb2c4f7-1
- Update to latest snapshot.

* Mon Jul 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180723.201433.376b39d2-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180722.000321.03504378-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180721.183048.2b40ce5e-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1+git180720.182234.0764bc2a-1
- Update to version 1.0.1.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180720.182234.0764bc2a-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180719.000721.ce2bab70-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180718.175459.314d876c-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180718.000536.4322e143-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180716.204108.39bd8075-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180713.181246.62dc84c2-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180711.100825.54bb88ba-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180710.222501.7e6d44ca-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180710.152439.2f0367a4-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180710.092116.e139c5c4-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180710.000320.fb14c9af-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180709.195831.3a6d7c24-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180709.123923.7a6acecd-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180709.103121.fb1d1610-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180703.190008.0035a1e2-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180613.000643.bf896f61-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180612.113946.722aadbd-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180612.064056.1d98733c-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0+git180610.001058.be6c6af5-1
- Update to version 1.0.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180610.001058.be6c6af5-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180609.145039.7a082d5d-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180606.115631.2b77e38f-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180606.000753.6016f021-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180605.085423.c37c8e27-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180603.061218.4b39ab34-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180602.184954.92ca85c3-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180602.000427.7d65e743-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180601.143941.310d24e3-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.175159.a5a74472-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.163017.d056e8a6-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.154652.e56f2ce9-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.061746.d3950773-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180529.235843.dbce6564-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180529.133554.dd192bde-2
- Adapt to upstream file changes.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180529.133554.dd192bde-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180528.072615.3dbfecdc-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180527.000438.a42769ed-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180525.195708.927d1c47-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180513.001054.a1a701be-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180512.001051.c338a167-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180420.001111.7502d749-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180324.152420.ed76e8ab-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180223.210831.d0fef5ff-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180205.001051.c1aebde1-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180120.193909.9f6838a3-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180109.120659.3b8fb5ff-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171010.092010.3494a051-3
- Clean up .spec file.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171010.092010.3494a051-2
- Adapt to upstream file changes.

* Tue Oct 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171010.092010.3494a051-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170925.094829.b4e015e7-1
- Update to latest snapshot.

* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170704.192116.7bb3dae9-1
- Update to version 0.3.0.1.



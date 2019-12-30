%global srcname mail
%global appname io.elementary.mail

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-mail
Summary:        Mail app designed for elementary
Version:        1.0.8+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(camel-1.2)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.0)

Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang pantheon-mail


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f pantheon-mail.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon Dec 30 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git191230.203112.f5b239c3-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git191226.193601.26dd00b5-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git191220.165943.094c1981-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git191117.202512.b097b1a0-1
- Update to latest snapshot.

* Sun Oct 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git191027.152416.970933d6-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git191008.223819.a9c5a7af-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git191008.215010.40b10a1d-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git191003.164914.78e61d72-1
- Update to latest snapshot.

* Sun Sep 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190922.172333.7c39061e-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190920.182332.029047a0-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190919.183044.f414f34e-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190916.162327.f29d9a0a-1
- Update to latest snapshot.

* Sun Sep 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190915.122314.b26bf8da-1
- Update to latest snapshot.

* Sat Sep 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190914.092315.187c2576-1
- Update to latest snapshot.

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190912.192321.4a6ccf44-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190909.112314.de75c13a-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190907.202310.75a9adbc-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190830.202245.9d3d1542-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190827.222322.b3a0cc91-1
- Update to latest snapshot.

* Mon Jul 29 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190729.192555.2aaf231b-1
- Update to latest snapshot.

* Sat Jul 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190720.092522.7b9bb1de-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190717.100655.9de70f8d-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190716.153530.80e3f7d6-1
- Update to latest snapshot.

* Mon Jul 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190701.220632.3126f64d-1
- Update to latest snapshot.

* Mon Jul 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190701.215639.f2f38095-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190626.204336.6243fe7c-1
- Update to latest snapshot.

* Tue Jun 25 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190625.155146.99ea33e2-1
- Update to latest snapshot.

* Thu Jun 13 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190613.165448.91ac1952-1
- Update to latest snapshot.

* Wed Jun 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190612.015230.7b5a35d2-1
- Update to latest snapshot.

* Tue Jun 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190611.060422.eb726656-1
- Update to latest snapshot.

* Fri Jun 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190607.073525.6b7cd69e-1
- Update to latest snapshot.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190604.203802.14c38e98-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190531.045003.13fe0a4a-1
- Update to latest snapshot.

* Thu May 23 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190523.153955.e612aa05-1
- Update to latest snapshot.

* Thu May 23 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190523.141257.8b6ef37f-1
- Update to latest snapshot.

* Tue Apr 23 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190423.113145.16af6af9-1
- Update to latest snapshot.

* Mon Apr 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190422.183144.3dd488fa-1
- Update to latest snapshot.

* Sun Apr 21 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190421.205903.40decf47-1
- Update to latest snapshot.

* Wed Apr 10 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190410.095311.81c26823-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190405.115214.933d55f7-1
- Update to latest snapshot.

* Sat Mar 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190316.212712.b47cdbbb-1
- Update to latest snapshot.

* Fri Mar 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190315.070917.5659fbbd-1
- Update to latest snapshot.

* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190313.172707.256397ae-1
- Update to latest snapshot.

* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190313.162706.b562bcc8-1
- Update to latest snapshot.

* Sun Mar 10 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190310.202710.30d9d450-1
- Update to latest snapshot.

* Fri Mar 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190308.141049.33c8b566-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190307.174612.47ed3182-1
- Update to latest snapshot.

* Sun Mar 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190303.133026.acdca1f0-1
- Update to latest snapshot.

* Thu Feb 21 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190221.073415.8a9d661a-1
- Update to latest snapshot.

* Wed Feb 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190220.173847.cdf082d1-1
- Update to latest snapshot.

* Sun Feb 17 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190217.195404.4e63f55c-1
- Update to latest snapshot.

* Thu Feb 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190214.220039.51dc2e54-1
- Update to latest snapshot.

* Thu Feb 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190214.064707.7681e967-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190212.000404.ec5724b6-1
- Update to latest snapshot.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190211.215715.68a8f0fd-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190209.113734.c2a9bc92-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190207.000042.bbbc8f16-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190207.000036.e6d59515-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190206.174550.3d8fd7e8-1
- Update to latest snapshot.

* Sun Feb 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190203.202823.0ccca786-1
- Update to latest snapshot.

* Sun Feb 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190203.120917.8c8e9500-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190128.214507.93b3d4a5-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190128.151757.d52c5478-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190128.080919.93ccc23f-1
- Update to latest snapshot.

* Sun Jan 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190127.000114.0b92a2bb-1
- Update to latest snapshot.

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190123.180743.a28016a5-1
- Update to latest snapshot.

* Fri Jan 18 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190118.045943.373c84bb-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190115.130122.006680bd-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190115.000541.4dfbfcbe-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190114.164004.b1a91d6a-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190114.000240.174e1223-1
- Update to latest snapshot.

* Sun Jan 13 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190113.090054.c2218b41-1
- Update to latest snapshot.

* Sat Jan 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190112.134402.34dfbbd4-1
- Update to latest snapshot.

* Sat Jan 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190112.000913.a4928308-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190111.205335.60dc05d3-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190111.131334.5d88b6e8-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190111.093732.eb622ee8-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190111.085458.4cecb59d-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190111.003910.2a6450e2-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190110.214743.dc262e22-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190110.134059.398f6efa-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190109.093337.e6aae00d-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190109.000625.cad59559-1
- Update to latest snapshot.

* Tue Jan 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190108.180523.11627e2e-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190107.000306.229fe85e-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190105.025907.67860a7b-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190104.005522.f40f66bf-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190103.000429.3ad4da64-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190102.221722.1b95b196-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190102.190843.a00ef006-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190102.183844.6f9d567e-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git190101.003240.9afb2087-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181224.105426.798f7eef-1
- Update to latest snapshot.

* Sat Dec 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181222.105651.7ea3f76c-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181221.021103.c7d10a90-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181220.214604.91e05f11-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181220.141326.1ac91f10-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181219.120807.614fd7aa-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181219.110424.b39bc54f-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181219.000739.24f2fd4a-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181218.163320.fb068e4b-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181218.124158.8eb41e0f-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181218.110412.592caf46-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181218.105514.69c5cd69-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181218.060518.ca170dba-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181217.061041.3cd60697-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181204.143528.2a633841-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181126.174308.b9aef3c3-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181112.165250.8f86b5c5-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181107.173401.bc61b816-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181105.204856.004a725f-2
- Require granite >= 5.2.0.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181105.204856.004a725f-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181102.083559.20eab2ea-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181102.083559.20eab2ea-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181029.185443.ace22983-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181029.174833.1d9b3900-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181029.093843.0d10f351-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181026.164252.a25b7d55-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181025.091500.deb577b3-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181023.213556.9da633a8-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181023.204710.598df5e0-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181023.125008.a8b8b354-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181022.203003.902f87a4-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181022.161029.46fbd0f1-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181017.174742.a00c9d66-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181017.170608.7086c825-1
- Initial package.


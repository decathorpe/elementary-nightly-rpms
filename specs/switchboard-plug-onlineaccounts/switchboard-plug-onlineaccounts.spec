%global __provides_exclude_from ^%{_libdir}/(switchboard)/.*\\.so$

%global plug_type network
%global plug_name online-accounts

Name:           switchboard-plug-onlineaccounts
Summary:        Switchboard Online Accounts plug
Version:        2.0.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libsignon-glib) >= 2.0
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       hicolor-icon-theme

# make sure old sub-packages are removed upon upgrade
Provides:       pantheon-online-accounts
Obsoletes:      pantheon-online-accounts

Provides:       pantheon-online-accounts-libs
Obsoletes:      pantheon-online-accounts-libs

Obsoletes:      pantheon-online-accounts-devel


%description
%{summary}.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%files -f %{plug_name}-plug.lang
%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_libexecdir}/io.elementary.online-accounts.*

%{_datadir}/accounts/providers/*.provider
%{_datadir}/accounts/services/*.service
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOnUI.service
%{_datadir}/icons/hicolor/*/apps/*.svg


%changelog
* Sat Dec 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181222.104204.dbf3d131-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181221.020027.ef861b66-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181219.110021.ae2f42ae-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.205843.3f2c3411-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.142714.8dcd41e0-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.130317.323aebd1-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.112541.f914247a-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.105050.9471341a-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.095450.a9a849bf-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181217.062839.a7de59cb-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181214.232918.d49d9d71-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181211.064726.f63a0e05-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181210.221745.44028343-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181210.214605.49b82b64-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181208.214548.01987c7b-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181207.040301.e8aba6b3-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181207.025111.e212056d-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181202.064418.31b3e35d-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181126.071028.6e87ed56-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181122.064756.c58523d5-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181119.190442.ee602729-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181116.082402.6f4b520b-1
- Update to latest snapshot.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181114.025241.2c0f038e-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181113.190149.cbd976ca-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181112.180542.a11177ca-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181112.170044.fb1ce336-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181112.154406.fe2b817a-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181112.050232.d9d257f0-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181110.161001.0f213686-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181110.101549.9ae0a4f2-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181110.071454.a16bf01e-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181110.025804.33a362b4-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.230142.c2972696-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.225049.525b53ed-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.190001.91195702-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.173120.97c63fef-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181109.063550.2d8829dc-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181108.210735.f9f4a764-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181107.165258.c192be5b-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181107.130735.55b07b07-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181106.212945.fc06b284-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181105.201921.0751c294-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181105.182101.003d6673-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181105.010917.6435b147-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181028.160943.facc0045-2
- Occasional mass rebuild.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181028.160943.facc0045-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git181025.080926.ede2d8c3-1
- Update to version 2.0.1.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181020.133815.d4dd9bda-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181016.101331.d176a3c6-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181015.223557.c361131d-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181015.163827.3e9f8704-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181015.144935.58ea9191-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181014.021817.6d1316a4-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181014.000356.3d887e66-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.145651.d0792290-2
- Adapt to CMake -> meson switch.
- Adapt to upstream dependency changes.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.145651.d0792290-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.123315.7186b6fe-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.082238.ddf8f687-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181013.010238.7509ae03-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181012.200027.76df4d61-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181012.183505.8117a332-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181012.163143.9563a1ba-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181012.122341.06b77032-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181010.172327.45844513-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181009.174832.727394f4-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181008.000550.5148e1bb-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181007.024531.e16a6297-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git181003.001112.989c409f-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180920.000502.ac9f5d8b-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180919.000951.4cf8463c-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180907.000637.99cce44c-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180901.000915.ef455438-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180830.000820.31c9be9f-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180819.000954.46ab224f-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180722.121017.4d9120fe-2
- Occasional mass rebuild.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180722.121017.4d9120fe-1
- Update to latest snapshot.

* Sat Jul 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180713.000426.28ab9f76-2
- Add missing BR: gcc, gcc-c++.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180713.000426.28ab9f76-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180709.001039.065523ec-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180615.001137.6681f49f-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180614.084400.f7e7d699-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git180608.001247.71232c3e-1
- Update to version 0.3.1.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180608.001247.71232c3e-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180602.000659.f4a516eb-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180601.000846.5939f300-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.000340.ba846e3a-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180530.000452.f15fc437-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180529.001328.4ef48886-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180528.013226.a2d80eb8-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180527.000610.8d9f2d8a-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180525.000844.2b7afbc9-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180517.000438.7dcdfebb-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180516.142722.5a3b2494-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180512.001224.1d3bb83f-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180507.214154.8e1a7250-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180506.165017.428d765c-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180503.080142.82ff3bc0-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180429.140459.d27880a1-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180426.000400.bbae39f4-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180425.000355.fa2cf116-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180420.001229.076f8540-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180414.122720.0a67281a-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180413.224003.53ed4500-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180413.174634.57314690-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180328.000418.dd88920e-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180326.000923.e0e81d25-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180325.000944.f1062df8-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180322.000551.e076b4f0-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180318.000834.4ba1ddb0-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180314.000246.dd7645af-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180312.001018.6449fd0d-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180310.000445.baf33cb0-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180308.175706.fe9c5855-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180224.000451.858c3a83-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180211.000918.86f9a2b3-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180205.001214.43e2b5ec-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180119.124731.fe7d6b39-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171104.071431.369e4703-3
- Remove icon cache scriptlets.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171104.071431.369e4703-2
- Merge .spec file from fedora.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171104.071431.369e4703-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170818.231615.62729c89-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170703.172833.b673f979-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170628.152738.cde8dcd5-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170617.150143.919b2c92-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170417.235528.5a0270aa-1
- Initial package.



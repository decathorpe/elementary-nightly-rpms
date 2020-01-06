%global srcname code
%global appname io.elementary.code

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-code
Summary:        Code editor from elementary
Version:        3.1.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  vala-devel
BuildRequires:  libvala-devel

BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.24
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       hicolor-icon-theme

Obsoletes:      scratch-text-editor
Provides:       scratch-text-editor


%description
%{summary}.


%package        devel
Summary:        The text editor that works (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

This package contains the development headers.


%prep
%autosetup

chmod +x meson/post_install.py


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%if 0%{?suse_version}
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/
%{_libdir}/libcodecore.so.0
%{_libdir}/libcodecore.so.0.0

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml


%files devel
%{_includedir}/codecore.h

%{_libdir}/libcodecore.so
%{_libdir}/pkgconfig/codecore.pc

%{_datadir}/vala/vapi/codecore.deps
%{_datadir}/vala/vapi/codecore.vapi


%changelog
* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git200106.180742.ea56cab4-1
- Update to latest snapshot.

* Tue Dec 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191231.190727.721661c7-1
- Update to latest snapshot.

* Mon Dec 30 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191230.075629.8c0ce7c3-1
- Update to latest snapshot.

* Fri Dec 27 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191227.062438.766aec4b-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191226.000759.ec793588-1
- Update to latest snapshot.

* Mon Dec 23 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191223.072156.07b6d4f8-1
- Update to latest snapshot.

* Sat Dec 21 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191221.182553.6f7ae946-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191219.053556.68d11180-1
- Update to latest snapshot.

* Mon Dec 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191216.214137.b9ed8560-1
- Update to latest snapshot.

* Sun Dec 15 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191215.020707.9f6dc2f9-1
- Update to latest snapshot.

* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191213.170721.e9066520-1
- Update to latest snapshot.

* Wed Dec 11 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191211.182603.49663df5-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191125.212933.cd28d403-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191125.205650.7a0d831c-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191125.194553.5a9c13cb-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191125.182427.59277e49-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191122.032515.73356508-1
- Update to latest snapshot.

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191119.181530.f1211d91-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191115.194207.c8774677-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191111.122442.5dd01803-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191109.112431.624b7c2b-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191106.100547.52730935-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191106.095714.c0ca4292-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191106.005754.95811665-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191105.132436.b28cb284-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191104.184510.6a2a2086-1
- Update to latest snapshot.

* Mon Oct 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191028.165902.3867082d-1
- Update to latest snapshot.

* Sun Oct 27 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191027.102430.90bd6af8-1
- Update to latest snapshot.

* Sat Oct 19 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191019.042418.ce7a9fb5-1
- Update to latest snapshot.

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191016.192403.d6ace0ca-1
- Update to latest snapshot.

* Mon Oct 14 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191014.112408.702c2839-1
- Update to latest snapshot.

* Sun Oct 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191013.211258.c7f83a54-1
- Update to latest snapshot.

* Thu Oct 10 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191010.152348.fdaa2689-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191009.142350.fd627ff4-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191007.231243.b8d26505-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191007.201012.314d3f91-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191007.161400.56d76d07-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191007.012352.c81a1cd6-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191005.212340.a07086cb-1
- Update to latest snapshot.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191004.154651.f7d59da9-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git191002.223135.388b5b39-1
- Update to latest snapshot.

* Sun Sep 29 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190929.095134.8d19ae44-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190919.183949.1ee91ac6-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190911.162443.fb8af720-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190911.074810.28c876f2-1
- Update to latest snapshot.

* Tue Sep 10 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190910.145504.311266b4-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190909.183331.41d4471d-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190909.165248.63a84d5a-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190902.012239.fd4c288f-1
- Update to latest snapshot.

* Sun Sep 01 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190901.132410.cc0b2356-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190829.152242.6d34e5dd-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190827.222221.8c6cb16b-1
- Update to latest snapshot.

* Sat Aug 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190729.204214.0dc21ab6-2
- Relax condition on libvala dependency.

* Mon Jul 29 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190729.204214.0dc21ab6-1
- Update to latest snapshot.

* Thu Jul 18 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190718.002410.18728dfe-1
- Update to latest snapshot.

* Fri Jul 12 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190712.154614.4f774c1d-1
- Update to latest snapshot.

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190709.214116.fafa53b8-1
- Update to latest snapshot.

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190709.190301.97e99389-1
- Update to latest snapshot.

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190709.185914.f3768ea4-1
- Update to latest snapshot.

* Mon Jul 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190708.182013.96d64aaa-1
- Update to latest snapshot.

* Mon Jul 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190708.143142.70d6dec8-1
- Update to latest snapshot.

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190703.142604.57ba6277-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190626.204244.a7cb973e-1
- Update to latest snapshot.

* Thu Jun 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190613.194326.fa3e50ca-1
- Update to latest snapshot.

* Sun Jun 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190609.022954.88ea25a1-1
- Update to latest snapshot.

* Sat Jun 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190608.013524.06387ce2-1
- Update to latest snapshot.

* Sat Jun 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190608.003417.8e5299eb-1
- Update to latest snapshot.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190604.212018.37b27542-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190531.045931.4094c294-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190530.231023.07b27bc9-1
- Update to latest snapshot.

* Tue May 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190528.070330.a112812f-1
- Update to latest snapshot.

* Sun May 26 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190526.152902.576c7807-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190514.190240.8e61a9b6-1
- Update to latest snapshot.

* Mon May 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190513.115402.88e9c25c-1
- Update to latest snapshot.

* Mon May 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190513.040652.07024667-1
- Update to latest snapshot.

* Tue Apr 30 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190430.165926.c37c374a-1
- Update to latest snapshot.

* Thu Apr 25 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190425.084237.5480ec3e-1
- Update to latest snapshot.

* Tue Apr 23 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190423.215434.c08e5b95-1
- Update to latest snapshot.

* Tue Apr 23 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190423.101334.327158c7-1
- Update to latest snapshot.

* Mon Apr 22 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190422.150816.ff9abc3d-1
- Update to latest snapshot.

* Mon Apr 15 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190415.164514.8ac9fcd5-1
- Update to latest snapshot.

* Sun Mar 17 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1+git190314.184315.66f27732-1
- Update to version 3.1.1.

* Thu Mar 14 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+git190314.184315.66f27732-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+git190312.082451.ef118956-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+git190312.031531.cb9fc92b-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+git190307.191107.c95adcfc-1
- Update to version 3.1.0.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190307.191107.c95adcfc-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190307.182306.ea69aeef-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190307.102617.289463a8-1
- Update to latest snapshot.

* Wed Mar 06 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190306.111442.a56645b2-1
- Update to latest snapshot.

* Sun Mar 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190303.141942.cbbfd0b5-1
- Update to latest snapshot.

* Thu Feb 21 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190221.000558.480b3f87-1
- Update to latest snapshot.

* Sat Feb 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190216.180619.cc80f278-1
- Update to latest snapshot.

* Fri Feb 15 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190215.083456.e709b455-1
- Update to latest snapshot.

* Wed Feb 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190213.000734.caab3c32-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190212.161657.6180103e-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190212.000635.3eae7638-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190209.114617.514852e0-1
- Update to latest snapshot.

* Fri Feb 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190208.051256.cb72473f-1
- Update to latest snapshot.

* Thu Feb 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190207.000603.a4739955-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190206.190444.498caf44-1
- Update to latest snapshot.

* Wed Feb 06 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190206.154055.1167ff5f-1
- Update to latest snapshot.

* Sun Feb 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190203.120256.7db0b2f9-1
- Update to latest snapshot.

* Fri Feb 01 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190201.031724.32f34369-1
- Update to latest snapshot.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190129.211246.6e1345e1-1
- Update to latest snapshot.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190129.000315.8fcdf1a0-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190128.222644.991cc08f-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190128.214349.283daec5-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190128.152051.70b34c6e-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190128.141848.a7122b20-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190128.120623.9eee2fc1-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190128.111020.c409c986-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190128.104146.a6f39c23-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190128.081012.4cc4b6c7-1
- Update to latest snapshot.

* Sun Jan 27 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190127.213601.504a2a7a-1
- Update to latest snapshot.

* Sun Jan 27 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190127.000055.093269de-1
- Update to latest snapshot.

* Sat Jan 26 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190126.181803.62d24e00-1
- Update to latest snapshot.

* Sat Jan 26 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190126.152809.60bbd54b-1
- Update to latest snapshot.

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190123.180245.728823f3-1
- Update to latest snapshot.

* Mon Jan 21 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190121.182042.bc62520c-1
- Update to latest snapshot.

* Fri Jan 18 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190118.050329.8a19ff3f-1
- Update to latest snapshot.

* Wed Jan 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190116.123305.1ba1d705-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190115.123633.afd5cb7c-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190114.000822.0cb86d09-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190111.085800.f3083be0-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.210850.1c9b35e7-2
- Adapt to libvala version bump.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.210850.1c9b35e7-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.185835.50a5104c-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.152811.7d789306-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.130813.300d3533-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.123735.b68178c0-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.120024.c96e2415-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.105156.dc266277-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.062549.4961d73d-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190109.000221.cae07ae5-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190108.235407.b0e4fb7b-1
- Update to latest snapshot.

* Tue Jan 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190108.143219.5f3d6236-1
- Update to latest snapshot.

* Tue Jan 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190108.085444.97d276b6-1
- Update to latest snapshot.

* Tue Jan 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190108.002204.e3f884fd-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.2+git190107.185554.f85ac2aa-1
- Update to version 3.0.2.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190107.185554.f85ac2aa-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190107.163209.1867a468-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190107.152732.d9d359f9-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190107.141037.bd076886-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190107.123515.d69e750b-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190107.115446.8056c743-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190107.105849.e27cc6d4-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190107.082452.99092173-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190107.075946.a3db4d41-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190104.195234.0aaf8a72-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190104.000747.c6b2c90c-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190103.223420.424026fe-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190103.100417.e9a5a40e-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190103.071439.69464d20-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190103.063428.c9c363ed-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190102.180047.b81086d0-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git181219.181209.7cafbb53-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git181219.171059.a7a43cdb-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git181219.165456.05cba1b3-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git181216.192437.d40820e8-1
- Update to version 3.0.1.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181216.192437.d40820e8-1
- Update to latest snapshot.

* Sun Dec 09 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181209.000032.11903ec6-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181208.163037.1d8cf998-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181206.220907.cce8e298-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181203.000834.bd311260-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181202.061919.98d8933e-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181130.140636.1f008823-1
- Update to latest snapshot.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181129.000206.40b0c7ee-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181128.143435.44d1014a-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181124.072306.78e96c9b-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181123.000145.61e4b85c-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181122.000203.93f9b34a-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181121.125412.c8c16842-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181121.112852.95074987-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181121.000353.f2370c9b-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181120.130005.62772d8a-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181119.173359.4540a289-1
- Update to latest snapshot.

* Sun Nov 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181118.200940.9256568e-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181117.002304.d0fa69b3-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181116.115052.fb35ed1e-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181116.083948.9dd98697-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181115.155848.caf757ee-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181106.161923.478e19be-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181105.000916.a12b4f23-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181104.110941.1320ddef-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181104.105823.57a8c527-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181104.000303.efe76c85-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181101.232404.1b5ffc54-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181101.232404.1b5ffc54-1
- Update to latest snapshot.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181101.101701.12796cda-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181030.000026.7ec4b1f8-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181029.192625.3a34bbe0-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181029.000942.a8ece41c-2
- Adapt to cauldron/tumbleweed/fedora differences.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181029.000942.a8ece41c-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181028.000535.7cda144b-1
- Update to latest snapshot.

* Sat Oct 27 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181027.224451.ec7aa5b9-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181026.175412.8e1a55d1-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181026.000434.c1cc935a-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181025.072525.8718e175-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181025.060933.c8d48382-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181025.000910.04daec9d-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181024.133336.6f16d110-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181023.000258.16e5fe67-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181022.000301.6cb4bfe6-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181021.113908.f67b3e7d-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181021.101948.01194d24-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181021.000706.50951bc0-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181020.001023.0ae051d0-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181019.173514.f2af1811-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181018.212803.44f85c16-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181018.000926.ef9cd754-1
- Update to version 3.0.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181018.000926.ef9cd754-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181016.093813.ec222a7a-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181016.000826.040aeb5f-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181015.141947.683bd57c-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181015.035735.f388ccd5-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181014.182725.9c548b23-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181013.172030.7a978934-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181013.000855.7e4ea3bb-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181010.182529.baf32f3c-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181010.122011.a7043899-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181007.023648.893c4c21-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181005.100045.3f4cde09-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181005.000805.42423b04-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181003.142415.cd3e50b2-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181003.001033.f4033cf1-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181002.191327.ca453574-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180930.000925.dc5cc29e-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180928.000655.22e8dc1b-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180927.000955.6d180931-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180926.212100.2d23f582-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180925.000135.abb3cd0f-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180924.071733.93ecb0b1-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180924.000459.7d2949e4-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180921.181906.fa9668a1-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180919.142014.2091cb54-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180919.112543.a27054ad-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180919.102017.5feaf3dc-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180919.075609.d18135cf-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.234815.093cb61a-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.212746.b07f182b-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.181436.5b17ffdc-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.175315.d11c501d-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.154547.241c7579-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.070149.2ed1477d-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.003506.2fccf1d6-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180917.215938.1c3b9b92-1
- Update to latest snapshot.

* Sun Sep 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180916.105037.81b503eb-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180911.171723.6a0c5d4e-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180906.000849.74e42c3a-1
- Update to latest snapshot.

* Tue Sep 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180904.000554.7554101b-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180901.000807.696e2ceb-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180831.130415.0c6093c6-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180831.115906.a265f9f2-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180831.025118.92086580-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.194029.27fecd61-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.182358.6e69e299-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.054758.6c46c77b-2
- Adapt to upstream dependency changes.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.054758.6c46c77b-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180826.000409.df6691cb-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180823.170549.24b4a60f-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180820.211957.477faeae-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180820.174319.e55d48c4-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180819.000847.98e6edea-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180818.134306.275970c6-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.150514.7d984752-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.031621.591cb429-3
- Fix building by being less smart.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.031621.591cb429-2
- Occasional mass rebuild.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.031621.591cb429-1
- Update to latest snapshot.

* Tue Aug 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180813.000248.959b5715-2
- Adapt to libvala bump.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180813.000248.959b5715-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180812.112418.4c9c72f8-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180812.000533.02084e1a-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180809.125811.5b7fbfda-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180809.000504.3b318b31-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.151542.322c2eec-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.135615.608fcae3-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.091545.1439bb9d-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.080835.12a5e22a-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.062727.911932b0-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180803.000350.d3a45b28-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180802.181951.8c5f17da-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180731.223701.e0004a34-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180730.000718.a62fa1ea-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180722.000325.07b93fd1-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.190302.8cf17e8b-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.121900.83ee0290-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.104145.60be3c97-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.000707.f5cd46f4-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180720.111147.63e4f159-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180720.000650.3ff1e5c8-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180719.170336.a28ca0d0-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180719.000331.17b6ff9f-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.185919.91033659-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.122448.b000917b-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.101018.8870817d-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.082404.afe66381-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.073221.6fd4b53b-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180717.183506.7c281376-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180717.173400.b277fda3-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180715.000959.e90959dc-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180713.000329.d3492b37-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180710.143312.12e5dd6a-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180710.000325.78d6a211-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180706.000757.d147cbec-2
- Adapt to upstream file changes.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180706.000757.d147cbec-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180704.210827.bcefca30-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180703.000557.6d626625-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180615.001000.737256ff-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180614.000708.9a4a16ea-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180613.152600.0d8de916-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180613.121936.b566cec3-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180613.000241.3c1cb848-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180612.162950.a24e9566-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180610.001105.6e22c031-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180608.001112.14471ee3-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180606.205953.6a5cc8fd-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180606.000759.60471b55-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180605.092434.5bdc20c9-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180605.000521.bc6e2d91-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180604.000827.df6bc66e-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180603.162531.d1618141-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180602.000435.f63a2d78-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180601.000652.06bd1c68-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180531.150917.46f6cee7-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180531.144958.ca362b18-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180531.000206.372c3b67-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180529.001104.68360211-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180528.123800.b237d932-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180527.000443.47159cf0-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180526.073944.9cfeffa8-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180524.160358.21d512a8-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180518.082357.0c987928-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180517.000131.1160c09a-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180516.184432.86040600-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180515.000540.f25153e8-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180514.145252.dc765970-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180512.001056.370e422d-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180511.061657.4d0fc620-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180510.064254.d3effc13-1
- Fix build due to bogus changelog entries.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180421.162355.9329bf5b-1
- Update to latest snapshot.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180421.001026.9209d900-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180420.001116.92d67c54-1
- Update to latest snapshot.

* Thu Apr 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180419.172746.ca7a24f6-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180417.183345.622afc32-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180416.000339.13d09286-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180415.171917.abac84b8-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180403.000528.88639b83-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180328.000336.2d04e755-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180327.000137.86513d03-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180326.072358.fefa07b2-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180324.151817.64db28f9-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.191347.8ff356a4-1
- Update to latest snapshot.
- Adapt to upstream dependency changes.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.185628.7ea0aac1-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.134356.17216658-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.021758.e59a69a2-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180321.160405.0a830c14-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180320.191932.91728fda-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180320.182241.89dd92f5-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180320.034656.d06bc802-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.225618.af5b02ea-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.204714.6f545742-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.182316.4eb6bf78-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.155402.0a03186c-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.000143.c263fa22-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180318.014452.600d44ae-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.225504.5197da96-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.193317.53c41de6-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.101513.e0a7cdc9-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.091702.61f4b86b-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.001124.40c0b8b3-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180316.182314.a4212caa-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180316.004052.b29a98a5-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180315.180805.2e970910-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180315.004730.9a1b77ca-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180314.000156.e16b5795-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180312.202140.d65721e2-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180310.000330.a44720c2-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180309.112149.a400d30b-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180307.000931.3fe16b80-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180306.000445.5b84a413-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180304.000738.1c5e17af-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180301.000317.1599c6fa-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180227.185938.5312a6a6-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180227.000356.827a5d89-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180226.105909.8b98c54e-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180225.165330.c726d965-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180225.023324.d7ef7e5d-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180224.115243.1a4af761-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180223.181222.6e77ae1b-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180222.000758.26f3b776-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180221.143240.251c99b9-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180221.123443.c8e53c66-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180221.074128.83155730-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180220.192202.59278f0c-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180220.022714.e305f284-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180219.175143.82a1697f-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180218.145615.edc1200c-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180216.125400.069696a9-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180216.000253.9691592b-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180214.182858.2d3f62bd-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180214.013747.b4951d12-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180213.213524.e3686e34-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180213.005517.891c74fa-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180212.212015.b3353b8f-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180212.160234.0954ba6d-2
- Adapt to cmake -> meson switch.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180212.160234.0954ba6d-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180209.001000.2d369a0a-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180206.200848.714fc767-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180129.195832.b8629598-2
- Be lazy about undefined symbols in plugins.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180129.195832.b8629598-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180129.185322.b15ff49d-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180125.000833.ad688fc4-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180124.123947.d3ab6ba9-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180123.221341.4969d443-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180122.060359.dc426bee-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180120.020812.e959a13c-1
- Update to latest snapshot.

* Wed Jan 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180117.192407.07d814d5-1
- Update to latest snapshot.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180116.180121.cc9cd0ba-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180112.191811.9961a070-1
- Update to latest snapshot.

* Thu Jan 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180111.160157.63bf2a42-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.231632.616f30af-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.222901.cefbdb61-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.170232.0d7cbb8a-1
- Update to latest snapshot.

* Mon Jan 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180108.201726.899b0b68-2
- Adapt to upstream file changes.

* Mon Jan 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180108.201726.899b0b68-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180106.000312.b62cbf36-2
- Remove icon cache scriptlets.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180106.000312.b62cbf36-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180105.001608.fc57a13d-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git171219.151614.17101d60-1
- Initial package.



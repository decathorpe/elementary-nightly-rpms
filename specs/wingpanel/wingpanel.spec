%global appname io.elementary.wingpanel

%global common_description %{expand:
Stylish top panel that holds indicators and spawns an application
launcher.}

Name:           wingpanel
Summary:        Stylish top panel
Version:        2.2.6+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.24.0

BuildRequires:  mutter-devel

BuildRequires:  pkgconfig(gala)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(granite)

Requires:       hicolor-icon-theme

%description %{common_description}


%package        libs
Summary:        Stylish top panel (shared library)
%description    libs %{common_description}

This package contains the shared library.


%package        devel
Summary:        Stylish top panel (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel %{common_description}

This package contains the files required for developing for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang wingpanel

# create plugin directory
mkdir -p %{buildroot}/%{_libdir}/wingpanel

# create settings directory
mkdir -p %{buildroot}/%{_sysconfdir}/wingpanel.d


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f wingpanel.lang
%license COPYING
%doc README.md

%{_bindir}/wingpanel

%{_libdir}/gala/plugins/libwingpanel-interface.so

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%files libs
%license COPYING
%doc README.md

%dir %{_sysconfdir}/wingpanel.d
%dir %{_libdir}/wingpanel

%{_libdir}/libwingpanel-2.0.so.0
%{_libdir}/libwingpanel-2.0.so.0.2.0


%files devel
%license COPYING
%doc README.md

%{_includedir}/wingpanel-2.0/

%{_libdir}/libwingpanel-2.0.so
%{_libdir}/pkgconfig/wingpanel-2.0.pc

%{_datadir}/vala/vapi/wingpanel-2.0.deps
%{_datadir}/vala/vapi/wingpanel-2.0.vapi


%changelog
* Tue Jan 28 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git200128.080623.35dfcd8c-1
- Update to latest snapshot.

* Wed Jan 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git200122.185405.cde24a7f-1
- Update to latest snapshot.

* Wed Jan 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git200122.175340.da03fa2d-1
- Update to latest snapshot.

* Fri Jan 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git200103.220731.c2a4197c-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191217.224954.4db5ec3d-1
- Update to latest snapshot.

* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191107.202405.d8aeb883-2
- Rebuild for switch to mutter 3.3x.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191107.202405.d8aeb883-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191106.002332.0295a458-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191105.212402.a04479e9-1
- Update to latest snapshot.

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191103.002359.fb81bcb9-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6+git191101.125122.23a73e76-1
- Update to version 2.2.6.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191101.125122.23a73e76-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191031.204142.09462f55-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191030.232335.02ee1c20-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191029.222635.1df4fc39-2
- Adapt to upstream changes.

* Tue Oct 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191029.222635.1df4fc39-1
- Update to latest snapshot.

* Tue Oct 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191029.194822.efbab5bf-1
- Update to latest snapshot.

* Tue Oct 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191029.190019.21d961dd-1
- Update to latest snapshot.

* Wed Oct 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191023.085619.b6811e83-1
- Update to latest snapshot.

* Mon Oct 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191014.192555.bd6ddfc2-1
- Update to latest snapshot.

* Mon Oct 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191014.173546.ab20c221-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191003.152040.61488878-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191001.145826.e4652387-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191001.083808.5cdc32bd-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git191001.015846.da64cca4-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190919.182047.f8fae894-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190830.212311.584a372f-1
- Update to latest snapshot.

* Mon Aug 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190812.194724.0f167bcb-1
- Update to latest snapshot.

* Thu Jul 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190725.043426.727d7043-1
- Update to latest snapshot.

* Thu Jul 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190711.154959.e12385ed-1
- Update to latest snapshot.

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190702.234948.ddf0de85-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190626.204649.7bc969b9-1
- Update to latest snapshot.

* Thu Jun 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5+git190605.095520.1fbb38ce-1
- Update to version 2.2.5.

* Wed Jun 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190605.095520.1fbb38ce-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190531.044557.94615a8a-1
- Update to latest snapshot.

* Sun May 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190512.215027.86098c20-1
- Update to latest snapshot.

* Sun May 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190511.231805.31980680-1
- Update to latest snapshot.

* Wed May 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190501.002411.687b3166-1
- Update to latest snapshot.

* Wed Apr 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4+git190424.123039.15da046c-1
- Update to version 2.2.4.

* Wed Apr 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190424.123039.15da046c-1
- Update to latest snapshot.

* Tue Apr 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190423.113358.25af8fec-1
- Update to latest snapshot.

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3+git190318.163823.e5432f12-1
- Update to version 2.2.3.

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190318.163823.e5432f12-1
- Update to latest snapshot.

* Tue Feb 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190225.232554.fc1b8ea3-1
- Update to latest snapshot.

* Fri Jan 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git190117.200329.44b5f49a-1
- Update to version 2.2.2.

* Thu Jan 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190117.200329.44b5f49a-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190114.170305.65e66c1a-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190111.000744.3b37fa0a-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181220.122356.f9ad33a2-1
- Update to version 2.2.1.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181220.122356.f9ad33a2-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181211.225715.dd64ba82-2
- Adapt to CMake -> meson switch.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181211.225715.dd64ba82-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181202.053540.b0a8cb40-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181104.224453.b009131a-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181027.170845.8aacbcf5-2
- Occasional mass rebuild.

* Sat Oct 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181027.170845.8aacbcf5-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181025.101353.fe26118e-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181023.122941.654d77bf-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181018.170818.42bbb42b-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181018.083009.d4d8d0e3-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181015.054124.5fa1bd45-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181013.212105.5d6d1004-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181011.194449.fd0ebe1d-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181010.181821.4f1672f6-1
- Update to latest snapshot.

* Sat Oct 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181004.143415.1bc406e7-1
- Update to version 2.2.0.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181004.143415.1bc406e7-1
- Update to latest snapshot.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git181001.090627.c0e3cab9-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180910.233108.62841217-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180724.030936.6e7163ba-3
- Rebuild for gala mutter328 support.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180724.030936.6e7163ba-2
- Occasional mass rebuild.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180724.030936.6e7163ba-1
- Update to latest snapshot.

* Sat Jul 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180714.021814.4d47d06a-2
- Add missing BR: gcc, gcc-c++.

* Sat Jul 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180714.021814.4d47d06a-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180710.084651.4257f977-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180709.102949.8559b1da-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1+git180706.025944.4007a0da-1
- Update to version 2.1.1.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180706.025944.4007a0da-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180628.174238.f8341c84-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180611.173547.5a038ca2-2
- Adapt to upstream file changes.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180611.173547.5a038ca2-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180610.001420.650b45bc-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180606.114154.e6363ef3-1
- Update to version 2.1.0.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180606.114154.e6363ef3-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180529.173131.69a0e08c-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180529.115925.0354979e-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180525.230611.f45ad708-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180515.184608.105c1d0c-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180509.192023.ce82b438-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180429.171525.aaf6bf89-1
- Update to latest snapshot.

* Wed Apr 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180418.085804.a437def1-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180404.221723.ea00c6c9-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180326.230847.71572016-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180304.223212.61c4f9fe-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180301.035959.ec08fc69-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180227.204746.c33538ca-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180123.164118.24e4bc4a-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180123.164115.13b6f31a-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git180109.211653.2742b76f-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171228.191354.fceb2a0e-3
- Remove icon cache scriptlets.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171228.191354.fceb2a0e-2
- Merge .spec file from fedora.

* Thu Dec 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171228.191354.fceb2a0e-1
- Update to latest snapshot.

* Mon Dec 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171217.225711.99d68c1f-1
- Update to latest snapshot.

* Sat Dec 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171209.001619.c9ec63d5-1
- Update to latest snapshot.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171112.174057.6120bb4e-1
- Update to latest snapshot.

* Wed Oct 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git171018.165259.ba79059d-1
- Update to latest snapshot.

* Fri Sep 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git170929.175649.d95e3a6c-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git170925.094220.4dd02953-1
- Update to latest snapshot.

* Wed Sep 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git170920.164736.3362a41e-1
- Update to latest snapshot.

* Wed Sep 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4+git170912.020136.6d4d6108-1
- Update to version 2.0.4.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170912.020136.6d4d6108-1
- Update to latest snapshot.

* Sun Sep 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170902.204052.434f6743-1
- Update to latest snapshot.

* Fri Sep 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170901.150050.7a1a5834-1
- Update to latest snapshot.

* Fri Sep 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170901.053352.81c9dd69-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170725.184035.e0d0dc3c-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170724.181439.af3b22c2-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170724.174100.916be7c9-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170706.075146.0b938258-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170702.101840.b565cb61-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170620.180231.74e81f3a-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170617.152544.fce293ab-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170602.172312.51d21feb-1
- Update to latest snapshot.

* Wed May 31 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170530.215459.0b6d4863-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170530.190722.3adbfc1a-1
- Update to version 2.0.3.

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev183-1
- Update to latest snapshot.

* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev182-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev180-2
- Adapt to upstream file changes.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev180-1
- Update to latest snapshot.

* Wed Mar 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev176-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev175-1
- Update to latest snapshot.

* Fri Mar 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev173-1
- Update to version 2.0.2.

* Fri Mar 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev173-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev172-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev171-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev170-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev169-1
- Update to latest snapshot.

* Sun Feb 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev168-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev167-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev166-1
- Update to latest snapshot.

* Tue Jan 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev165-1
- Update to version 2.0.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev164-1
- Update to version 2.0.1.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev163-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev162-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev161-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev160-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev159-1
- Update to latest snapshot.

* Thu Nov 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev158-2
- Remove rpath workaround, fix is upstream now.

* Thu Nov 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev158-1
- Update to latest snapshot.

* Thu Nov 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev157-2
- Add rpath workaround for f25.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev157-1
- Update to latest snapshot.

* Tue Nov 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev156-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev155-3
- *Really* rebuild for new gala.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev155-2
- Rebuild for new gala.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev155-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev154-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev153-1
- Update to version 2.0.1.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev153-2
- Spec file cosmetics.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev153-1
- Update to latest snapshot.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev152-1
- Update to latest snapshot.

* Wed Aug 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev151-1
- Update to version 2.0.1.

* Sat Aug 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev150-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev149-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev148-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev148-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev147-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev146-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev144-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev143-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev142-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev141-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev140-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev139-1
- Update to latest snapshot.

* Tue Jul 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev138-1
- Update to latest snapshot.

* Mon Jul 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev137-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev136-2
- Update for packaging changes.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev131-1
- Update to latest snapshot.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev130-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev129-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev128-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev127-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev126-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev126-2
- Update for packaging changes.

* Sat May 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev126-1
- Update to latest snapshot.

* Mon May 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev125-3
- Update for packaging changes.

* Fri May 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev124-2
- Update for packaging changes.

* Fri May 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev124-1
- Initial package.



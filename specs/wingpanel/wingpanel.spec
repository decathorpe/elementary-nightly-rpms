Name:           wingpanel
Summary:        Stylish top panel
Version:        2.1.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  vala >= 0.24.0

BuildRequires:  pkgconfig(gala)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(granite)

Requires:       hicolor-icon-theme


%description
Stylish top panel that holds indicators and spawns an application
launcher.


%package        libs
Summary:        Stylish top panel (shared library)
%description    libs
Stylish top panel that holds indicators and spawns an application
launcher.

This package contains the shared library.


%package        devel
Summary:        Stylish top panel (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
Stylish top panel that holds indicators and spawns an application
launcher.

This package contains the files required for developing for wingpanel.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang wingpanel

# create plugin directory
mkdir -p %{buildroot}/%{_libdir}/wingpanel

# create settings directory
mkdir -p %{buildroot}/%{_sysconfdir}/wingpanel.d


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/wingpanel.desktop


%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig


%files -f wingpanel.lang
%{_bindir}/wingpanel

%{_libdir}/gala/plugins/libwingpanel-interface.so

%{_datadir}/applications/wingpanel.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/wingpanel.svg


%files libs
%license COPYING

%dir %{_sysconfdir}/wingpanel.d
%dir %{_libdir}/wingpanel

%{_libdir}/libwingpanel-2.0.so.0
%{_libdir}/libwingpanel-2.0.so.0.2.0


%files devel
%{_includedir}/wingpanel-2.0/

%{_libdir}/libwingpanel-2.0.so
%{_libdir}/pkgconfig/wingpanel-2.0.pc

%{_datadir}/vala/vapi/wingpanel-2.0.deps
%{_datadir}/vala/vapi/wingpanel-2.0.vapi


%changelog
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



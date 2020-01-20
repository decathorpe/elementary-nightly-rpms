%global srcname files
%global appname io.elementary.files

%global __provides_exclude_from ^%{_libdir}/(gtk-3.0)|(%{appname})/.*\\.so$

Name:           elementary-files
Summary:        File manager from elementary
Version:        4.3.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.34.0

BuildRequires:  pkgconfig(cloudproviders)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.29
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 5.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libcanberra) >= 0.30
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libnotify) >= 0.7.2
BuildRequires:  pkgconfig(pango) >= 1.1.2
BuildRequires:  pkgconfig(plank)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(unity) >= 4.0.0
BuildRequires:  pkgconfig(zeitgeist-2.0)

Provides:       pantheon-files
Obsoletes:      pantheon-files

%description
The simple, powerful, and sexy file manager from elementary.


%package        devel
Summary:        Pantheon file manager (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The simple, powerful, and sexy file manager from elementary.

This package contains the development headers.


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
%doc AUTHORS README.md
%license COPYING

%{_bindir}/%{appname}
%{_bindir}/%{appname}-daemon
%{_bindir}/%{appname}-pkexec

%{_libdir}/gtk-3.0/modules/libpantheon-filechooser-module.so
%{_libdir}/%{appname}/

%{_libdir}/libpantheon-files-core.so.4*
%{_libdir}/libpantheon-files-widgets.so.4*

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/dbus-1/services/%{appname}.Filemanager1.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/pixmaps/%{appname}/
%{_datadir}/polkit-1/actions/%{appname}.policy


%files devel
%{_includedir}/pantheon-files-widgets.h
%{_includedir}/pantheon-files-core/

%{_libdir}/libpantheon-files-core.so
%{_libdir}/libpantheon-files-widgets.so

%{_libdir}/pkgconfig/pantheon-files-core.pc
%{_libdir}/pkgconfig/pantheon-files-widgets.pc

%{_datadir}/vala/vapi/pantheon-files-core.vapi
%{_datadir}/vala/vapi/pantheon-files-widgets.vapi


%changelog
* Mon Jan 20 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200120.195537.73d61a6b-1
- Update to latest snapshot.

* Mon Jan 20 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200120.175526.9742a17c-1
- Update to latest snapshot.

* Mon Jan 20 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200120.134224.3daeb37c-1
- Update to latest snapshot.

* Mon Jan 20 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200120.123003.7f7fc106-1
- Update to latest snapshot.

* Sun Jan 19 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200119.103500.674e0a88-1
- Update to latest snapshot.

* Fri Jan 17 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200117.220753.074c1509-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200115.175932.6038ec35-1
- Update to latest snapshot.

* Mon Jan 13 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200113.160300.8235f632-1
- Update to latest snapshot.

* Sun Jan 12 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200112.120744.68d3f74e-1
- Update to latest snapshot.

* Fri Jan 10 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200110.140742.ac90956e-1
- Update to latest snapshot.

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 4.3.0+git200107.185325.6fa5e44d-1
- Update to version 4.3.0.

* Tue Jan 07 2020 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git200107.185325.6fa5e44d-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git200106.225338.c63cd461-1
- Update to latest snapshot.

* Fri Jan 03 2020 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git200103.170732.48214623-1
- Update to latest snapshot.

* Tue Dec 31 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191231.024036.4a34517b-1
- Update to latest snapshot.

* Sun Dec 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191229.104613.64a75881-1
- Update to latest snapshot.

* Sun Dec 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191229.071124.33e02571-1
- Update to latest snapshot.

* Fri Dec 27 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191227.132401.88efeb13-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191226.191723.c234abfd-1
- Update to latest snapshot.

* Thu Dec 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191226.165743.db8543b1-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191224.180807.87e70500-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191220.094315.a3047bec-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191219.073612.bead83a6-1
- Update to latest snapshot.

* Mon Dec 16 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191216.212907.4d42df9e-1
- Update to latest snapshot.

* Sat Dec 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191214.220704.0303c750-1
- Update to latest snapshot.

* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191213.200515.f6b4c79c-1
- Update to latest snapshot.

* Sun Dec 08 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191208.124810.d69e8d1f-1
- Update to latest snapshot.

* Fri Dec 06 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191206.172501.76d24be9-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191204.212520.fad3853d-1
- Update to latest snapshot.

* Tue Dec 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191203.113454.1180bc9e-1
- Update to latest snapshot.

* Mon Dec 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191202.142456.dbefee28-1
- Update to latest snapshot.

* Mon Dec 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191202.083944.499ff3d1-1
- Update to latest snapshot.

* Sun Dec 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191201.151007.22fb227f-1
- Update to latest snapshot.

* Fri Nov 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191129.182451.2053f7a3-1
- Update to latest snapshot.

* Fri Nov 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191129.104321.899a9c00-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191127.202449.8ad2e643-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191121.000500.aefa58ef-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191105.000257.41f5a0a0-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191104.235943.1ceba50b-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191104.201322.2057071f-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191104.192049.aa262e30-1
- Update to latest snapshot.

* Sat Nov 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191102.124637.16a96532-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191101.182359.747cdc49-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191031.181415.703de25c-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191029.233530.5b13cb21-1
- Update to latest snapshot.

* Tue Oct 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191029.192356.7a079c55-1
- Update to latest snapshot.

* Mon Oct 28 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191028.195746.ef93c748-1
- Update to latest snapshot.

* Mon Oct 28 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191028.165554.4525e4fa-1
- Update to latest snapshot.

* Sun Oct 27 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191027.192355.2243737d-1
- Update to latest snapshot.

* Thu Oct 24 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191023.154600.18da551b-2
- Add BR for libgit2-glib-1.0.pc.

* Wed Oct 23 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191023.154600.18da551b-1
- Update to latest snapshot.

* Tue Oct 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191022.184600.cd0902a5-1
- Update to latest snapshot.

* Tue Oct 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191022.155017.0666fbb7-1
- Update to latest snapshot.

* Mon Oct 21 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191021.223444.3e6d8c60-1
- Update to latest snapshot.

* Mon Oct 21 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191021.142345.57df6454-1
- Update to latest snapshot.

* Sat Oct 19 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191019.090316.d431ccab-1
- Update to latest snapshot.

* Fri Oct 18 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191018.195350.60cbe017-1
- Update to latest snapshot.

* Mon Oct 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191014.142335.866d3a68-1
- Update to latest snapshot.

* Sat Oct 12 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191012.142331.21f2f3a8-1
- Update to latest snapshot.

* Thu Oct 10 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191010.142327.d1cf562d-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191008.073133.5fe5709e-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191007.012323.7f270a7d-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191005.113609.fbee081b-1
- Update to latest snapshot.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191004.193114.f382079e-1
- Update to latest snapshot.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191004.161009.4f00d7b9-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191003.220157.76b5cc95-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191003.160531.5ff2a6c5-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191002.214658.25213790-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191001.163124.bbdac1f3-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git191001.154307.55592ce0-1
- Update to latest snapshot.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git190924.113211.6efd84b0-1
- Update to latest snapshot.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git190923.162304.1c243ba9-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git190920.192258.9aa0ffa9-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git190919.183744.b9744891-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git190919.173535.be0a54f3-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git190918.143056.ff975a1f-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git190916.104709.76107162-1
- Update to version 4.2.0.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190916.104709.76107162-1
- Update to latest snapshot.

* Sat Sep 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190914.122250.95bda632-1
- Update to latest snapshot.

* Sat Sep 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190914.102247.bb573936-1
- Update to latest snapshot.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190913.062248.e94f410a-1
- Update to latest snapshot.

* Tue Sep 10 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190910.011750.e36b02dc-1
- Update to latest snapshot.

* Tue Sep 10 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190910.005235.c3dbecaf-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190907.112236.6e9edc2e-1
- Update to latest snapshot.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190905.162238.7917af8b-1
- Update to latest snapshot.

* Wed Sep 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190904.224652.b3c82b9c-1
- Update to latest snapshot.

* Wed Sep 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190904.175111.56f9d774-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190902.202240.5fb8d13c-1
- Update to latest snapshot.

* Wed Aug 28 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190828.102219.178e5af5-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190826.042221.a8ea92ff-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190823.002212.ee6c2105-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190822.002211.264aad73-2
- Add BuildRequires: pkgconfig(cloudproviders).

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190822.002211.264aad73-1
- Update to latest snapshot.

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190820.042219.b26c85b3-1
- Update to latest snapshot.

* Mon Aug 19 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190819.101538.35b7661f-1
- Update to latest snapshot.

* Sat Aug 17 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190817.174634.a06e35ed-1
- Update to latest snapshot.

* Sat Aug 17 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190817.142203.b4784803-1
- Update to latest snapshot.

* Sat Aug 17 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190817.112203.1cfdb614-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190815.192202.68d97696-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190815.161046.d007e751-1
- Update to latest snapshot.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190814.175415.1d3fe5d9-1
- Update to latest snapshot.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190814.055524.7af18ad1-1
- Update to latest snapshot.

* Tue Aug 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190813.152159.2d6f55bf-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190801.162155.33555e44-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.9+git190731.084526.dc87cb88-1
- Update to version 4.1.9.

* Wed Jul 31 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190731.084526.dc87cb88-1
- Update to latest snapshot.

* Mon Jul 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190729.170221.9f6d6e24-1
- Update to latest snapshot.

* Sat Jul 27 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190726.235751.5defac6f-1
- Update to latest snapshot.

* Fri Jul 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190726.225710.175fc075-1
- Update to latest snapshot.

* Fri Jul 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190726.181136.16d17206-1
- Update to latest snapshot.

* Fri Jul 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190726.174308.14d0a5e6-1
- Update to latest snapshot.

* Fri Jul 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190726.145402.022985a3-1
- Update to latest snapshot.

* Thu Jul 25 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190725.212722.66956b89-1
- Update to latest snapshot.

* Thu Jul 25 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190725.122433.58e3fc75-1
- Update to latest snapshot.

* Mon Jul 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190722.012432.c5f6fa9d-1
- Update to latest snapshot.

* Sun Jul 21 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190721.000937.21b89af9-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190717.121842.a2c3ea59-1
- Update to latest snapshot.

* Mon Jul 15 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190715.185340.3019afec-1
- Update to latest snapshot.

* Sun Jul 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190714.202842.390ddfe4-1
- Update to latest snapshot.

* Sun Jul 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190714.002116.2169ae77-1
- Update to latest snapshot.

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190709.195459.93eb08d5-1
- Update to latest snapshot.

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190703.172849.36cd09c6-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190626.204259.1eee5d35-1
- Update to latest snapshot.

* Tue Jun 25 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190625.194349.9a6dfac2-1
- Update to latest snapshot.

* Mon Jun 24 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190624.202422.3711d524-1
- Update to latest snapshot.

* Thu Jun 20 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190620.190222.d471f331-1
- Update to latest snapshot.

* Mon Jun 17 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190617.104008.f8041303-1
- Update to latest snapshot.

* Sun Jun 16 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190616.181908.05a2a655-1
- Update to latest snapshot.

* Thu Jun 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190613.103603.18e6234f-1
- Update to latest snapshot.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190604.084636.f0b1f356-1
- Update to latest snapshot.

* Sat Jun 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190601.180600.46e39582-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190531.045745.9a46f3cf-1
- Update to latest snapshot.

* Thu May 30 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190526.172909.1dacf733-1
- Update to latest snapshot.

* Sat May 25 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190525.140326.b5a06bb8-1
- Update to latest snapshot.

* Thu May 23 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190523.121310.90157b56-1
- Update to latest snapshot.

* Thu May 23 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190523.091337.1e79003c-1
- Update to latest snapshot.

* Wed May 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190522.085544.f1dcd9f1-1
- Update to latest snapshot.

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190517.173900.c5785680-1
- Update to latest snapshot.

* Wed May 15 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190515.185437.1c869f64-1
- Update to latest snapshot.

* Mon May 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190513.131422.1d2a190a-1
- Update to latest snapshot.

* Tue May 07 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190507.154540.375f095f-1
- Update to latest snapshot.

* Fri May 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.8+git190502.204524.bfabe590-1
- Update to version 4.1.8.

* Thu May 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.7+git190502.204524.bfabe590-1
- Update to latest snapshot.

* Wed May 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.7+git190501.214341.45b3cd5e-1
- Update to latest snapshot.

* Sat Apr 20 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.7+git190420.183144.732d80c3-1
- Update to latest snapshot.

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.7+git190418.193719.9b6aa439-1
- Update to latest snapshot.

* Tue Apr 16 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.7+git190416.123139.da16dcdf-1
- Update to latest snapshot.

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.7+git190413.225328.15b0236d-1
- Update to latest snapshot.

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.7+git190411.225324.3b44c56b-1
- Update to version 4.1.7.

* Thu Apr 11 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6+git190411.225324.3b44c56b-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6+git190408.195301.48246d6d-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6+git190408.115313.0e2efec5-1
- Update to latest snapshot.

* Sun Apr 07 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6+git190407.165305.b740700f-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6+git190405.115210.5cd61527-1
- Update to latest snapshot.

* Thu Apr 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6+git190404.135212.fbc1edee-1
- Update to latest snapshot.

* Sun Mar 31 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6+git190331.225207.7629b75d-1
- Update to latest snapshot.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6+git190330.205200.1896524f-1
- Update to latest snapshot.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.6+git190330.034310.c166ae04-1
- Update to version 4.1.6.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190330.034310.c166ae04-1
- Update to latest snapshot.

* Fri Mar 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190329.025243.9f72db3e-1
- Update to latest snapshot.

* Tue Mar 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190326.165252.f21c665d-1
- Update to latest snapshot.

* Tue Mar 26 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190326.095849.961f539e-1
- Update to latest snapshot.

* Thu Mar 21 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190321.000608.b96a4e8e-1
- Update to latest snapshot.

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190318.134035.868814e6-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190312.152655.d5ee238a-1
- Update to latest snapshot.

* Mon Mar 11 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190311.200116.5ebe8c0d-1
- Update to latest snapshot.

* Mon Mar 11 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190311.150937.cc9926c4-1
- Update to latest snapshot.

* Mon Mar 11 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190311.145212.3aa98eb1-1
- Update to latest snapshot.

* Sat Mar 09 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190309.205511.706a86cc-1
- Update to latest snapshot.

* Wed Mar 06 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190306.182649.06bb7465-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190305.174753.40e2fbda-1
- Update to latest snapshot.

* Mon Mar 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190304.151431.ea86bf78-1
- Update to latest snapshot.

* Sun Mar 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190303.142637.3556bde8-1
- Update to latest snapshot.

* Thu Feb 28 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190228.222635.e89d6070-1
- Update to latest snapshot.

* Thu Feb 28 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190228.121334.7888a730-1
- Update to latest snapshot.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190222.000432.13e81776-1
- Update to latest snapshot.

* Thu Feb 21 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190221.180702.c0a6f593-1
- Update to latest snapshot.

* Thu Feb 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.5+git190213.235357.14ab6db4-1
- Update to version 4.1.5.

* Thu Feb 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.4+git190213.235357.14ab6db4-1
- Update to latest snapshot.

* Sat Feb 09 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.4+git190209.111246.e2c5b278-1
- Update to latest snapshot.

* Sun Feb 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.4+git190203.200643.32269921-1
- Update to latest snapshot.

* Sun Feb 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.4+git190203.163650.01c349df-1
- Update to latest snapshot.

* Sun Feb 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.4+git190203.115530.74bae870-1
- Update to latest snapshot.

* Sun Feb 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.4+git190203.103012.7d613af3-1
- Update to latest snapshot.

* Thu Jan 31 2019 Fabio Valentini <decathorpe@gmail.com> - 4.1.4+git190131.133534.4341a5f2-1
- Update to version 4.1.4.

* Thu Jan 31 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190131.133534.4341a5f2-1
- Update to latest snapshot.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190129.083926.3b54d676-1
- Update to latest snapshot.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190129.003432.adea87d9-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190128.135043.261dd245-1
- Update to latest snapshot.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190128.081043.50e5eb12-2
- Adapt to renamed polkit policy file.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190128.081043.50e5eb12-1
- Update to latest snapshot.

* Sun Jan 27 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190127.151325.81792176-1
- Update to latest snapshot.

* Sun Jan 27 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190127.122741.6875d432-1
- Update to latest snapshot.

* Sun Jan 27 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190127.000104.668aac65-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190125.213421.fe7a2c10-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190125.184035.0b5ccad7-1
- Update to latest snapshot.

* Thu Jan 24 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190124.091637.edee9887-1
- Update to latest snapshot.

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190123.180444.59c3eb3f-1
- Update to latest snapshot.

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190123.093518.7a6032e6-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190122.161422.a6ad707e-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190122.155109.67c7d5ab-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190122.112108.e09254c0-1
- Update to latest snapshot.

* Sun Jan 20 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190120.165122.378bc9e2-1
- Update to latest snapshot.

* Fri Jan 18 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190118.050016.5847f814-1
- Update to latest snapshot.

* Wed Jan 16 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190116.000330.4e76c31b-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190115.125314.612a8892-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190114.162816.d7162c64-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190114.094206.2b97e861-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190114.000841.951872f5-1
- Update to latest snapshot.

* Sun Jan 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190113.093242.67c4744d-1
- Update to latest snapshot.

* Sat Jan 12 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190112.134113.9f21a880-1
- Update to latest snapshot.

* Sat Jan 12 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190112.000902.78689451-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190111.205150.0a7b7a2a-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190111.131137.bbac8654-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190111.085607.d80ba1d7-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190111.005611.e2680f48-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190110.113125.0205e198-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190109.230353.15e32037-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190109.204032.36c122b6-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190109.152228.075e79e9-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190109.134221.4e4ffb2c-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190109.000604.03a9c694-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190108.235441.d473b01d-1
- Update to latest snapshot.

* Tue Jan 08 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190108.161433.7f75e2be-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190107.181847.8f1606ff-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190107.000250.70508674-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190106.162211.cec82988-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190105.022035.93f5a913-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190105.005406.5f8ea721-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190104.000808.5a65e33d-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190102.192335.08e2084f-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190102.183919.8e858b7c-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190102.103257.29d5d715-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190102.060523.7b03652e-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190102.000619.d65453e5-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190101.200224.c8247989-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190101.155213.46131c8b-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0+git190101.004446.148a277c-1
- Update to latest snapshot.

* Mon Dec 31 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181231.132251.d82bf967-1
- Update to latest snapshot.

* Sun Dec 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181230.000415.046f2955-1
- Update to latest snapshot.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181229.201648.5eadcf63-1
- Update to latest snapshot.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181229.183327.ea1b7953-1
- Update to latest snapshot.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181229.000106.03bf9692-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181228.203415.0ca65ae0-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181228.190237.cdf96893-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181228.175216.ec9e7e36-1
- Update to latest snapshot.

* Thu Dec 27 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181227.183152.b2a92948-1
- Update to latest snapshot.

* Tue Dec 25 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181225.000621.79c16aa2-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181224.105638.c38941bb-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181224.000641.5cf3ed81-1
- Update to latest snapshot.

* Sun Dec 23 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181223.000659.bfee544f-1
- Update to latest snapshot.

* Sat Dec 22 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181222.104909.85019e6c-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181221.192730.77670539-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181221.082200.d19d2fbd-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181221.015713.1ed21bfc-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181221.000023.f582d2eb-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181220.215008.dd333e00-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181220.191056.8b26b203-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181220.185006.e6848d57-1
- Update to latest snapshot.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181220.001032.e3c81940-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181219.150436.1a458051-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181219.150021.f21951f6-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181219.115950.772b34cd-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181219.094800.d31b597f-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181219.082540.4c4029e5-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181219.035057.62f480ba-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181218.172059.c94810f2-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181217.000938.a1740f82-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181215.121329.10abbbec-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181215.110408.8477889e-1
- Update to latest snapshot.

* Fri Dec 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181214.000802.767b62cc-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181213.143919.e7e4c596-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181213.111944.e21894e1-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181210.202229.964be688-1
- Update to latest snapshot.

* Sun Dec 09 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181209.000111.32a38658-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181208.211951.a5f036b3-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181203.174948.a661722c-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181202.200454.6fc9b0a7-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181202.062413.50ee00b3-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181130.163222.64a8bbe5-1
- Update to latest snapshot.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181129.204936.816cf8c2-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181128.082506.86192511-2
- Adapt to upstream file changes.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181128.082506.86192511-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181127.174816.3c57bea8-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181126.102958.0e523cc4-3
- Adapt to upstream file changes.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181126.102958.0e523cc4-2
- Adapt to upstream file changes.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181126.102958.0e523cc4-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181126.065524.c2b5adb8-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181126.000547.d3335623-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181124.000942.c925d04a-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181123.182131.8efd7d62-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181123.172954.60c3ab20-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181123.000154.d58c7147-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181122.195846.6dff9576-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181122.160613.495d1077-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181121.201744.31936a57-2
- Adapt to upstream file changes.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181121.201744.31936a57-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181121.182456.47ed65a0-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181120.205142.52581899-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181120.164434.48d4ed00-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181120.114004.c87a1a2a-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181119.192734.bab8a12f-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181119.185406.d2342ff0-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181116.083930.00185684-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181115.174452.4f594e0a-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181115.164517.5c52229d-1
- Update to latest snapshot.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181114.095601.3012758d-2
- Adapt to CMake -> meson switch.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181114.095601.3012758d-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181113.001014.3e25171d-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181112.180633.049b5af0-1
- Update to latest snapshot.

* Sun Nov 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181111.000816.8810e82d-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181110.155407.a6ccc8ee-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181107.012117.0819a73e-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181107.000643.a555f1c4-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181106.190109.62b660fd-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181105.000927.21bd8a65-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181104.000306.a7679907-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181103.201657.64bfcf7c-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181103.164426.43171059-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181103.150149.2b668bbd-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181102.174511.cef63d5d-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181102.155655.9ca0deab-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181102.145552.e638c5be-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181102.134947.79223bc6-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181102.134947.79223bc6-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181102.084033.e7f5cd1d-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181102.015604.f0ea762f-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181101.232327.d5cf5685-1
- Update to latest snapshot.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181101.011450.c10a9b97-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181030.222154.6d95d200-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181030.163615.e5bd28cb-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181030.150858.69dfa947-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181030.145737.de19e1d6-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181030.091422.f2a328b9-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181030.060522.5d69c15b-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181030.025928.1f89b32e-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181030.014730.63b9954f-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181030.000038.7a5fd133-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181029.154541.fb31e1b2-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181028.114257.1c431baa-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181028.000603.67fb34ac-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181027.230431.1492d22c-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181026.125333.a8418d57-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181026.000340.c0eb373b-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181025.163915.2c872ebc-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181025.073712.b150793d-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181024.160749.38334084-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181023.123845.5369ba29-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181023.000308.7235868c-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181022.000342.0e774bc9-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181021.090130.03e6537a-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181021.000721.f84cbd70-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181020.000336.b09cdaeb-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181019.184841.9412a0d2-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181019.000751.f883c88b-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0+git181018.000943.9af8cbdb-1
- Update to version 4.0.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181018.000943.9af8cbdb-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181017.000630.6b3ba394-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181016.095113.f4c037db-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181016.000306.9ba0de8e-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181015.175638.20c5ebd2-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181015.000535.e83e6d6a-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181014.164535.6b0a6f07-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181014.154444.556282cd-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181014.112826.929c1f78-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181013.172102.db75a7a5-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181013.163913.58facd54-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181013.000018.018eb758-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181012.155615.6934def4-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181012.000505.38ff1739-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181011.164141.9ef0d911-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181011.015118.6dd887b3-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181011.000621.3e2274b4-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181009.000043.62c93edf-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181009.000037.2fef722e-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181008.150046.d4fd34c6-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181008.143016.b48ee7b4-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181008.000421.d7d64e8d-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181003.162453.edce30e3-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181003.143153.2505b42b-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181003.001043.b4312340-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181002.091734.5baedf4f-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git181002.000352.b8ef9bfa-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180930.000940.35e955c9-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180929.000915.25a42aa8-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180928.000703.23c17dc4-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180927.001004.4c4cedb9-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180926.061244.0a4750e5-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180926.000219.39a20404-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180925.134453.86921755-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180925.000200.7130cd0f-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180924.070431.8087a1ad-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180924.000509.7ea70511-1
- Update to latest snapshot.

* Sun Sep 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180923.105317.5e077335-1
- Update to latest snapshot.

* Sun Sep 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180923.000619.e9865664-1
- Update to latest snapshot.

* Sat Sep 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180922.091333.3bb8fa49-1
- Update to latest snapshot.

* Sat Sep 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180922.022418.7332564e-1
- Update to latest snapshot.

* Sat Sep 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180922.005731.551fd9d0-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180921.183928.1b3b4629-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180921.173424.ada815c2-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180921.164225.aba361bc-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180920.172947.f948a279-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180919.070807.f7bff19f-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180919.000845.3ba98531-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180918.220509.4a19f77e-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180905.224301.27df27c1-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180905.000047.81b8a44f-1
- Update to latest snapshot.

* Tue Sep 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180904.201103.40c69be9-1
- Update to latest snapshot.

* Mon Sep 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180903.000246.4b46b30a-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180901.000727.d1d3974f-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180831.125528.b783704e-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180830.000316.5f31a309-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180829.171513.f93d3118-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180829.161023.261d9987-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180829.151320.4f795061-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180829.060044.1605b864-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180826.000429.39b673c5-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180822.200453.667b0951-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180821.163318.e86b0560-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180819.000239.5954660b-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180818.135620.a1499011-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180815.165716.bcec2449-2
- Occasional mass rebuild.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180815.165716.bcec2449-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180814.182820.38df4879-1
- Update to latest snapshot.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180813.203703.8e53ad72-1
- Update to latest snapshot.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180813.000308.f1e64d40-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180812.195832.d839ee99-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180812.121859.4bee5e4c-1
- Update to latest snapshot.

* Fri Aug 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180810.000743.e2308d88-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180808.000141.86bdb0c4-1
- Update to latest snapshot.

* Sun Aug 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180805.033458.a1475450-1
- Update to latest snapshot.

* Sat Aug 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180804.134749.04d8f867-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180803.181331.f8e18d23-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180803.170919.632e6f34-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180803.000405.fd4f30e2-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180802.154229.152cfbca-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180802.000104.1d320490-1
- Update to latest snapshot.

* Wed Aug 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180801.183626.482d993d-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180730.000725.204cfdf8-1
- Update to latest snapshot.

* Sat Jul 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180728.005550.3fb9157b-1
- Update to latest snapshot.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180727.114652.19451191-1
- Update to latest snapshot.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180727.061731.7d09d7ef-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180726.212626.d428e29a-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180726.161128.c585b907-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180726.142412.e17ecee9-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180726.122931.a509ba06-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180726.062710.9b8a97ee-1
- Update to latest snapshot.

* Wed Jul 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180725.195716.9e498235-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180722.000332.475dd854-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180721.123308.5972a147-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180721.000721.fb84117a-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180720.092205.85bf1542-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180717.202258.5a34ded5-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180717.184745.d8fc3039-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180717.133353.e561be23-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180717.112849.b3056fc7-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180717.063435.cafdc891-1
- Update to latest snapshot.

* Mon Jul 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180716.000354.a10c2cea-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180715.001006.a7b73167-1
- Update to latest snapshot.

* Sat Jul 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180714.000405.c16faeb3-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180713.000344.40a6a127-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180711.000844.aa42aee6-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180709.001017.04d7bb94-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180705.125247.da5a2bb3-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180703.000604.b2342f4b-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180615.000041.9785e68a-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180614.023420.3a8983cc-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180613.000712.59399dca-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180612.061502.219164b1-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180611.194224.2f7cd057-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180611.183116.f7b23818-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180610.154713.7c9cf111-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180610.001125.319e2b9c-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180608.001139.a243922e-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180607.000905.ea750f1a-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180606.000827.8ed5a93f-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180605.004029.71a09e25-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180604.000848.c203d79d-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180603.064815.6d36c1d8-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180602.192150.398dcb8a-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180602.160207.2ed7bd4e-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180602.011635.481c5814-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180601.163845.b29748e2-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180601.000715.361d0f2b-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180531.000223.d8b82118-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180530.125715.97bcddc4-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180530.091728.67524a54-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180529.134005.d96277c8-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180528.093854.df33b1da-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180528.000035.c76f01fd-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180527.091253.48572692-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180525.222952.f9e2b4df-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180524.155638.c6fb4c82-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180518.000720.e44a0e5f-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180515.173433.2950ae9f-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180513.221801.ecfeb272-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180512.000240.1334c4b9-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180511.101029.16587420-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180511.094814.42e17f65-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180511.055226.64252e30-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180510.171517.8042badc-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180510.115634.21f81806-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180510.000855.d219795d-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180509.143136.433d5824-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180508.182518.44c8e49d-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180508.143025.94feb0d8-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180507.175319.c3e40a22-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180507.000235.de34dd6a-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180505.001029.1c3cc11c-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180503.174827.3ae8c272-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180503.165744.a76dfcc1-1
- Update to latest snapshot.

* Wed May 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180502.181326.76da6ca1-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180501.000326.ddd79748-2
- Fix bogus changelog dates.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180421.165835.f61d26c6-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180421.001057.74b8c888-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180420.165621.dd490bd4-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180420.001132.7b75433d-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180413.180300.ee9f9fd0-1
- Update to latest snapshot.

* Thu Apr 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180412.164505.138dd28b-1
- Update to latest snapshot.

* Wed Apr 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180411.192641.2a2956fb-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180410.190608.fccfa34f-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180410.175649.054291d3-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180410.085903.9cc80804-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180404.211441.393e726a-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180401.092955.cfe80985-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180328.183611.1409f029-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180327.175037.e1f30613-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180327.000154.3cb86e1a-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180326.000844.9974320e-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180325.182528.d6a78d0d-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180322.215431.66d7d37f-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180321.203955.82b5647c-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180321.014843.37eec518-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180320.035526.4b07cd27-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180319.205928.0a025b01-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180319.182633.9c1bec60-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180319.094901.7542e769-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180318.012205.c434ef95-2
- Adapt to upstream file changes.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180318.012205.c434ef95-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180316.000347.1c84ea9c-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180314.000210.4ecd1eb3-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180312.004723.d3d34317-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180310.000347.e2056d65-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180309.112333.ccb71951-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180307.000940.cd195430-2
- Adapt to upstream file changes.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180307.000940.cd195430-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180305.171632.35e2e890-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180228.105717.893872c5-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180222.000807.571556c5-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180217.193046.43d16f21-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180217.183017.d82a4e74-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180216.195606.7f7a88f9-1
- Update to latest snapshot.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180215.000105.57089717-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180214.174649.724e3ffa-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180213.093014.a3cc3db4-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180210.173952.e7b108ea-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180209.000233.9f83c54b-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180208.220536.dae8895e-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180208.091554.a9329380-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180205.001109.df7f56d3-1
- Update to latest snapshot.

* Thu Feb 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180201.000905.20d0fb9e-1
- Update to latest snapshot.

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180130.180731.16a545ee-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180129.000213.3955ab26-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180127.230240.087bef40-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180127.211145.935bd662-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180127.000247.34dd9845-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180126.172006.33b40939-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180125.183753.39e4e386-2
- Be lazy about undefined symbols in plugins.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180125.183753.39e4e386-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180124.171932.982a30cb-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180124.000352.d17099fe-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180123.172756.6c046866-1
- Update to latest snapshot.

* Sun Jan 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180121.000519.d93398b1-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180120.114454.d631383f-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180119.194807.d569ae2d-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180119.183832.aed6bc92-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180119.100436.c59ced2b-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180113.201114.b657781e-1
- Update to latest snapshot.

* Thu Jan 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180111.175854.cba1186c-1
- Update to latest snapshot.

* Thu Jan 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180111.103557.64389f27-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180110.000139.29695198-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180109.180210.93df5413-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180109.173424.8e59915b-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git171231.000534.edfb165e-1
- Initial package.



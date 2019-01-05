%global srcname calendar
%global appname io.elementary.calendar

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-calendar
Summary:        Desktop calendar app from elementary
Version:        4.2.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libecal-1.2) >= 3.8.0
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libnotify)

# elementary-calendar also provides a generic symbolic icon (actions/calendar-go-today)
Requires:       hicolor-icon-theme

# calendar requires the gsettings key from the datetime wingpanel indicator
Requires:       wingpanel-indicator-datetime

Provides:       maya-calendar
Obsoletes:      maya-calendar


%description
A slim, lightweight GTK+3 calendar app written in Vala, designed for
elementary OS. Also looks and works great on other GTK+ desktops.


%package        devel
Summary:        The official elementary calendar (devel files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
A slim, lightweight GTK+3 calendar app written in Vala, designed for
elementary OS. Also looks and works great on other GTK+ desktops.

This package contains the development files.


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
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop || :

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop || :

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

%{_bindir}/%{appname}

%{_libexecdir}/%{appname}-daemon

%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.1
%{_libdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%files devel
%{_includedir}/%{name}/

%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%{_datadir}/vala/vapi/%{name}.deps
%{_datadir}/vala/vapi/%{name}.vapi


%changelog
* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190105.121448.5083f96a-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190103.214912.986d26dc-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190103.191344.c32c0c20-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190103.183624.cb2f73e3-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190103.093549.e44a82c1-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190102.201423.f605614a-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190102.193811.2a687085-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190102.180229.4b788bf2-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190101.184123.6071f4bb-1
- Update to latest snapshot.

* Tue Jan 01 2019 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git190101.003332.b4b9ed94-1
- Update to latest snapshot.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181229.012045.e02d5e78-1
- Update to latest snapshot.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181229.004335.74c9e41c-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181228.124139.52c9da81-1
- Update to latest snapshot.

* Thu Dec 27 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181227.191110.99731e27-1
- Update to latest snapshot.

* Tue Dec 25 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181225.000604.f3588871-1
- Update to latest snapshot.

* Sat Dec 22 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181222.103318.9bf61be3-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181221.015648.2785c50a-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181219.110455.d416c6fd-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181218.234320.32b1da5f-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181218.204325.6c7730b6-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181218.185949.df83f735-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181218.104429.347bf161-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181218.012448.21078307-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181217.205842.126dc578-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181217.105024.029ac51a-1
- Update to latest snapshot.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181216.190823.c4cd0930-1
- Update to latest snapshot.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181216.000154.cab4f502-1
- Update to latest snapshot.

* Fri Dec 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181214.191524.f92d8c42-1
- Update to latest snapshot.

* Fri Dec 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181214.180426.b8c4d3e4-1
- Update to latest snapshot.

* Fri Dec 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181214.174927.eb11d134-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181213.220415.9f5ff908-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181213.211211.b79b5b27-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181213.195932.bf88539a-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181213.162222.da0deb91-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181213.145957.7274a246-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181212.233757.af38053c-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181212.184900.152280a4-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181212.164332.7576cfc7-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181212.084925.04a8ef86-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181212.075108.398ba098-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181212.050826.0f5bc989-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181212.002805.5acdd536-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181211.230549.67fbef6d-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181211.213433.4d66c0b5-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181211.204729.bee32498-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181211.173850.ba35a41d-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181211.145251.710fd8d9-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181211.120704.b402c134-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181211.065922.c0191e29-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181211.020811.de0dc2f9-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181211.004404.addfb955-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181210.235549.85ab39ac-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181210.210325.55becb33-1
- Update to latest snapshot.

* Sun Dec 09 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181209.000057.9de66c59-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181202.061804.46d99adb-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181124.000954.58cd0ca7-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181121.130034.9079dc42-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181121.091930.26231721-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181119.000653.da119f46-2
- Add Requires: wingpanel-indicator-datetime.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181119.000653.da119f46-1
- Update to latest snapshot.

* Sun Nov 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181118.193246.25cc2214-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181117.000142.37366ede-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181116.221316.e5cb9fb8-1
- Update to latest snapshot.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181114.002012.63203abf-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181113.220851.1b027d1f-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181113.064123.546e837c-2
- Bump granite dependency to >= 5.2.0.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181113.064123.546e837c-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181112.024015.86a416b0-1
- Update to latest snapshot.

* Sun Nov 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181111.164056.f7a412bc-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181103.225132.9316ebb3-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181102.194638.b1cfee5c-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181102.174734.14531321-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181102.163500.8b47cc2b-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181030.000427.f3977891-2
- Occasional mass rebuild.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181030.000427.f3977891-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181026.074258.8ed166aa-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181025.070855.c4be3f6e-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181024.113724.7d046b05-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181023.000251.e9f6fefb-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181022.000252.1d3ebcec-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181021.121610.f3d67ae5-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181021.115143.05c4da34-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181019.221240.b5eaa967-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181019.190448.f6f9a11d-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181019.165907.49e05eb5-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181018.120236.51b07efa-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181018.115900.02b08441-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181018.070343.93eac74a-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181017.000615.c12997dd-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181016.194825.16d2c1af-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3+git181016.175556.f63a3821-1
- Update to version 4.2.3.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181016.175556.f63a3821-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181016.135219.20b21903-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181016.124949.c1ef011f-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181016.104238.55b60fcf-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181016.094459.a4294ef9-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181015.105247.ca16c450-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181012.171018.2475e7fb-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181012.000440.b3c69971-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181011.133644.94ee58a1-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181010.000206.b417edf0-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181008.200153.66b0baa8-2
- Adapt to dependency changes.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181008.200153.66b0baa8-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181008.000401.5590652b-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181007.024358.33737caf-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181005.211601.01fb4ce7-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181005.205513.62ff0b2a-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181005.170207.196bae9e-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2+git181003.081705.f4147134-1
- Update to version 4.2.2.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git181003.081705.f4147134-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git181003.001024.ce5e0fa6-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180930.203719.88a9c4e1-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180927.053902.5c28802f-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180926.212201.ecbfbc77-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180921.000611.9e754ecb-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180920.112736.ade08742-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180920.000406.693d3209-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180919.000830.8c2e6197-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180917.143805.29bdc640-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180906.022335.10e1728c-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180905.191609.6a32d06c-2
- Adapt to upstream file changes.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180905.191609.6a32d06c-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180901.000800.403a4376-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180830.151904.1a58bdad-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180830.000641.ceb4a167-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180829.193855.00844aca-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180829.034833.3c4cb976-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180827.000757.f0c47d06-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180822.000831.b8410c14-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180820.000623.6258ed82-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180818.113335.11b16b98-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180816.150016.984a04f8-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180813.000237.a1ac3bb2-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180813.000237.a1ac3bb2-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180803.000340.497a569e-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180801.201412.11f1b0bb-1
- Update to latest snapshot.

* Sat Jul 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180728.115637.92bd471c-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180726.192707.9c156d39-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180724.030535.dcd02192-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180722.000317.b6f1b2d8-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180721.111125.dcb72b85-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180721.104829.8e8e84e5-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180721.000659.7ec952ee-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180720.193634.39275d28-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180720.110715.b751b529-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180720.000640.4beee93a-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180719.000717.2340f134-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180718.000531.2cda4812-1
- Update to latest snapshot.

* Mon Jul 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180716.085921.c4023353-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180715.000952.f363c29e-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180713.172541.5f4ce522-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180712.213938.17f5e8c7-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180712.172152.d621fb14-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180712.124048.a423b930-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180712.102324.92f1bb13-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180712.095804.01a1daee-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180712.075956.d5dd07b7-2
- Adapt to CMake -> meson switch.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180712.075956.d5dd07b7-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180711.000831.714f1dbe-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180710.000316.3a01436f-1
- Update to latest snapshot.

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1+git180703.000553.f171748c-1
- Update to version 0.4.2.1.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180703.000553.f171748c-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180613.000639.1a5b7b1f-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180611.141020.a35c33c1-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180610.001054.b3ecdb10-1
- Update to version 0.4.2.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180610.001054.b3ecdb10-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180608.001103.9c1b8db4-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180607.000842.39980c34-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180606.090454.6b3aa6f2-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180606.000748.2dcd4574-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180604.000821.73dd709f-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180602.000422.7bbe67fc-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180601.000646.b2ce4baa-2
- Adapt to upstream file changes.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180601.000646.b2ce4baa-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180531.001609.6d0dd544-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180529.094358.e6b6136a-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180528.000212.d048de9d-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180527.000433.5f26b83d-2
- Adapt to upstream file changes.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180527.000433.5f26b83d-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180525.200944.36924234-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180512.114236.a6618ed1-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180512.001046.280a4d9f-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180511.000534.470dc177-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180507.000214.343f2ba6-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180506.000930.e2fbfd9c-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180501.124238.38ac20f8-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180501.101351.e842b66b-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180430.184613.b55e6ebe-1
- Update to latest snapshot.

* Mon Apr 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180423.000918.c0e1a1de-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180420.181014.a820e08c-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180420.001105.8d053678-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180322.183805.f86347ae-2
- Adapt to upstream file changes.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180322.183805.f86347ae-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180320.001106.fce14afd-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180318.000758.9963bc7c-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180316.000135.9753182b-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180306.185646.c47dec04-2
- Adapt to upstream file changes.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180306.185646.c47dec04-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180305.200209.e03204ba-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180228.000732.56ab3464-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180227.081048.174f147d-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180220.210223.5dec77cf-1
- Initial package.



%global srcname greeter
%global appname io.elementary.%{srcname}

Name:           elementary-greeter
Summary:        LightDM Login Screen for the elementary desktop
Version:        3.3.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz
Source1:        40-%{appname}.conf
Source2:        %{appname}.whitelist

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(x11)

%if 0%{?fedora} < 28
BuildRequires:  pkgconfig(mutter-clutter-1)
BuildRequires:  pkgconfig(mutter-cogl-1)
BuildRequires:  pkgconfig(mutter-cogl-pango-1)
BuildRequires:  pkgconfig(mutter-cogl-path-1)
%else
BuildRequires:  pkgconfig(mutter-clutter-2)
BuildRequires:  pkgconfig(mutter-cogl-2)
BuildRequires:  pkgconfig(mutter-cogl-pango-2)
BuildRequires:  pkgconfig(mutter-cogl-path-2)
%endif

Provides:       pantheon-greeter = %{version}-%{release}
Obsoletes:      pantheon-greeter


Requires:       lightdm%{?_isa}
Requires:       wingpanel%{?_isa}

# Raleway font is used for interface elements
Requires:       impallari-raleway-fonts

# Runtime requirement for numlock capture
Requires:       numlockx

# Requirements for default artwork
Requires:       elementary-icon-theme
Requires:       elementary-theme-gtk3
Requires:       elementary-wallpapers


# All LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

# Alternate, more descriptive names
Provides:       lightdm-%{name} = %{version}-%{release}
Provides:       lightdm-%{name}%{?_isa} = %{version}-%{release}


%description
The elementary Greeter is a styled Login Screen for LightDM.


%prep
%autosetup -p1


%build
%meson -Dubuntu-patched-gsd=false
%meson_build


%install
%meson_install

%find_lang %{appname}

# Install LightDM configuration file
mkdir -p %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d
install -pm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/

# Install wingpanel overrides for the greeter
mkdir -p %{buildroot}%{_sysconfdir}/wingpanel.d
install -pm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/wingpanel.d


%files -f %{appname}.lang
%license LICENSE

%config(noreplace) %{_sysconfdir}/lightdm/%{appname}.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf.d/40-%{appname}.conf
%config(noreplace) %{_sysconfdir}/wingpanel.d/%{appname}.whitelist

%{_bindir}/%{appname}-compositor

%{_sbindir}/%{appname}

%{_datadir}/xgreeters/%{appname}.desktop


%changelog
* Thu Mar 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190328.180539.897c0737-1
- Update to latest snapshot.

* Thu Mar 21 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190321.092921.36b34fb9-1
- Update to latest snapshot.

* Thu Mar 21 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190320.234824.dc1a219a-1
- Update to latest snapshot.

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190318.102941.00478390-1
- Update to latest snapshot.

* Sun Mar 17 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190317.170150.82f5cc28-1
- Update to latest snapshot.

* Sat Mar 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190316.212709.3161675d-1
- Update to latest snapshot.

* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190313.193530.637bc355-2
- Add dependencies on the default theme and artwork.

* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190313.193530.637bc355-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190312.212654.352539cf-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190307.065640.1617ee20-1
- Update to latest snapshot.

* Thu Jan 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190131.215234.15a69aca-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190109.000540.61d72136-1
- Update to latest snapshot.

* Sat Jan 05 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190105.003922.58bd2d29-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190104.000755.15087039-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190103.000416.d83d4e25-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190102.190808.c61a7e5d-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190102.185030.ccfce043-1
- Update to latest snapshot.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181229.000059.1d9d995d-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181218.202524.7f36454d-2
- Remove unnecessary patch which might actually break things now.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181218.202524.7f36454d-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181218.163217.961fc4c3-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181213.144614.df3d94e7-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181212.000720.ebf9a3c3-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181211.070214.ee7e3955-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181210.195848.04c8b2be-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181208.000436.84cae4c8-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181207.052456.34fca809-1
- Update to latest snapshot.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181129.120801.ee470266-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181128.141436.2e651ac8-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181122.082822.6b166a5f-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181122.000217.751da95e-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181120.143725.4a8ae6ee-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181120.121359.c1c97fde-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181119.171525.64f25a0b-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181119.111948.13bde710-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181119.082601.ad9650d0-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181119.000705.4057ad08-1
- Update to latest snapshot.

* Sun Nov 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181118.011325.e79a97b5-1
- Update to latest snapshot.

* Sun Nov 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181118.000717.19b9ed89-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181117.224329.7bbb6a38-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181117.211806.3c8ada43-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181117.180009.da450d89-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181117.115056.b93c9d4a-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181117.100814.c1be3c43-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181117.095746.4e9324cb-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181117.090055.21388589-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181116.223428.25b80ac9-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181116.202649.79289688-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181114.234526.fd36f26b-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git181106.180405.767bbcdc-1
- Update to version 3.3.1.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.0+git181106.180405.767bbcdc-2
- Remove upstreamed patch.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.0+git181106.180405.767bbcdc-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.0+git181105.220552.f7813437-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.0+git181104.193444.3b98a9f9-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.0+git181104.000318.b4eda4b8-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.0+git181029.152158.270afdfe-2
- Occasional mass rebuild.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 3.3.0+git181029.152158.270afdfe-1
- Update to version 3.3.0.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181029.152158.270afdfe-3
- More gnome-settings-daemon and gsettings fixes.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181029.152158.270afdfe-2
- Try to fix brokenness around g-s-d.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181029.152158.270afdfe-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181029.000950.a8fcc9c4-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181028.000546.de2dbace-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181026.000445.94fd91d4-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181025.071312.8a257d58-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181024.170958.795b2723-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181022.000325.25584773-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181019.000736.3d1d73f8-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181017.182232.cbfbca98-2
- Renamed package from pantheon-greeter.


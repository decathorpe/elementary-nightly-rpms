%global srcname greeter
%global appname io.elementary.%{srcname}

Name:           elementary-greeter
Summary:        LightDM Login Screen for the elementary desktop
Version:        5.0.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz
Source1:        40-%{appname}.conf
Source2:        %{appname}.whitelist

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite) >= 5.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(mutter-clutter-2)
BuildRequires:  pkgconfig(mutter-cogl-2)
BuildRequires:  pkgconfig(mutter-cogl-pango-2)
BuildRequires:  pkgconfig(mutter-cogl-path-2)
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(x11)

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


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license LICENSE

%config(noreplace) %{_sysconfdir}/lightdm/%{appname}.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf.d/40-%{appname}.conf
%config(noreplace) %{_sysconfdir}/wingpanel.d/%{appname}.whitelist

%{_bindir}/%{appname}-compositor

%{_sbindir}/%{appname}

%{_datadir}/xgreeters/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Tue Nov 12 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git191112.140634.15c80e45-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git191111.122414.ca897682-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git191109.122412.66771ade-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git191107.102409.201340f1-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git191106.004005.ff679351-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git191105.202410.8be2b866-1
- Update to latest snapshot.

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git191103.002405.d87b97bf-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git191031.211021.467f91a9-1
- Update to version 5.0.1.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191031.211021.467f91a9-1
- Update to latest snapshot.

* Thu Oct 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191031.204440.40671285-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191030.201346.cbcd391c-1
- Update to latest snapshot.

* Tue Oct 29 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191029.153644.081d411a-1
- Update to latest snapshot.

* Sun Oct 27 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191027.092349.88a2eee1-1
- Update to latest snapshot.

* Wed Oct 23 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191023.184819.9eeb0fe3-1
- Update to latest snapshot.

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191016.002317.64ff62e6-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191009.074716.fe1b1ad0-1
- Update to latest snapshot.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191008.073848.a728a84d-1
- Update to latest snapshot.

* Sun Oct 06 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191006.142317.6f26076a-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191005.032315.bcdef7f9-1
- Update to latest snapshot.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191004.025031.cb3b95e2-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191003.154528.bbebcf5e-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191002.161036.58d9b05c-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191001.221113.29590dc9-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git191001.203251.170355bd-1
- Update to latest snapshot.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190923.223739.6f42e810-1
- Update to latest snapshot.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190923.213709.511b020e-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190919.182655.4c75aa1b-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190919.173621.89502ac5-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190918.162253.0ec583a3-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190916.162246.3e12382f-1
- Update to latest snapshot.

* Tue Sep 10 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190910.222239.cad7d28d-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190907.212232.dd311734-1
- Update to latest snapshot.

* Wed Sep 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190904.210213.a53000fd-1
- Update to latest snapshot.

* Tue Sep 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190903.202230.8c432576-1
- Update to latest snapshot.

* Tue Sep 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190903.172403.f9593b5c-1
- Update to latest snapshot.

* Tue Sep 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190903.170002.0c908a18-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190902.193637.c42b1a9c-1
- Update to latest snapshot.

* Wed Aug 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190828.173116.6ee6e883-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190827.222225.a692d1ca-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190827.022207.0474e656-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190826.223911.2476cbf1-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190822.002206.75aa2a03-1
- Update to latest snapshot.

* Fri Aug 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190816.084708.faa867b4-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190813.152214.43d3d89a-2
- Remove accountsservice stuff again.

* Tue Aug 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190813.152214.43d3d89a-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190801.104145.4f87fd26-1
- Update to latest snapshot.

* Wed Jul 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190731.155932.c2c64687-1
- Update to latest snapshot.

* Thu Jul 18 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190718.161142.6717a172-1
- Update to latest snapshot.

* Mon Jul 15 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190715.172553.851f43a7-1
- Update to latest snapshot.

* Sun Jul 14 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190714.192602.d57b82e1-1
- Update to latest snapshot.

* Sun Jul 14 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190714.142827.4d266263-1
- Update to latest snapshot.

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190703.204621.7adc2aa8-1
- Update to latest snapshot.

* Mon Jul 01 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190701.150129.269bfa8e-1
- Update to latest snapshot.

* Sun Jun 30 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190630.183104.8dbe7764-1
- Update to latest snapshot.

* Fri Jun 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190628.163753.4398a5ec-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190626.204624.dc5da2fa-1
- Update to latest snapshot.

* Tue Jun 25 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190625.005023.a03f08cc-1
- Update to latest snapshot.

* Mon Jun 24 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190624.213545.72662968-1
- Update to latest snapshot.

* Wed Jun 19 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190608.002905.0646e5b0-2
- Pull upstream pull request fixing login issues.

* Sat Jun 08 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190608.002905.0646e5b0-1
- Update to latest snapshot.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190531.130435.665d2114-2
- Adapt to upstream file changes.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190531.130435.665d2114-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190531.121809.25da6767-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190531.045908.02e3288c-1
- Update to latest snapshot.

* Tue May 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190528.120045.bed3ea45-1
- Update to latest snapshot.

* Tue May 28 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190528.001505.a21ed31b-1
- Update to latest snapshot.

* Mon May 27 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190527.222912.a511dc57-1
- Update to latest snapshot.

* Wed May 22 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190522.090313.f0f179bd-1
- Update to latest snapshot.

* Mon May 20 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190520.184727.47645d24-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190514.150709.13f8dc95-1
- Update to latest snapshot.

* Tue May 07 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190507.224003.5b26dd70-1
- Update to latest snapshot.

* Mon Apr 22 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190422.221553.a3a53652-1
- Update to latest snapshot.

* Fri Apr 19 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190419.205904.79066b80-1
- Update to latest snapshot.

* Thu Apr 11 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190408.234506.451b3df8-2
- Add missing BuildRequires, clean up mutter dependencies for fedora 28+.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190408.234506.451b3df8-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190406.030545.53929ce9-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190405.020148.cb90262c-1
- Update to latest snapshot.

* Thu Apr 04 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190404.202043.fe4810ba-1
- Update to latest snapshot.

* Tue Apr 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190402.224730.66f199b9-1
- Update to latest snapshot.

* Fri Mar 29 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.1+git190329.062703.1e60ebe0-1
- Update to latest snapshot.

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


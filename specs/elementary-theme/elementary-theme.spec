%global srcname stylesheet

%global appname io.elementary.stylesheet

Name:           elementary-theme
Summary:        elementary GTK+ Stylesheet
Version:        5.3.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildArch:      noarch


%description
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.


%package        gtk2
Summary:        elementary GTK+ Stylesheet for GTK+2

Requires:       %{name} = %{version}-%{release}
Requires:       gtk-murrine-engine

Supplements:    (%{name} and gtk2)

%description    gtk2
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the GTK+2 theme.


%package        gtk3
Summary:        elementary GTK+ Stylesheet for GTK+3

Requires:       %{name} = %{version}-%{release}

Supplements:    (%{name} and gtk3)

%description    gtk3
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the GTK+3 theme.


%package        plank
Summary:        elementary GTK+ Stylesheet for plank

Requires:       %{name} = %{version}-%{release}
Requires:       plank

Supplements:    (%{name} and plank)

%description    plank
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the plank theme.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files
%doc README.md
%license COPYING

%dir %{_datadir}/themes/elementary
%{_datadir}/themes/elementary/index.theme

%{_datadir}/metainfo/%{appname}.appdata.xml

%files          gtk2
%{_datadir}/themes/elementary/gtk-2.0/

%files          gtk3
%{_datadir}/themes/elementary/gtk-3.0/

%files          plank
%{_datadir}/themes/elementary/plank/
%{_datadir}/plank/themes/elementary-dark/


%changelog
* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.0+git191125.173513.f94f7fcf-1
- Update to latest snapshot.

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.0+git191119.210523.039b04c6-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.0+git191101.213327.44d0c152-3
- Package and validate appdata file.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.0+git191101.213327.44d0c152-2
- Drop removed files.

* Sat Nov 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.0+git191101.213327.44d0c152-1
- Update to version 5.3.0.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git191101.213327.44d0c152-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git191101.200723.13ceada6-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git191101.154825.6f469729-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git191030.222648.82a8a27d-2
- Add new dark plank theme.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git191030.222648.82a8a27d-1
- Update to latest snapshot.

* Wed Oct 23 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git191023.220547.ed4a690e-1
- Update to latest snapshot.

* Fri Oct 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git191010.234549.93eb1b1a-1
- Update to latest snapshot.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git191004.165330.f734bd78-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git191002.001255.890a892a-1
- Update to latest snapshot.

* Fri Sep 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git190927.202256.1563a1fa-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git190919.182334.1fcde348-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git190919.173324.2865aa2f-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git190917.230447.1d171593-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git190911.015119.d3a44086-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git190829.084713.a1d4e8c1-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git190827.160912.6fbec65d-1
- Update to latest snapshot.

* Sun Aug 25 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git190825.081949.6b0eb984-1
- Update to latest snapshot.

* Sun Aug 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5+git190803.183237.2ded98fb-1
- Update to version 5.2.5.

* Sat Aug 03 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.4+git190803.183237.2ded98fb-1
- Update to latest snapshot.

* Thu Jul 25 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.4+git190725.070525.a296d8c8-1
- Update to latest snapshot.

* Wed Jul 24 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.4+git190724.211807.4ab8d71f-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.4+git190716.173417.b8b6f7b9-1
- Update to latest snapshot.

* Thu Jul 11 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.4+git190711.160542.7583a9ad-1
- Update to latest snapshot.

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.4+git190709.172753.485f0c40-1
- Update to latest snapshot.

* Tue Jul 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.4+git190627.221816.ec23fec4-1
- Update to version 5.2.4.

* Thu Jun 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190627.221816.ec23fec4-1
- Update to latest snapshot.

* Thu Jun 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190627.215659.097d4122-1
- Update to latest snapshot.

* Thu Jun 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190627.205717.3801f079-1
- Update to latest snapshot.

* Wed Jun 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190619.122630.77d87125-1
- Update to latest snapshot.

* Tue Jun 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190618.214120.76f38469-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190531.222031.b5575c1d-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190531.213639.56e31e9b-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190531.050000.e8120ef8-1
- Update to latest snapshot.

* Tue May 28 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190528.203526.1825284a-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190514.190131.5a31c029-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190514.185953.2364c75a-1
- Update to latest snapshot.

* Fri May 10 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190510.194528.3e9e2eea-1
- Update to latest snapshot.

* Fri May 10 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190510.181219.e8ab1380-1
- Update to latest snapshot.

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3+git190418.090441.c170761e-1
- Update to version 5.2.3.

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.2+git190418.090441.c170761e-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.2+git190408.202115.ab2f20b0-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.2+git190406.201619.0ee1aa62-1
- Update to latest snapshot.

* Fri Mar 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.2+git190301.182135.231726bf-1
- Update to latest snapshot.

* Fri Mar 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.2+git190228.002954.c91036b7-1
- Update to version 5.2.2.

* Thu Feb 28 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.1+git190228.002954.c91036b7-1
- Update to latest snapshot.

* Fri Feb 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.1+git190215.212300.615a1914-1
- Update to latest snapshot.

* Fri Feb 08 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.1+git190207.232546.813e2927-1
- Update to latest snapshot.

* Sat Feb 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.1+git190202.045518.10f8b946-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.1+git190110.223909.e35b3c1f-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.1+git190102.195159.12e434cd-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.1+git181228.180858.a09e9f1f-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.1+git181218.175422.a1613265-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.1+git181218.091947.1ccc1ca1-1
- Update to version 5.2.1.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.0+git181218.091947.1ccc1ca1-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.0+git181121.225823.9107b925-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.0+git181113.185112.0b49902f-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.0+git181105.203238.199e333e-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.0+git181102.180606.8cc03498-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.0+git181016.052546.5c94e686-2
- Occasional mass rebuild.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.0+git181016.052546.5c94e686-1
- Update to version 5.2.0.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git181016.052546.5c94e686-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git181004.184229.d8be6eb3-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git181003.175719.d0abc2c0-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git181002.211120.2c0b0e2c-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git181002.193835.fca53948-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git181002.175203.d30e49bc-1
- Update to latest snapshot.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git181001.214238.4000a324-1
- Update to latest snapshot.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git181001.181827.3bf23332-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180928.064913.4f8def59-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180928.042417.56886ca9-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180918.180700.eff19f3d-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180908.213517.b350fa09-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180908.201722.755f0796-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180908.172049.17b463d0-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180821.170537.92aee75b-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180815.204820.24e5a70a-3
- Use the new meson build system.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180815.204820.24e5a70a-2
- Occasional mass rebuild.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180815.204820.24e5a70a-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180815.192250.1097c52a-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180815.154517.b626d2b5-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180814.230618.b5cf464c-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180808.182356.51d47e5d-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180803.170121.b4ab2c3f-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180731.205941.0ad13ad6-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180726.154816.751d9124-2
- Adapt to upstream file changes.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180726.154816.751d9124-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180725.230831.ae51069a-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180723.224817.94122bc1-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180710.121620.27ad74e6-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180707.102354.8b910cfd-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180605.013208.bfa7b6d2-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180529.184617.14207e9c-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180528.200206.0b0bcbd0-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180515.173135.a42bb09c-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180511.053434.f6c2eba8-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180509.012253.1cf07172-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180504.162317.9d70eeb6-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180502.230854.2c1268f6-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180501.162241.4e729f9b-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180427.234753.92ce54a7-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180420.192502.3e0c472b-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180420.014620.796341be-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180413.172700.0a900e40-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180408.174826.a88f2a31-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180401.183645.203811e5-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180327.190808.53a1dc4f-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180321.163925.64271313-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180319.180130.2e48681f-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180313.200856.a3caf471-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180311.202136.33b87f73-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180305.183832.9454cd43-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180301.035922.4c9415b9-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180223.223338.8b2f1f3f-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180223.063424.56a5a1d6-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180210.174550.e496c542-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180131.221940.a2d7b70f-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180120.212024.8468054a-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180118.181744.f0dd2c40-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180109.204946.0347dcdc-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171231.175903.886c9630-2
- Merge .spec file from fedora.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171231.175903.886c9630-1
- Update to latest snapshot.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171229.222307.18ec68f6-1
- Update to latest snapshot.

* Thu Dec 28 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171228.183102.137afe69-1
- Update to latest snapshot.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171212.203746.d4766477-1
- Update to latest snapshot.

* Mon Dec 11 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171211.183836.18d919e6-1
- Update to latest snapshot.

* Wed Nov 29 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171129.182341.bd7fc6bc-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171116.234955.383aa236-1
- Update to latest snapshot.

* Wed Nov 15 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171114.224021.2b2e0523-1
- Update to latest snapshot.

* Sun Oct 29 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171029.214602.e3d44a58-1
- Update to latest snapshot.

* Sat Oct 28 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171028.003928.be507119-1
- Update to latest snapshot.

* Wed Oct 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171017.211349.a244d049-1
- Update to latest snapshot.

* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171012.163047.a6e541d3-1
- Update to latest snapshot.

* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git170925.140355.6a96d0f3-1
- Update to version 5.1.1.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170925.140355.6a96d0f3-1
- Update to latest snapshot.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170917.191146.384412d6-1
- Update to latest snapshot.

* Thu Aug 31 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170831.163958.d4137cb0-1
- Update to latest snapshot.

* Wed Aug 30 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170830.192346.73e8e2cb-1
- Update to latest snapshot.

* Sat Aug 26 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170826.203852.27c0fe5f-1
- Update to latest snapshot.

* Sat Aug 26 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170826.195943.65c8b062-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170819.171047.2f485fb1-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170819.165546.77d918ca-1
- Update to latest snapshot.

* Sat Aug 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170810.193052.29777e21-1
- Update to version 5.1.0.

* Thu Aug 10 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170810.193052.29777e21-1
- Update to latest snapshot.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170808.152138.cde785f6-1
- Update to latest snapshot.

* Sat Jul 29 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170729.203948.5a0b0bbc-1
- Update to latest snapshot.

* Thu Jul 27 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170727.011959.ae7b021a-1
- Update to latest snapshot.

* Wed Jul 26 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170726.141331.49869a84-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170725.033915.06327c6d-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170722.201500.a27fee78-1
- Update to latest snapshot.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170719.161159.a057c8af-1
- Update to latest snapshot.

* Tue Jul 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170718.170824.1e91f11f-1
- Update to latest snapshot.

* Mon Jul 17 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170717.144046.d771a6dc-1
- Update to latest snapshot.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170716.193802.ffa88847-1
- Update to latest snapshot.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170715.183054.2e1b2771-1
- Update to latest snapshot.

* Fri Jul 14 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170714.174844.9b9cf189-1
- Update to latest snapshot.

* Fri Jul 14 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170714.132038.f68e4d02-1
- Update to latest snapshot.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170711.172317.224c8b63-1
- Update to latest snapshot.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170710.191636.0676d4d9-2
- Add GTK 3.22 theme to gtk3 subpackage.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170710.191636.0676d4d9-1
- Update to latest snapshot.

* Mon Jul 10 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170710.063940.73154fb8-1
- Update to latest snapshot.

* Sun Jul 09 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170709.163839.1f26c7c2-1
- Update to latest snapshot.

* Sat Jul 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170707.193146.fcadef2d-1
- Update to latest snapshot.

* Fri Jul 07 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170707.025047.0102c0fe-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170617.153121.5696951d-1
- Update to latest snapshot.

* Thu Jun 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170607.205340.72f9a91e-1
- Update to latest snapshot.

* Wed May 24 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170524.154507.546aeb0e-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170506.180348.62761903-1
- Update to latest snapshot.

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170501.094928.bf0893a0-1
- Update to latest snapshot.

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170430.094741.471ffaeb-2
- Adapt to upstream file changes.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170430.094741.471ffaeb-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170212.162057.5f600c6b-1
- Update to version 5.0.4.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git170128.184610.01d0411e-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git170128.184610.01d0411e-2
- Sync spec with fedora package.

* Fri Jan 20 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git170115.161326.548fac7c-1
- Update to version 5.0.3.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git170115.161326.548fac7c-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git161218.174932.727c158a-1
- Update to version 5.0.2.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git161218.174932.727c158a-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git161015.175037.cb6b93eb-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160927.144324.36a46bf9-2
- Spec file cleanups.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160927.144324.36a46bf9-1
- Update to latest snapshot.

* Sun Sep 25 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160925.113001.778259b4-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160923.173728.192e7cc8-1
- Update to version 5.0.2.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git160923.173728.192e7cc8-1
- Update to latest snapshot.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git160922.142219.f2f734b3-1
- Update to version 5.0.1.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160919.163423~877fab28-1
- Update to latest snapshot.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160919.134452~ad45ee14-1
- Update to latest snapshot.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160916.205458~8189f96b-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160911.211643~3457221a-1
- Update to version 5.0.1.



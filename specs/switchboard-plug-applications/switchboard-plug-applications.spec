%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type personal
%global plug_name applications

%global appname io.elementary.switchboard.applications

Name:           switchboard-plug-applications
Summary:        Switchboard Applications plug
Version:        2.1.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            http://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  /usr/bin/appstream-util

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
The applications plug is a section in the Switchboard (System Settings)
that allows the user to manage application settings.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f applications-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191109.122512.18794117-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191107.002048.97891e4f-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191106.234205.2fea2f08-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191007.152328.1cba7c7b-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191003.145638.ec8eac51-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191001.224045.56f48bc3-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191001.211335.45b11b1b-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191001.203451.8fcdfed7-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190919.173404.90a09c05-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190917.234635.cc19c96f-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190916.145927.f7e5fbc6-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190916.004340.0a994b31-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190906.152240.059f4340-1
- Update to latest snapshot.

* Wed Aug 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190828.092242.ce65b4fd-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190826.062223.89ffa2cd-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190823.222629.79ba1f84-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190731.232739.907db6d9-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190716.165509.16556cd3-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190626.204449.ba8241d5-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190531.045825.c9dc303c-1
- Update to latest snapshot.

* Thu May 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190530.093252.dbe49c63-1
- Update to latest snapshot.

* Tue May 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190528.100342.01fe346e-1
- Update to latest snapshot.

* Thu May 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190516.171442.05bc42a2-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190513.230257.8ab8d749-1
- Update to latest snapshot.

* Thu Apr 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190411.215327.e992256b-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190408.005312.49867a38-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190312.212704.fe2dabea-1
- Update to latest snapshot.

* Wed Mar 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190306.182655.146e0b6d-1
- Update to latest snapshot.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190128.131832.4b5b77b8-1
- Update to version 2.1.5.

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190128.131832.4b5b77b8-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190125.000124.55de8ab7-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190114.132223.aca477a4-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190114.000940.e0b7d5b8-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190110.000708.4c00979a-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190107.000319.4d476d83-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190106.122714.0c08112d-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190102.193123.5243395c-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181211.160503.0bdf4a38-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181202.063358.8bb1a55d-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181124.130839.fe457da6-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181116.081447.6f431c93-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181107.015243.e00703b8-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181104.132152.cc9ed550-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181026.150247.85b35602-2
- Occasional mass rebuild.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181026.150247.85b35602-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181025.073815.86066b4d-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181020.205646.63ff4455-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181020.140842.2d7c77cc-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181020.025732.3e6eb045-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181019.222320.636d534d-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181019.193553.0f21ea45-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181018.203253.cee345fa-1
- Update to version 2.1.4.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181018.203253.cee345fa-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181018.064414.7b56b7e3-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181017.000723.c5f6ab87-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.194906.fb465387-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.180749.a45af474-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.163944.6e2305c3-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.134052.d763a174-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.124433.2fbba3cf-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.102956.336f1529-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.090737.9f2e630d-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.082006.57acaaff-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.065806.aa80eeae-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.015214.31a85ce7-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181016.005953.babce0a9-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181013.220607.4df4e0fd-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181009.174029.7ab7b1d6-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git181003.205232.0975f8a1-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git180919.000912.cc4c9f02-1
- Update to latest snapshot.

* Fri Sep 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git180914.053411.c5b1cb05-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git180724.000540.7d60fe99-2
- Occasional mass rebuild.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git180724.000540.7d60fe99-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git180622.081214.73abc519-2
- Adapt to upstream file changes.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3.1+git180622.081214.73abc519-1
- Update to version 0.1.3.1.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180622.081214.73abc519-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180610.001153.e7db2e17-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180607.144630.22b57f9f-1
- Update to version 0.1.3.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180607.144630.22b57f9f-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180607.131819.3e2c6845-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180602.000559.b97c790c-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180530.000348.651b54c5-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180529.142418.1725b2d9-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180527.125410.b5598085-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180527.000534.ab362bed-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180524.104908.bb539acc-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180510.171846.758ee6f8-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180509.203331.7c70cbd4-2
- Adapt to upstream file changes.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180509.203331.7c70cbd4-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180429.123557.91df7ad0-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180415.092349.62fa74dd-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180324.205550.d241d8f0-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180310.000419.52d13bf9-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180308.143743.1d8540da-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180306.182625.6312a321-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180303.174002.cf7f768c-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180228.095909.11260457-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180220.223349.99c08f28-2
- Adapt to cmake -> meson switch.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180220.223349.99c08f28-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180218.110907.765db998-1
- Update to latest snapshot.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180215.153436.5026068c-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180209.001012.a8dc4447-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180206.201803.48dbc0e0-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180206.192818.94cd2223-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180205.001141.e3b2fa8c-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171226.000956.a480ecf7-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.233212.252a4e74-2
- Merge .spec file from fedora.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.233212.252a4e74-1
- Update to latest snapshot.

* Sat Oct 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171007.070417.f9e56991-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170725.082730.490bb634-1
- Update to version 0.1.2.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev257-1
- Update to latest snapshot.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev256-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev233-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev232-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev231-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev230-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev229-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev227-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev226-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev220-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev219-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev218-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev217-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev216-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev215-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev214-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev213-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev212-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev211-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev210-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev209-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev208-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev207-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev206-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev205-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev204-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev203-1
- Update to version 0.1.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev202-1
- Update to version 0.1.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev201-1
- Update to version 0.1.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev200-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev199-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev198-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev197-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev196-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev195-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev194-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev193-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev192-1
- Update to latest snapshot.

* Wed Dec 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev191-1
- Update to latest snapshot.

* Tue Dec 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev190-1
- Update to latest snapshot.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev189-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev188-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev187-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev186-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev185-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev184-1
- Update to latest snapshot.

* Sat Nov 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev183-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev181-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev179-1
- Update to latest snapshot.

* Tue Nov 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev177-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev176-1
- Update to latest snapshot.

* Tue Nov 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev175-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev174-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev173-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev172-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev171-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev170-1
- Update to latest snapshot.

* Fri Oct 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev169-1
- Update to latest snapshot.

* Thu Oct 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev168-1
- Update to latest snapshot.

* Tue Oct 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev165-1
- Update to latest snapshot.

* Mon Oct 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev164-1
- Update to latest snapshot.

* Mon Oct 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev161-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev160-1
- Update to latest snapshot.

* Fri Sep 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev159-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev158-1
- Update to version 0.1.1.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev158-2
- Spec file cosmetics.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev158-1
- Update to latest snapshot.

* Sat Sep 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev157-1
- Update to latest snapshot.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev156-1
- Update to latest snapshot.

* Fri Aug 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev155-1
- Update to version 0.1.1.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev154-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev153-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev152-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev151-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev151-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev150-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev149-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev148-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev147-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev146-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev145-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev144-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev143-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev142-2
- Update for packaging changes.

* Tue Jul 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev142-1
- Update to latest snapshot.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev141-1
- Update to latest snapshot.

* Sat Jul 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev140-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev139-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev138-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev137-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev137-2
- Update for packaging changes.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev137-1
- Update to version 0.1.0.2.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev137-1
- Initial package.



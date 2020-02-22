%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_name datetime
%global plug_type system

%global plug_rdnn io.elementary.switchboard.%{plug_name}

Name:           switchboard-plug-%{plug_name}
Summary:        Switchboard Date and Time plug
Version:        2.1.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
A switchboard plug to configure date and time settings.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200222.140853.fdc53570-1
- Update to latest snapshot.

* Fri Feb 14 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200214.170839.f30cf1a7-1
- Update to latest snapshot.

* Fri Jan 24 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200124.010803.996d5967-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200121.160800.22bd2b72-1
- Update to latest snapshot.

* Sat Jan 11 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200111.160744.853d513d-1
- Update to latest snapshot.

* Thu Jan 09 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200109.160740.7fb01cbb-1
- Update to latest snapshot.

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200108.080229.0721fa7d-1
- Update to latest snapshot.

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200107.233430.f4e6dd08-1
- Update to latest snapshot.

* Tue Jan 07 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200107.183201.136507ea-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200106.210743.22513a5c-1
- Update to latest snapshot.

* Sun Jan 05 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200105.170736.d1461c6a-1
- Update to latest snapshot.

* Wed Jan 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200101.160730.95957e45-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191224.220720.8286cecc-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191220.160913.fd5f54e9-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191219.130718.08e24843-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191217.183534.3e41ea03-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191204.212526.b5549752-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191127.202526.de5745c0-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191125.092511.bc443fa3-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191122.032523.f677c737-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191117.212454.0812e194-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191111.122450.48899c85-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191109.122502.e0ff57dc-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191106.234908.8ff1026b-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191106.224353.08b4547d-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191009.172328.0dc1759c-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191007.152328.d62f5271-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191003.151253.436766fe-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191003.011754.a30524ba-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191002.112318.06bc2246-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191001.220424.f2b6955d-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190919.183757.45355f05-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190919.173105.73e6e4f8-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190917.092302.68189852-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190907.202241.954027b7-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190906.152245.0d8569d0-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190823.222319.f00b2f7a-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190822.002218.e29666f7-1
- Update to latest snapshot.

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190820.032208.033b082c-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190815.002202.a2fcdb51-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190801.104239.6418c5ef-1
- Update to latest snapshot.

* Wed Jul 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190731.211740.2d70f2d1-1
- Update to latest snapshot.

* Tue Jul 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190723.170539.777d50d9-1
- Update to latest snapshot.

* Sun Jul 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190721.172434.ba084eeb-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190717.095626.8161b679-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190716.150708.20cbd3d0-1
- Update to latest snapshot.

* Fri Jul 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190712.204309.bcd6ce18-1
- Update to latest snapshot.

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190709.171657.b854b581-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190626.204503.b25ae99c-1
- Update to latest snapshot.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190604.202705.14f865fd-1
- Update to latest snapshot.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190604.194924.9101a429-1
- Update to latest snapshot.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190604.011805.6e4e0528-2
- Remove unnecessary downstream patch.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190604.011805.6e4e0528-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190531.045943.34d34738-1
- Update to latest snapshot.

* Thu May 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190530.093127.0089c11d-1
- Update to latest snapshot.

* Sat May 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190518.030309.04961ba1-1
- Update to latest snapshot.

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190408.195330.5e7ea91c-2
- Add patch to use the correct GSettings schema for clock-format.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190408.195330.5e7ea91c-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190406.175221.941e56cf-1
- Update to latest snapshot.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190405.171549.b5e53c03-1
- Update to latest snapshot.

* Sun Mar 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190331.065211.961fa41c-1
- Update to latest snapshot.

* Tue Mar 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190326.112254.e12ef42a-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190305.084243.277cf57f-2
- Adapt to renamed appdata file.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190305.084243.277cf57f-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190115.000635.65d6bf51-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190114.001035.84787948-1
- Update to latest snapshot.

* Sat Jan 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190112.000925.46bc981d-1
- Update to latest snapshot.

* Fri Jan 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190111.091828.8ecd5a28-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190106.140043.f7d864ff-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181215.080107.63eef345-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181210.214814.caff3063-1
- Update to version 2.1.5.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181210.214814.caff3063-2
- Adapt to added appdata file.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181210.214814.caff3063-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181202.063500.2aa045fb-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181124.130900.d779bbc6-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181120.095945.fc3c5825-1
- Update to latest snapshot.

* Tue Nov 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181113.160548.a8dd6c2a-1
- Update to latest snapshot.

* Fri Nov 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181109.181107.73135362-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181107.014705.f286e315-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181102.110154.e3a55bf9-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181102.110154.e3a55bf9-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181102.091059.8dd62bac-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181025.082314.c616a9ec-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181024.235244.e40f1e87-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181024.092717.f8f7ba87-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181022.052314.f9b7da8e-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181021.132705.ce75b28d-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181015.145306.e22d4d06-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181014.020938.f1138a23-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181014.000553.27fefa7d-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181013.122552.d5116918-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181011.175820.65c8eb2d-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181011.000645.ba7e7107-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181010.211342.ddbfaf94-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181010.141735.a4ba72e5-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181010.000232.cdbf68cb-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181009.232209.95b3eb64-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181009.200538.b8911014-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181009.191803.ea008c33-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181009.170759.e5dc4af4-1
- Update to version 2.1.4.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181009.170759.e5dc4af4-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181009.160829.aa8ae79f-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181009.154625.9420ca08-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181007.001008.5a6f905e-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181002.214452.1dccc813-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180910.000835.8f2eda69-1
- Update to latest snapshot.

* Sun Sep 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180909.000301.8f9f92a2-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180908.191012.44745ead-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180907.005937.d0bd7d5e-1
- Update to latest snapshot.

* Mon Sep 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180903.120753.1a4d17fa-1
- Update to latest snapshot.

* Mon Sep 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180903.000258.ee27b3aa-1
- Update to latest snapshot.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180902.000858.777e1718-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180901.000911.a1ed081c-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180830.000816.a145d3b9-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180829.165011.ee116cf7-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180818.135058.f202a5cd-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180813.000407.6b759453-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180813.000407.6b759453-1
- Update to latest snapshot.

* Fri Aug 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180809.234149.590aa0af-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180726.170408.deb2c17a-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180721.000750.e7a660b2-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180720.205837.4499e93e-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180718.000643.6d36cf45-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180717.000326.40e72ca9-1
- Update to latest snapshot.

* Mon Jul 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180716.085434.c6fbce7a-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180715.001024.fa825167-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180713.000423.2d97d2f1-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180712.072815.d4662023-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180711.164645.6fa742a1-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180710.000358.4677162f-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180703.000701.e80de7c2-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180614.151535.ae88a9fe-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180614.000937.d03e95a4-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180613.165208.d4ed969e-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180613.000810.68f9ccd7-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180612.073242.0ee3e3cb-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180607.142937.b43005cd-1
- Update to version 0.1.3.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180607.142937.b43005cd-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180607.001004.d267ac12-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180606.000952.0ed8eda3-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180604.135014.c5dbd31f-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180604.000949.579a2e7c-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180603.114957.e85fb83d-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180601.000842.cb49573c-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180531.000336.b6d7ff0a-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180530.000448.dabe9b4d-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180529.001323.ad4251ad-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180528.000330.0d2053d5-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180527.142359.0c71aa9c-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180524.001053.a0d0ea5a-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180518.143434.2eb65e61-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180518.000800.d292f746-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180517.000434.be17c3d7-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180515.000633.c5fd7520-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180514.000254.377e7f74-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180511.000700.343fa1b0-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180509.000750.3c1fbcb9-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180507.000334.677b6ee6-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180506.001032.8de8c630-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180429.141948.85d5f4a8-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180420.001225.cc1400d0-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180325.000941.1b775201-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180319.070527.6014fbf6-2
- Adapt to CMake -> meson switch.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180319.070527.6014fbf6-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180316.000422.2a44f960-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180314.000243.07c96517-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180313.125733.94e50634-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180312.001015.5fc49ec7-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180311.201006.c4c7d575-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180309.090858.6a3b46f3-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180308.174432.c5e89e34-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180227.000427.29f759a9-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180224.000447.f13b2f63-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180221.000841.1f0afc8c-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180218.200715.1b293c64-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180217.101017.1ab285ea-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180211.000915.93d233a4-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180208.070007.6f2cc6a9-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180205.001211.ab431a8f-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180123.000636.b0e003d3-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170818.000141.a838f78d-2
- Merge .spec file from elementary-stable.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170818.000141.a838f78d-1
- Update to latest snapshot.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170808.134649.17bcd921-1
- Update to latest snapshot.

* Sun Aug 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170806.162520.a5163b2e-1
- Update to latest snapshot.

* Mon Jul 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170717.003956.c6304c47-1
- Update to latest snapshot.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170715.160723.4c1cc554-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170702.102817.d4184541-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170617.175316.5db4d317-1
- Update to latest snapshot.

* Thu Jun 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170608.165115.fbc68f9c-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170508.195619.f52eb815-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170421.132822.df62aaaf-1
- Update to version 0.1.2.

* Fri Apr 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev221-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev210-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev209-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev208-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev207-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev206-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev205-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev204-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev203-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev202-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev201-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev200-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev199-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev198-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev197-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev196-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev195-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev194-1
- Update to latest snapshot.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev193-1
- Update to version 0.1.1.1.

* Thu Jan 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev192-1
- Update to version 0.1.1.1.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev191-1
- Update to version 0.1.1.1.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev190-1
- Update to version 0.1.1.1.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev189-1
- Update to version 0.1.1.1.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev188-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev187-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev186-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev185-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev184-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev183-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev182-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev181-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev180-1
- Update to version 0.1.1.1.



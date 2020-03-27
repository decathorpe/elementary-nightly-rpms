%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type system
%global plug_name accessibility

%global plug_rdnn io.elementary.switchboard.a11y

Name:           switchboard-plug-a11y
Summary:        Switchboard Accessibility plug
Version:        2.1.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

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
The accessibility plug is a section in the Switchboard (System Settings)
that allows the user to manage accessibility settings.


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
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Fri Mar 27 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200326.230954.9eac1a2b-1
- Update to latest snapshot.

* Wed Mar 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200324.230944.94756395-1
- Update to latest snapshot.

* Thu Mar 19 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200319.190948.929525a6-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200301.140928.95744f23-1
- Update to latest snapshot.

* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200222.140904.2f694a88-1
- Update to latest snapshot.

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200115.222634.9883fcc2-1
- Update to latest snapshot.

* Sun Jan 12 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200112.200747.a493f6fa-1
- Update to latest snapshot.

* Sun Jan 05 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200105.170742.485e9143-1
- Update to latest snapshot.

* Thu Jan 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200101.230834.1f08d26d-1
- Update to latest snapshot.

* Wed Jan 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git200101.160729.62480dc5-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191224.220720.2b184b50-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191220.160919.2b2ab432-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191219.130720.61158cf8-1
- Update to latest snapshot.

* Sun Dec 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191201.102505.2f0b3299-1
- Update to latest snapshot.

* Fri Nov 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191129.002508.80fe111d-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191127.202528.074b8aee-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191125.092512.767c8c1c-1
- Update to latest snapshot.

* Sat Nov 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191123.003035.712dd1fe-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191122.032523.39105452-1
- Update to latest snapshot.

* Wed Nov 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191120.175715.f55c6bb0-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191117.202503.4db540e8-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191116.172454.b7101b49-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191111.122452.d1046da6-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191109.122504.3fe201b0-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191107.161728.16f7d67d-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191106.234302.5e1c1e8d-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191009.172402.5ee08bb4-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191007.152344.0bb78479-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191005.042325.7bb2e754-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191003.151019.adc4ffa2-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191002.210340.c23cb63c-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191001.150030.957c4212-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git191001.103234.a0035df8-1
- Update to latest snapshot.

* Sun Sep 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190929.014633.8046f8e1-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190919.182159.19d22502-1
- Update to latest snapshot.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190904.232244.49799459-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190823.222719.9472c50c-1
- Update to latest snapshot.

* Fri Aug 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190816.013253.ddd550eb-1
- Update to latest snapshot.

* Sun Aug 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190811.091821.b9df3a6c-1
- Update to latest snapshot.

* Thu Aug 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190808.193434.0584770c-1
- Update to latest snapshot.

* Sun Aug 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190804.172227.559e67a2-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190731.233556.ced682e5-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190717.130728.6d030ee1-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190626.204438.62fa8825-1
- Update to latest snapshot.

* Sat Jun 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190622.112648.d6a76a08-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190531.045952.3164dd15-1
- Update to latest snapshot.

* Wed May 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190529.040402.72b6cdda-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190408.000735.ca79932f-1
- Update to latest snapshot.

* Thu Apr 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190404.195223.c6241f50-1
- Update to latest snapshot.

* Sun Feb 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190224.000211.32749117-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190212.000708.d00e5062-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190114.134554.7c51c372-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190114.001048.1b7fcd1c-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190107.000354.01aa4bff-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190106.122428.df39296a-1
- Update to latest snapshot.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181229.000126.d2cc8bb9-1
- Update to latest snapshot.

* Fri Dec 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181228.142021.7944959f-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181218.000140.40be7ed3-1
- Update to latest snapshot.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181216.193706.f6662ac5-1
- Update to latest snapshot.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181215.131845.aefefaa0-2
- Adapt to fixes appdata file name.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181215.131845.aefefaa0-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181215.125927.7746e078-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181212.090009.a4480409-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181210.202643.383ae7ad-1
- Update to version 2.1.3.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181210.202643.383ae7ad-2
- Adapt to added appdata file.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181210.202643.383ae7ad-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181207.003851.003b290e-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181122.200359.b6a5d81b-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181116.082659.192841ac-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181107.015415.29106a65-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181106.212232.89632d4a-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181104.145706.70166bd9-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181027.180217.08b3a9eb-2
- Occasional mass rebuild.

* Sat Oct 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181027.180217.08b3a9eb-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181025.081544.de2b0ac2-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181024.090608.cdbe8ea6-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181021.121510.b7644bc5-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181020.030730.6c0d4f77-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181018.071134.8a5822b3-1
- Update to version 2.1.2.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181018.071134.8a5822b3-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181017.000753.38b14c66-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.201106.999041c9-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.180157.52d53c3f-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.133933.4ec26626-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.123226.511da150-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.103346.9b64aa8e-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.092545.5951dc62-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.005435.305ad773-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181015.215531.f3ace5fa-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181010.170409.1e91d18d-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181009.155152.5ad6d52e-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181003.143243.bfd88a60-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180930.001008.6f5f816a-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180929.183805.34fc7128-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180929.000952.1e28edc9-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180927.001035.84b17236-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180926.061812.5b3be60a-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180919.160347.ef46ac37-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180919.155603.66e87a12-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180919.121603.13aab7fb-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180919.112242.bd03ff81-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180919.103239.7818b305-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180919.080018.046423c3-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180919.054320.2d8e4d91-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180919.000959.ae5e5305-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180918.234754.1106b862-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180918.182210.90877213-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180918.175054.50f92fd2-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180910.152604.c398a3fd-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180829.061859.2f49123a-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180812.140718.adcf3992-2
- Occasional mass rebuild.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180812.140718.adcf3992-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180803.000442.f38ec804-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180724.030804.3a1820cd-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180716.211327.dda0b4cc-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180709.205846.aefb7e39-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180706.140115.0a6fe1ca-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180706.102737.ba4c6542-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180618.000614.c5447c22-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180615.001145.36aa98fd-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180612.194642.a29f93e3-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180612.072400.18af7098-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180602.024713.eb216f28-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180601.000851.378a816e-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180531.144519.c6b7308c-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180531.000351.f0b8918f-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180530.000459.858cce35-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180527.123815.7936427b-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180527.000618.0493de58-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180516.141241.8ad91a61-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180511.000708.94a7dc7f-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180429.142358.8d837e1f-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180424.201839.e4c824cb-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180416.211420.dc7deda5-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180415.001045.5a6f2ece-1
- Update to latest snapshot.

* Mon Apr 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180408.231355.8b544623-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180330.173223.acffe723-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180326.000929.bc242d14-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180311.183843.18f7221a-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180306.185105.aa3ec29d-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180301.000350.eba0a6c1-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180226.201622.239b22e8-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180226.000913.0ba049fb-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180225.000958.b01f92ea-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180223.182641.13a1a0e4-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180221.215240.704b9b16-2
- Adapt to cmake -> meson switch.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180221.215240.704b9b16-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180221.144751.a8cdfbab-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180221.122114.2a4e61f2-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180221.005524.f3f00207-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180209.001034.912e36f8-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171213.044016.33b965d9-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171118.230503.f1ce2761-2
- Merge .spec file from fedora.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171118.230503.f1ce2761-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170731.073728.cac6ed4f-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170711.211554.deda13c2-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170711.211547.b3621378-1
- Update to latest snapshot.

* Fri Jul 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170706.205148.275373aa-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170703.171056.c89450a1-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170702.185904.1a97c3bc-1
- Update to latest snapshot.

* Thu Jun 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170622.101506.c48b7053-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170617.151523.ae2429ec-1
- Update to latest snapshot.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170521.211428.bb6c014b-1
- Update to latest snapshot.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170515.154435.e54d55cc-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170507.203006.a63cdbcf-1
- Update to version 0.1.1.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev140-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev139-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev138-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev137-1
- Update to latest snapshot.

* Mon Mar 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev135-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev133-1
- Update to latest snapshot.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev132-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev127-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev126-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev125-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev124-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev123-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev122-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev121-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev120-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev119-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev118-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev117-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev116-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev115-1
- Update to version 0.1.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev114-1
- Update to version 0.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev113-1
- Update to version 0.1.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev112-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev111-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev110-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev109-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev108-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev107-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev106-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev105-1
- Update to version 0.1.



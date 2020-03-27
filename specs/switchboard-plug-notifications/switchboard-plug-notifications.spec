%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type personal
%global plug_name notifications

%global appname io.elementary.switchboard.%{plug_name}

Name:           switchboard-plug-notifications
Summary:        Switchboard Notifications plug
Version:        2.1.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       gala%{?_isa}
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and gala%{?_isa})


%description
Configure which apps should be allowed to show notifications.

This is a GModule plugin for Switchboard that configures gsettings keys
related to the Notifications plugin for Gala.


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


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Mar 27 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200326.230949.09999faf-1
- Update to latest snapshot.

* Thu Mar 19 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200319.190949.55e7ef0d-1
- Update to latest snapshot.

* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200301.140921.c727070f-1
- Update to latest snapshot.

* Thu Feb 27 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200227.171748.e00a796d-1
- Update to latest snapshot.

* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200222.140905.d0cc809a-1
- Update to latest snapshot.

* Tue Jan 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200121.082705.58881b24-1
- Update to latest snapshot.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200106.190741.7aba6119-1
- Update to latest snapshot.

* Wed Jan 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git200101.160730.c72947c1-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191224.220721.4fff6820-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191220.160929.8793af88-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191219.130721.d47e9185-1
- Update to latest snapshot.

* Wed Dec 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191204.194050.2f3bb01b-1
- Update to latest snapshot.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191127.202532.76471f1c-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191125.092516.ee453bfb-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191122.032527.6841e029-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191121.091419.27a36fb1-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191121.084444.ec0bd1d1-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191117.202504.a30877fd-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191111.122455.57efd027-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191109.122506.540bd3b5-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191107.162035.e80a5de1-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191106.233938.4448b9d4-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191106.230038.cbf4f2a4-1
- Update to latest snapshot.

* Thu Oct 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191017.172355.d43ed379-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191007.152410.a2390a81-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191003.150138.f31bd8de-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191002.204922.3f74e662-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git191001.013620.f8fedaea-1
- Update to latest snapshot.

* Sun Sep 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190929.013047.895bda86-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190919.183633.693d23bb-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190906.152253.0c1d200d-1
- Update to latest snapshot.

* Sun Sep 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190901.152231.3956a6aa-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190827.012224.5d0e4453-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190823.222255.9a50b2ca-1
- Update to latest snapshot.

* Tue Jul 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190730.225315.8fbeaa71-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190717.135310.fa43cce1-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190626.204539.49455ce6-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190531.044836.89047f75-1
- Update to latest snapshot.

* Sun May 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190519.020312.fb4796e0-1
- Update to latest snapshot.

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190413.225339.0bf05631-1
- Update to latest snapshot.

* Fri Apr 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190412.215548.44f7b2bf-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190305.084320.fd2b2b92-2
- Adapt to renamed appdata file.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190305.084320.fd2b2b92-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190305.032652.4afa4e4b-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190125.000142.4b7d1323-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git190107.000338.8c05269b-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181212.230209.862fd7c4-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.151056.8509ad19-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181107.015451.056baec8-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181104.114915.524d8e05-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181029.101015.fc7966bf-2
- Occasional mass rebuild.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181029.101015.fc7966bf-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181024.150554.7bc081b8-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181016.080538.d7059982-1
- Update to version 2.1.5.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181016.080538.d7059982-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181014.002125.53428ea8-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181013.140136.b1d0986a-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181009.164519.371e7f40-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181002.000414.4d56a314-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180925.000241.b79d05f8-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180919.000930.6f823af5-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180830.000755.d4934ac0-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180722.000352.b51adae9-2
- Occasional mass rebuild.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180722.000352.b51adae9-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180618.000535.89176078-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180615.001116.733d9c68-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180611.152947.c7eabab0-1
- Update to version 0.1.4.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180611.152947.c7eabab0-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180610.001212.0bb2719d-1
- Update to version 0.1.3.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180610.001212.0bb2719d-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180608.122347.d26d9cd6-2
- Drop merged appdata patch.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180608.122347.d26d9cd6-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180606.211755.c63aaec7-3
- Include patch to fix appdata verification.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180606.211755.c63aaec7-2
- Adapt to upstream file changes.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180606.211755.c63aaec7-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180605.213652.f7662ad6-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180604.000937.8551c48f-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180602.000628.28c7c85f-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180601.000816.05fff7aa-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180531.000313.ce02f612-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180530.124507.58331f3f-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180527.192533.edef94f3-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180527.000554.2dace50d-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180525.182118.59c357c5-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180517.000423.082894ef-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180514.000242.0417e80a-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180511.000638.20e2429f-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180510.075335.38c1828b-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180504.000633.7d65672e-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180425.203030.4ea7d8f0-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180421.001137.d44a8f7c-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180324.211115.57170385-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180314.000229.8a0c94e4-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180224.000422.6eb50791-2
- Adapt to cmake -> meson switch.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180224.000422.6eb50791-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180223.183732.c2e0375b-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180220.222127.ef1de560-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180211.000856.afde90c3-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180205.001153.61bb1b5a-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180104.001436.805bb0f7-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.231310.3f6718a4-2
- Merge .spec file from fedora.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.231310.3f6718a4-1
- Update to latest snapshot.

* Sat Nov 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.015850.84bb9fb5-1
- Update to latest snapshot.

* Mon Nov 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171113.162945.ee1e53eb-1
- Update to latest snapshot.

* Fri Nov 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171103.130821.a78ed193-1
- Update to latest snapshot.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171010.111633.0a843d9b-1
- Update to latest snapshot.

* Wed Oct 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171003.204051.c7e7b25a-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170816.113719.7c47d814-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170715.163148.3738bd8e-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170702.103015.3f8aef29-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170617.152057.39a7441c-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170602.170610.8f4090f3-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170525.145811.cc1412cb-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170524.220747.7bf40e85-1
- Update to version 0.1.2.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev217-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev215-1
- Update to latest snapshot.

* Fri Apr 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev214-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev213-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev212-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev211-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev210-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev209-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev208-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev207-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev206-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev205-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev204-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev203-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev202-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev201-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev200-1
- Update to version 0.1.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev199-1
- Update to version 0.1.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev198-1
- Update to version 0.1.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev197-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev196-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev195-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev194-1
- Update to version 0.1.1.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev194-2
- Spec file cosmetics.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev194-1
- Update to latest snapshot.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev193-1
- Update to latest snapshot.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev192-1
- Update to latest snapshot.

* Sat Aug 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev191-1
- Update to version 0.1.1.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev190-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev189-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev188-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev187-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev187-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev186-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev185-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev184-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev183-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev182-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev181-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev180-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev179-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev178-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev177-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev176-2
- Update for packaging changes.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev176-1
- Update to latest snapshot.

* Fri Jul 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev175-1
- Update to latest snapshot.

* Thu Jun 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev174-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev173-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev172-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev171-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev170-4
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev170-3
- Update for packaging changes.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev170-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev170-1
- Initial package.



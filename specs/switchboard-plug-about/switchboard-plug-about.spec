%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type hardware
%global plug_name about

%global plug_rdnn io.elementary.switchboard.about

Name:           switchboard-plug-about
Summary:        Switchboard System Information plug
Version:        2.6.1+git%{date}.%{commit}
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
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       system-logos


%description
This switchboard plug shows system information.


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
* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git191122.032451.dd93eead-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git191117.202434.7c21bf74-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.1+git191116.172430.db7a37e7-1
- Update to version 2.6.1.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191116.172430.db7a37e7-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191115.222640.d060848e-1
- Update to latest snapshot.

* Sun Nov 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191110.192423.52ca1d80-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191109.122436.e49bf764-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191107.000129.948e3c26-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191106.235849.4d8bcfe2-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191106.224945.2d8730df-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191106.180935.8a7ce915-1
- Update to latest snapshot.

* Sun Oct 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191027.192402.e3772708-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191007.152328.faf44791-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git191003.150211.327101bc-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git190930.142318.7c106945-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git190926.220147.da0cac64-1
- Update to latest snapshot.

* Thu Sep 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git190926.215914.4caeea81-1
- Update to latest snapshot.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0+git190924.202308.f3ccec42-1
- Update to version 2.6.0.

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190924.202308.f3ccec42-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190920.173020.332b6102-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190917.144040.cbfeecd1-1
- Update to latest snapshot.

* Tue Sep 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190917.092258.5f0da022-1
- Update to latest snapshot.

* Wed Sep 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190911.191131.1effb636-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190907.212242.8ee72b55-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190906.152241.27e8209e-1
- Update to latest snapshot.

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190902.202240.eb58a147-1
- Update to latest snapshot.

* Sun Sep 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190901.162230.56d0dba2-1
- Update to latest snapshot.

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190826.052220.c232276c-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190823.222646.b513ee2e-1
- Update to latest snapshot.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190821.232212.b9b747ab-1
- Update to latest snapshot.

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190820.112209.dc513e04-1
- Update to latest snapshot.

* Sat Aug 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190817.142206.ece5a127-1
- Update to latest snapshot.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190815.223423.6ff63b8a-1
- Update to latest snapshot.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190814.110443.f1b9e691-1
- Update to latest snapshot.

* Wed Jul 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190731.211139.a8ace664-1
- Update to latest snapshot.

* Tue Jul 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190730.192659.4aab9011-1
- Update to latest snapshot.

* Tue Jul 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190723.173558.db0c4207-1
- Update to latest snapshot.

* Sat Jul 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190720.162419.e962fa0c-1
- Update to latest snapshot.

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190716.152915.a703761b-1
- Update to latest snapshot.

* Sat Jul 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190706.164918.ce201394-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190626.204444.d99333d5-1
- Update to latest snapshot.

* Tue May 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190513.230410.383e208a-1
- Update to latest snapshot.

* Mon May 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190513.040339.9c0dc9e9-1
- Update to latest snapshot.

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190413.230400.eb81a4a6-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190408.005312.f43e66f4-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190406.170321.621922a5-1
- Update to latest snapshot.

* Sun Mar 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190330.225205.e8b39c6a-1
- Update to latest snapshot.

* Fri Mar 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190308.091623.e61fcb78-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190125.000121.aa12b3b5-1
- Update to latest snapshot.

* Tue Jan 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190122.174029.3b7d2e08-1
- Update to latest snapshot.

* Sat Jan 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190119.000957.af19ea9b-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190114.132334.c7d46990-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190114.000936.b879928e-1
- Update to latest snapshot.

* Thu Jan 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190110.000703.9fff7509-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190109.000637.95d5e280-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190107.000316.8d4c36eb-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190106.005926.4bbe51e7-1
- Update to latest snapshot.

* Fri Jan 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git190104.000824.4b68893b-1
- Update to latest snapshot.

* Tue Dec 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git181223.182750.b5dc10c5-2
- Adapt to renamed appdata file.

* Sun Dec 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git181223.182750.b5dc10c5-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git181212.095220.1209dd82-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git181210.204030.fbe82aa3-2
- Adapt to added appdata file.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git181210.204030.fbe82aa3-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.2+git181204.163636.66202b55-1
- Update to version 2.5.2.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181204.163636.66202b55-1
- Update to latest snapshot.

* Sat Dec 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181130.160236.0f7bc840-2
- Remove patch, replaced with flexible solution upstream.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181130.160236.0f7bc840-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181107.014828.2f0696fc-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181105.214318.6e7621fa-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181101.200138.9d5fd511-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181101.200138.9d5fd511-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181030.080838.e8adc68b-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181021.154514.88ec4b4c-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1+git181017.125126.98063a66-1
- Update to version 2.5.1.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git181017.125126.98063a66-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git181015.233048.f827b7f4-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git181014.000327.b5979cf1-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git181009.155833.a06c5cec-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git181008.000503.bad3bf27-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180929.000932.a6a4dfe7-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180925.000224.83a35f4c-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180830.000727.08d07ed9-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180829.162230.01bfafe2-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180829.000349.47e63f2e-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180819.000926.bce5a9dd-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180813.000332.c80f8312-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180813.000332.c80f8312-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180808.110258.8320a86f-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180802.175819.10fa9e9b-1
- Update to latest snapshot.

* Wed Aug 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180801.160842.ab79dee6-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180721.000732.4d0e3468-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180720.210746.9553be05-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180716.154045.cae96744-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180704.231230.1676a600-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180703.192419.1625519e-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180613.000734.4e1db225-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180612.074611.2a91d1b0-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180610.001149.dc76d5ea-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180608.131457.8c0f48cf-1
- Update to version 0.2.5.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180608.131457.8c0f48cf-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180604.022534.cd8052ef-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180531.000244.4acb2d28-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180530.000344.52746f41-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180529.131441.43f30909-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180528.000255.57bd5f4d-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180527.115220.7932cbbe-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180525.203545.d3729a19-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180520.151824.2c0ab680-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180518.000735.5000ad07-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180517.000412.3e525fac-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180516.135310.219d7f44-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180513.095158.356eb51f-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180512.001137.6067dd7c-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180510.171821.2e39e72e-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180510.161028.98908cdf-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180510.000911.70337c0c-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180508.152058.f16e0ce5-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180507.213131.1be0644e-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180507.000253.e27ce7d0-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180506.001005.c7ca86ed-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180503.054500.3ae3004e-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180501.105713.f1d95571-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180501.095430.22cd1d91-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180501.042358.eaee4103-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180424.095041.ee51234b-1
- Update to latest snapshot.

* Mon Apr 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180409.000457.2a2f5b71-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180408.100032.02858026-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180404.000708.9b4032eb-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180402.105716.dfd0bffc-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180326.000856.badcac9a-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180324.174630.768b7ffc-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180313.025809.878b4dcd-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180312.154247.8eedd3f5-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180311.222526.b77f0493-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180311.094958.a55c45de-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180310.162106.c692d41b-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180310.000416.fd19551e-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180309.082724.802494b9-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180308.193148.37142d4c-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180308.180433.b314ac35-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180308.151649.c2a1a877-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180305.115050.a207098e-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180228.105809.51f68389-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180226.201759.559a1d2d-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180225.121246.4b751a9d-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180225.000927.ee1153eb-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.113435.5f0030c9-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.000412.12612fb3-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180223.184238.00d0a928-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.221857.fc251650-2
- Adapt to cmake -> meson switch.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.221857.fc251650-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.144707.f2506d79-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.074327.6423fa39-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180220.212715.ae2f2225-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180218.110914.ffc3cd35-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180213.201203.eea5ebf6-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180205.001138.de9123ea-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180117.181133.6877ed0b-1
- Update to latest snapshot.

* Wed Jan 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180117.181130.1d19504f-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180114.114129.1c705944-2
- Adapt patch for upstream changes.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180114.114129.1c705944-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170921.170550.974d3f19-2
- Merge .spec file from fedora.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170921.170550.974d3f19-1
- Initial package.



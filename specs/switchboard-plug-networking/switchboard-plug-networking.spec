%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type network
%global plug_name networking

%global plug_rdnn io.elementary.switchboard.network

Name:           switchboard-plug-networking
Summary:        Switchboard Networking plug
Version:        2.2.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite) >= 5.2.3
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Requires:       NetworkManager%{?_isa}

Supplements:    (switchboard%{?_isa} and NetworkManager%{?_isa})


%description
A switchboard plug for configuring available networks.


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
* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191220.160932.715878c2-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191219.150716.6e31578a-1
- Update to latest snapshot.

* Sat Dec 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191214.150711.11842e64-1
- Update to latest snapshot.

* Wed Dec 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191210.233225.fb2a6c73-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191121.215025.8d3446d7-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191121.201746.ef2f3991-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191121.195533.dae8ba29-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191121.080251.0aa43416-1
- Update to latest snapshot.

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191121.080012.f61c048e-1
- Update to latest snapshot.

* Wed Nov 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191120.191012.9d52c353-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git191115.224543.248835b4-1
- Update to version 2.2.0.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191115.224543.248835b4-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191105.141630.b523d1e1-1
- Update to latest snapshot.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191105.005359.5e4de43f-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191104.220844.ece3277b-1
- Update to latest snapshot.

* Mon Nov 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191104.172526.ea952c2d-1
- Update to latest snapshot.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191101.091603.0a64bd7f-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191030.201335.8b6326ff-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191030.170602.b7f361ba-1
- Update to latest snapshot.

* Wed Oct 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191030.165602.72854b50-1
- Update to latest snapshot.

* Thu Oct 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191017.172357.e276b475-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191009.172335.1e32c181-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191007.152343.ece8daac-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191003.150101.27050cbe-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191002.204856.bd5f264d-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191001.150011.28bc3011-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git191001.103151.dc08d686-1
- Update to latest snapshot.

* Sun Sep 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190929.013619.9b47efef-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190919.182613.2196f8b3-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190919.173221.bc03e102-1
- Update to latest snapshot.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190917.230144.4af2126f-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190906.152251.08ccae4c-1
- Update to latest snapshot.

* Sat Aug 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190831.082232.79ce9db1-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190827.222240.7952a990-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190823.222106.d02cbe61-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190801.104357.b71aff70-1
- Update to latest snapshot.

* Wed Jul 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190731.211643.e06e0bfc-1
- Update to latest snapshot.

* Wed Jul 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190731.085432.3d6553ef-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190717.134708.9972e7b9-1
- Update to latest snapshot.

* Fri Jun 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190628.164720.d8eaecbd-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190626.204534.7699fec1-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190531.045639.2974b0eb-1
- Update to latest snapshot.

* Tue May 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190528.180352.2129a6dc-1
- Update to latest snapshot.

* Fri May 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190524.063040.35e4363b-1
- Update to latest snapshot.

* Sun May 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190519.185140.4a712935-1
- Update to latest snapshot.

* Sat Apr 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190420.113150.d8dac0bf-1
- Update to latest snapshot.

* Fri Apr 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190419.112758.bce715e3-1
- Update to latest snapshot.

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190418.175058.ea6636d1-1
- Update to latest snapshot.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190409.020648.8891f3da-1
- Update to latest snapshot.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190409.005635.2dba1291-1
- Update to latest snapshot.

* Tue Apr 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190408.230718.02324c5b-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190408.224338.d3a4afe5-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190408.215449.e2547e2e-1
- Update to latest snapshot.

* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190313.220142.c2b434fb-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190312.120021.2d0425d7-1
- Update to latest snapshot.

* Mon Mar 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190311.063141.13fe195e-1
- Update to latest snapshot.

* Sat Mar 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190309.093236.dfe5cca1-1
- Update to latest snapshot.

* Fri Mar 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190308.191456.74f489c7-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190307.190914.b1d8da91-1
- Update to latest snapshot.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190307.185242.15c0a023-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190305.022656.facc66d8-1
- Update to latest snapshot.

* Sun Mar 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190302.202235.77af15aa-2
- Bump granite dependency to >= 5.2.3.

* Sat Mar 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190302.202235.77af15aa-1
- Update to latest snapshot.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190222.000530.0f2bc148-1
- Update to latest snapshot.

* Mon Feb 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190204.133549.09f5ed18-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190115.000618.b1565865-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190114.132854.d965bf35-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190114.001007.28594926-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190106.145813.980b9677-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git190102.195248.1807285c-1
- Update to latest snapshot.

* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181224.000706.8b7018c0-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181213.143312.eba464b6-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181212.072404.29f2bbd3-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181211.071158.d148be60-1
- Update to version 2.1.4.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181211.071158.d148be60-2
- Adapt to added appdata file.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181211.071158.d148be60-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181211.065753.dc22097b-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181211.003434.e93a1157-1
- Update to latest snapshot.

* Sun Dec 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181209.132037.a49edc98-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181208.212101.b94eb22c-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181208.204527.336d78bf-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181207.170916.d20c1147-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181207.101016.8b9cb097-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181206.100648.87fc7e59-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181203.163805.1d5af223-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181203.122810.f1da14bf-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181203.080443.f5ccb04c-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181203.025451.d4d8aa20-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181202.201342.a561cd7c-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181202.095137.b1943963-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181202.082722.1e693e30-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181202.064249.1e5adacb-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181130.013215.03d353c1-1
- Update to latest snapshot.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181129.120655.f69f18de-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181124.130847.15f83410-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181120.084246.0c7f4656-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181116.084027.22587bf1-1
- Update to latest snapshot.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181114.040905.c4edfb41-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181108.084418.f26f4a54-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181107.141018.a1e62d93-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181107.015141.a7db7c12-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181106.221617.9a6eb214-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181106.213753.fc0460aa-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181104.020926.8c5f2977-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181102.100612.334b0958-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181102.100612.334b0958-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181028.161556.f2257eab-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181025.120335.df433c14-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181025.081811.3e837fcd-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181024.090638.289a7544-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181021.133707.87571cd0-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181021.113809.01c305c2-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git181021.093159.a583ea3d-1
- Update to version 2.1.3.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181021.093159.a583ea3d-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181020.082814.2ad40800-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181020.030129.d9347065-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181018.100758.22b8b2a2-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181018.001054.11c725d6-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181017.193352.044193fc-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181017.185013.96cb08b1-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181017.130606.b14e9a92-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181017.105048.3d577e29-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181017.093551.f141c18f-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181017.080855.5bb6bcdd-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181017.074057.e9cc1587-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181017.024559.55405ce9-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181016.001039.c4237f5e-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181016.000034.fd676ca3-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181015.000635.8e5749ab-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181014.001046.9f9808ad-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181013.000918.d4a96170-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181009.173947.fe29627f-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181009.000140.7238bdf5-1
- Update to latest snapshot.

* Sat Oct 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git181006.034305.e91281f7-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180929.000942.eface277-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180926.122226.4baf8cec-1
- Update to latest snapshot.

* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180920.000451.ce1e89f3-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180919.020821.2893aaff-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180919.000926.dc4e1654-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180918.100906.c327bcdc-1
- Update to latest snapshot.

* Thu Sep 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180913.000225.425ba883-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180905.231511.5e98661b-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180830.000751.b23f2d79-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180829.163340.890f47b8-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180819.000941.20884ba9-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180813.000350.2d1614bf-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180813.000350.2d1614bf-1
- Update to latest snapshot.

* Sat Aug 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180804.134912.e50f3de3-1
- Update to latest snapshot.

* Mon Jul 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180723.000418.e7a4b903-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180721.122152.b86357d9-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180721.073309.2220127a-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180720.143328.2935a19b-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180718.000628.220150b7-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180717.202351.84b68b15-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180717.154208.de322dad-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180717.110455.60f4f656-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180717.063619.cacf8853-1
- Update to latest snapshot.

* Sat Jul 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180714.015208.773aecde-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180713.000406.e93c2a25-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180707.184905.7434089f-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180704.210724.da339f8d-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180627.160842.0ae515dd-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180615.001112.9c17de48-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180614.000915.a9daf347-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180613.174315.f3bbd1b5-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180613.000750.5eb1dd9b-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180608.162647.33c08563-1
- Update to version 0.1.2.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180608.162647.33c08563-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180603.070643.2979895a-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180602.000624.3c7405de-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180601.000812.27ce4efa-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180531.000309.bd3a7f68-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180530.123946.10841a56-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180530.035237.8bac34f0-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180529.001243.3bb1accd-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180528.071912.e01890ce-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180527.000550.28a5c1ef-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180525.164147.99c39b91-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180524.001038.d9c46139-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180514.000238.ebdabac6-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180513.101313.4b2cc42a-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180512.001159.489d3a22-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180511.032229.5e413d5a-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180510.172051.0dac2496-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180510.120312.51fd5d12-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180510.000923.7e85764b-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180507.000312.dc35b4fc-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180506.001018.d26fdb01-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180503.080152.bf4ae949-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180429.115218.22a97210-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180426.000345.4af6030e-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180424.211516.9652e34e-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180421.001132.77ff7438-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180415.001024.9420c053-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180414.124353.829565bc-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180406.080741.c9f9e0e8-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180405.143429.15045faa-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180404.000717.85120596-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180403.142806.f598e709-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180328.195243.dda97281-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180328.090437.b9ba8a04-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180327.162412.93e3de4d-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180326.174426.9ef566f4-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180326.072945.ea9b9199-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180325.211748.41948d16-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180325.000928.d4de991c-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180320.001157.c39f47b7-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180314.000226.5d059510-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180312.001005.a2e23c60-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180309.000611.ee5007e2-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180308.000909.b8ec6509-2
- Adapt to dependency changes.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180308.000909.b8ec6509-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180227.000415.2ee05bce-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180226.094153.a2c850f6-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180223.125025.3810943b-2
- Adapt to cmake -> meson switch.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180223.125025.3810943b-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180220.225803.00b630b3-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180220.215028.13ba7908-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180218.200533.c52183a1-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180217.101014.5af48c8f-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180211.000853.f2dfaec0-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180209.000246.d68ac879-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180208.220332.2e0f5d0b-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180205.001150.3d1bce13-1
- Update to latest snapshot.

* Thu Feb 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180201.000924.d343b692-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180129.000243.f2ef1946-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180118.000240.5265ea66-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180105.085339.b1094cb4-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180103.010504.5910cd45-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180103.010504.5910cd45-1
- Update to latest snapshot.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171229.230757.cfa74410-1
- Update to latest snapshot.

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171227.173136.e1bb1bc5-1
- Update to latest snapshot.

* Tue Dec 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171226.174250.53810d6a-1
- Update to latest snapshot.

* Sun Dec 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171222.220023.5a5867be-2
- Adapt to upstream dependency changes.

* Sun Dec 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171222.220023.5a5867be-1
- Update to latest snapshot.

* Wed Dec 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171220.181623.c8ca88b0-1
- Update to latest snapshot.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171118.235353.8e23d341-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171117.184103.adae98e2-1
- Update to latest snapshot.

* Thu Nov 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171102.164146.382f335a-1
- Update to latest snapshot.

* Fri Oct 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171027.154651.d36d298f-1
- Update to latest snapshot.

* Thu Oct 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171026.172718.a8b97c55-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171025.143830.b20434d6-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171024.181951.59b079bd-1
- Update to latest snapshot.

* Tue Oct 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171024.000054.03d3091f-1
- Update to latest snapshot.

* Mon Oct 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171023.183001.c7e0308a-1
- Update to latest snapshot.

* Mon Oct 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171002.185929.b49a6155-1
- Update to latest snapshot.

* Mon Oct 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171002.143240.914b8935-1
- Update to latest snapshot.

* Fri Sep 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170922.000642.b649a59f-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170916.000221.e500be8d-1
- Update to latest snapshot.

* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170915.095826.284e1174-1
- Update to version 0.1.1.

* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev504-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev503-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev501-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev495-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev491-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev490-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev384-1
- Update to latest snapshot.

* Sat May 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev383-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev382-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev381-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev380-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev379-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev378-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev377-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev376-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev375-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev374-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev373-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev372-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev371-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev370-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev369-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev368-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev367-1
- Update to latest snapshot.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev366-1
- Update to version 0.1.0.3.

* Tue Jan 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev365-1
- Update to version 0.1.0.3.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev364-1
- Update to version 0.1.0.3.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev363-1
- Update to version 0.1.0.3.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev362-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev361-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev360-1
- Update to latest snapshot.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev359-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev358-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev356-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev355-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev354-1
- Update to latest snapshot.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev353-1
- Update to latest snapshot.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev352-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev351-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev350-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev349-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev348-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev347-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev346-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev345-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev344-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev343-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev342-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev341-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev340-1
- Update to version 0.1.0.3.



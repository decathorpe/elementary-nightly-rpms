%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_name power
%global plug_type hardware

%global plug_rdnn io.elementary.switchboard.power

Name:           switchboard-plug-%{plug_name}
Summary:        Switchboard Power Plug
Version:        2.4.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.30.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       dbus
Requires:       elementary-dpms-helper


%description
Control system power consumption with this Switchboard preference plug.


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

%{_libexecdir}/io.elementary.logind.helper

%{_datadir}/dbus-1/system.d/io.elementary.logind.helper.conf
%{_datadir}/dbus-1/system-services/io.elementary.logind.helper.service
%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml
%{_datadir}/polkit-1/actions/io.elementary.switchboard.power.policy


%changelog
* Sun Mar 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git200301.140916.e2108bfd-1
- Update to latest snapshot.

* Sat Feb 22 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git200222.140905.8818c78f-1
- Update to latest snapshot.

* Fri Feb 07 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git200206.230825.e79a53db-1
- Update to latest snapshot.

* Sun Jan 12 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git200112.200747.c7bdef16-1
- Update to latest snapshot.

* Wed Jan 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git200101.160729.72a64406-1
- Update to latest snapshot.

* Tue Dec 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191224.220721.446c2f06-1
- Update to latest snapshot.

* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191220.160925.dabcdd28-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191219.130720.cc5e35c5-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191218.211247.f4f939c0-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191218.210038.d5f75822-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191217.183712.a8aed964-1
- Update to latest snapshot.

* Thu Nov 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191128.162535.2534439c-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191125.092518.b437371b-1
- Update to latest snapshot.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191122.032529.75df05c0-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191117.202506.d10dacea-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0+git191116.172457.0a3d0f8d-1
- Update to version 2.4.0.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191116.172457.0a3d0f8d-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191115.224803.557432f4-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191111.122459.6e8b4288-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191109.152456.b273e3ff-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191107.164332.524d46fc-1
- Update to latest snapshot.

* Thu Nov 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191106.234046.d9903c3a-1
- Update to latest snapshot.

* Wed Oct 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191009.172338.261151f7-1
- Update to latest snapshot.

* Mon Oct 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191007.152413.32ada449-1
- Update to latest snapshot.

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191005.092327.54f7b2fb-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191003.151306.4bd1f477-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191003.005240.34ffb7b8-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191002.205604.13ccc1c3-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191001.211608.af2921c1-2
- Adapt to upstream file changes.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191001.211608.af2921c1-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191001.203355.680ffff3-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git191001.155440.fb3dc062-1
- Update to latest snapshot.

* Fri Sep 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190920.164122.39393742-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190919.182009.9a579c49-1
- Update to latest snapshot.

* Mon Sep 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190916.162303.bf19dcf2-1
- Update to latest snapshot.

* Sat Sep 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190907.202247.a6669a05-1
- Update to latest snapshot.

* Fri Aug 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190830.212247.61769cde-1
- Update to latest snapshot.

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190829.152234.c7e8eb18-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190827.222320.938bfb79-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190731.234224.df238c43-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190717.184803.221d4eaf-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190717.142041.7470d3f1-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190626.205607.8353bfaa-1
- Update to latest snapshot.

* Sat Jun 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190608.003936.0475cf39-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190531.044907.14fc12f4-1
- Update to latest snapshot.

* Sun May 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190519.141500.93d57ec9-1
- Update to latest snapshot.

* Wed May 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190515.171451.b2ace842-1
- Update to latest snapshot.

* Fri May 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190510.093606.9a203574-2
- Adapt to new appdata file.

* Fri May 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190510.093606.9a203574-1
- Update to latest snapshot.

* Tue May 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190507.215717.9d300e54-1
- Update to latest snapshot.

* Tue Apr 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190416.223147.eb16fe99-1
- Update to latest snapshot.

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190414.185341.13c3975d-1
- Update to latest snapshot.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190406.225223.809e365f-1
- Update to latest snapshot.

* Thu Mar 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190321.105326.bbe63e84-1
- Update to latest snapshot.

* Sat Mar 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190309.133106.1d905789-1
- Update to latest snapshot.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190305.032652.1b3dab83-1
- Update to latest snapshot.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5+git190129.071514.06a7bebe-1
- Update to version 2.3.5.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190129.071514.06a7bebe-1
- Update to latest snapshot.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190125.000149.80aa7971-1
- Update to latest snapshot.

* Tue Jan 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190115.000623.376e0c5c-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190114.001017.f438bc08-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190107.000342.0a27eeb2-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git190106.221935.cc8dc4d2-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181219.000817.1eb43d1a-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181217.010353.1d6c4a57-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181211.151043.a241faa0-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181202.064801.050f7db4-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181124.130842.e37583b4-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181120.095740.6795dc28-1
- Update to latest snapshot.

* Sat Nov 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181109.230705.a12cf4e2-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181107.015101.fd9fbb3c-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181106.214539.641431fc-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181105.224738.b4c8e646-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181101.000339.f2d8db33-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181101.000339.f2d8db33-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181029.024650.ba4bf8dd-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181025.220719.e747a58a-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181021.120635.caec04e0-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181018.001103.d4433d38-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181016.000903.c0110441-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181012.000533.09820253-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4+git181010.152327.ab7fa57e-1
- Update to version 2.3.4.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181010.152327.ab7fa57e-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git181009.154602.9e067706-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180928.000719.91f9bf48-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180927.001024.7ea9438f-1
- Update to latest snapshot.

* Sun Sep 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180915.234303.e89b64cb-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180910.173653.da754e61-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180908.162537.bef6a913-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180830.000803.b0f676f8-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180829.163517.366991c1-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180809.215447.beb9a285-2
- Occasional mass rebuild.

* Fri Aug 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180809.215447.beb9a285-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180726.231543.6c32a27f-2
- Remove dpms-helper-removing patch.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180726.231543.6c32a27f-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180726.213750.3e587481-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180726.123758.36622cc5-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180715.001018.daa3b728-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180713.000414.3c5f681e-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180711.000901.d221f5f4-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180709.001034.3933d243-1
- Update to latest snapshot.

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180708.062520.aa85c421-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180703.000656.c6501fe8-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180614.000924.bfa8bbaf-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180612.073456.542ede1a-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180610.001219.be46803d-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180608.133519.253c0f6a-1
- Update to version 0.3.3.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180608.133519.253c0f6a-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180606.000928.b566fbf0-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180603.070802.b31d1f7a-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180602.000638.824b7ead-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180530.162225.d990a1d8-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180530.000424.61e85263-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180528.085615.29417ce0-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180527.000558.ec732a46-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180516.133121.cb90a7ea-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180512.001208.027d4522-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180511.032558.1b0bff88-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180503.000628.cf7adec7-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180501.123706.f1f61cf7-2
- Rebase patch to remove dpms-helper.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180501.123706.f1f61cf7-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180501.105915.df5d96a5-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180429.133102.7b5de95b-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180426.000350.cf80668d-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180424.202030.b8059505-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180415.001034.38e86602-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180413.225010.517c1db6-2
- Rebase patch to latest upstream.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180413.225010.517c1db6-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180402.000514.20ca1e09-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180326.000911.377e9769-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180324.175041.84556bb3-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180322.134250.828a81da-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180321.195210.8e8eac93-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180320.145052.a57ecf52-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180320.001202.a09bb76f-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180318.191307.dadec7c6-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180318.174820.3e86a0e9-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180318.120742.9afb7b03-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180318.080522.db93bd2f-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180317.225135.bdf21c79-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180316.035820.da6ba109-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180314.000235.789d24e4-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180310.160931.10594eff-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180310.000439.7c200778-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180309.034234.a07b173c-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180308.192903.7297d532-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180308.175429.394cedd9-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180307.001330.692bd157-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180306.000506.1d2bf48d-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180305.114821.c36be5ed-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180301.144925.afc0d321-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180228.105839.c04e1a8b-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180227.141036.9f46893c-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180227.104642.6a5e4d38-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180227.000422.866c375f-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180226.210754.cdb1851d-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180226.205330.c31a1c19-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180224.171403.cea06bc1-2
- Adapt to upstream file changes.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180224.171403.cea06bc1-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180220.230547.17eb9ca6-2
- Adapt to cmake -> meson switch.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180220.230547.17eb9ca6-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180220.212218.cc5ba827-1
- Update to latest snapshot.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180214.210831.477a1d37-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180211.000903.c1559f36-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180206.193731.26358d63-1
- Update to latest snapshot.

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180130.001037.ac8a0377-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180129.000247.2dc0af83-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180128.202412.d42024af-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180128.162135.e5d22315-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180128.020222.ced39b8c-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180127.202258.4d6181dd-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180125.102055.8de48329-2
- Adapt patch to upstream changes.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180125.102055.8de48329-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180124.140355.868ba346-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180124.062628.52aeaedf-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.204619.aeab31bf-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.170619.e3a02b71-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.162207.7f5f8eaa-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.155523.9c651f38-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.000558.93fb5a4b-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180122.091505.5327d3fa-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180122.061941.4330562b-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171112.174647.cf8fd1ca-2
- Merge .spec file from elementary-stable.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171112.174647.cf8fd1ca-1
- Update to latest snapshot.

* Sat Oct 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171007.070336.965c050e-1
- Update to latest snapshot.

* Sun Sep 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170924.001034.f80326f4-1
- Update to latest snapshot.

* Sat Sep 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170923.185712.da8d5c6f-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170817.000746.b0739ce5-1
- Update to latest snapshot.

* Sun Aug 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170719.185928.fd6e0bf8-2
- Add patch to remove usage and dependency on e-dpms-helper.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170719.185928.fd6e0bf8-1
- Update to version 0.3.2.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170719.185928.fd6e0bf8-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170715.120953.ef1e981a-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170702.171704.de550755-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170702.110138.955fcc93-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170621.170427.27ca0dbc-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170621.163313.8e244d22-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170619.111204.64d06d11-2
- Adapt to upstream file changes.

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170619.111204.64d06d11-1
- Update to latest snapshot.

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170619.064115.e60f522f-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170617.160328.af784cd4-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170603.180424.f7bb17b3-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170603.175305.4b646925-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170602.180706.63ecc031-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170602.173926.4a22ba34-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170601.211203.dd167ce2-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170601.192843.f127a598-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170601.012014.97d7184c-1
- Update to latest snapshot.

* Wed May 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170530.213003.d991eb14-1
- Update to latest snapshot.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170521.211443.06578eb5-1
- Update to latest snapshot.

* Fri May 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170511.073106.5ce5bdfe-1
- Update to version 0.3.1.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev423-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev422-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev421-1
- Update to latest snapshot.

* Wed Apr 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev417-1
- Update to latest snapshot.

* Fri Apr 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev416-1
- Update to latest snapshot.

* Mon Apr 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev415-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev414-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev413-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev412-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev411-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev408-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev407-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev406-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev405-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev404-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev403-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev402-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev401-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev400-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev399-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev398-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev397-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev396-1
- Update to latest snapshot.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev395-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev394-1
- Update to version 0.3.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev393-1
- Update to version 0.3.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev392-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev391-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev390-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev389-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev388-1
- Update to latest snapshot.

* Sun Dec 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev387-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev386-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev385-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev384-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev383-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev382-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev381-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev380-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev379-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev378-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev377-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev376-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev375-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev374-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev373-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev372-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev371-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev370-1
- Update to version 0.3.



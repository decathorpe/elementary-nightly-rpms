%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type system
%global plug_name sound

%global plug_rdnn io.elementary.switchboard.sound

Name:           switchboard-plug-sound
Summary:        Switchboard Sound Plug
Version:        2.2.2+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
Switchboard Sound Plug.


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
* Fri Dec 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191220.160950.c6ffdc75-1
- Update to latest snapshot.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191219.130726.dfa9fea8-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191218.193231.6f3b2d74-1
- Update to latest snapshot.

* Wed Dec 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191218.190024.6c9aad0f-1
- Update to latest snapshot.

* Tue Dec 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191217.170900.edf52cce-1
- Update to latest snapshot.

* Sat Nov 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191130.082522.cd611a05-1
- Update to latest snapshot.

* Thu Nov 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191128.162550.d071ae26-1
- Update to latest snapshot.

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191125.102516.cc0b53ca-1
- Update to latest snapshot.

* Sat Nov 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191123.072516.621b1faa-1
- Update to latest snapshot.

* Sun Nov 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191117.212503.d72bafe0-1
- Update to latest snapshot.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2+git191116.172506.53249149-1
- Update to version 2.2.2.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191116.172506.53249149-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191115.230123.49aeb8cd-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191111.122509.f2f7e5b0-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191109.152506.2dddaad1-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191106.221432.38e6069d-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191106.174517.55f4cbe8-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191106.164239.3a990367-1
- Update to latest snapshot.

* Fri Oct 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191025.132403.1e163b31-1
- Update to latest snapshot.

* Thu Oct 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191017.172435.1aa128f5-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191003.160938.c5adfdc2-1
- Update to latest snapshot.

* Thu Oct 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191003.151319.0b1c13b4-1
- Update to latest snapshot.

* Wed Oct 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191001.014246.e0676876-1
- Update to latest snapshot.

* Tue Oct 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git191001.014145.862919f2-1
- Update to latest snapshot.

* Thu Sep 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190919.183207.60935c55-1
- Update to latest snapshot.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190909.152532.137280d1-1
- Update to latest snapshot.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190906.152311.6236a089-1
- Update to latest snapshot.

* Tue Aug 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190827.012232.ca89fd82-1
- Update to latest snapshot.

* Fri Aug 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190823.221122.6a78fcf7-1
- Update to latest snapshot.

* Thu Aug 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190731.233731.fbb961b6-1
- Update to latest snapshot.

* Wed Jul 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190717.143534.26afeba2-1
- Update to latest snapshot.

* Wed Jun 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190626.205816.c2b288eb-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190531.044720.6cb4141b-1
- Update to latest snapshot.

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190517.011530.c895ea25-1
- Update to latest snapshot.

* Fri May 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190510.112943.b128ad13-2
- Adapt to new appdata file.

* Fri May 10 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190510.112943.b128ad13-1
- Update to latest snapshot.

* Mon Apr 15 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190415.222601.f6476b12-1
- Update to latest snapshot.

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git190408.183647.957cf3ed-1
- Update to version 2.2.1.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190408.183647.957cf3ed-1
- Update to latest snapshot.

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190408.172155.f40e40f6-1
- Update to latest snapshot.

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git190330.175210.bdd3bb8e-1
- Update to version 2.2.0.

* Thu Mar 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190328.101152.fb9c170c-1
- Update to latest snapshot.

* Sat Mar 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190309.182705.82456a03-1
- Update to latest snapshot.

* Wed Mar 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190306.182709.f69ee95c-1
- Update to latest snapshot.

* Thu Feb 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190228.093150.ebf0ad59-1
- Update to latest snapshot.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190114.134439.f247d2db-1
- Update to latest snapshot.

* Tue Jan 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3+git190108.134435.0935f90a-1
- Update to version 2.1.3.

* Tue Jan 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190108.134435.0935f90a-1
- Update to latest snapshot.

* Sun Jan 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190106.223617.4a5b443e-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190103.190303.8b8ce064-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190103.000446.ef888855-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git190102.215603.b48c936f-1
- Update to latest snapshot.

* Sat Dec 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181229.000122.ce47b7e4-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181213.142137.40f16ce9-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181211.151053.ec0f1ebb-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181211.071055.1da23ced-1
- Update to latest snapshot.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181207.031821.dd036592-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181202.065131.70bc83c1-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181124.121033.f2054c44-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181122.215839.0eee6eee-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181122.200403.4c5a55bd-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181122.083016.bec1a73a-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181121.130552.43519ee9-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181121.100930.7095c15e-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181119.171835.5669b55e-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181119.163745.6dc0752e-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181119.111530.320dc0d0-1
- Update to latest snapshot.

* Sun Nov 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181118.192738.a039934c-1
- Update to latest snapshot.

* Sun Nov 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181118.153836.eca9d57d-1
- Update to latest snapshot.

* Sun Nov 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181118.011015.76b189cc-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181117.173825.6c847fd2-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181117.120643.05c3c650-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181117.103256.a62b6b85-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181117.093000.91dbf3e1-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181117.071548.b8cea08c-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181116.203140.fab4c4ae-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181116.082854.5d759d2a-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181116.021423.6206f98a-1
- Update to latest snapshot.

* Thu Nov 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181108.142229.16a7b5e2-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181107.015223.4b79d02c-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181106.212636.5f998353-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181105.235434.3939737e-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181028.161455.82eabf9e-2
- Occasional mass rebuild.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181028.161455.82eabf9e-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181025.081115.12b646a2-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181022.184849.09e7bb3c-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181021.110153.743629ca-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.2+git181020.030507.b211e416-1
- Update to version 2.1.2.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181020.030507.b211e416-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181017.000748.3cc0a632-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.195311.08fc9fd0-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.180428.502d7942-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.164202.fa0380b8-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.134418.d0629773-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.124230.a91b1935-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.101719.1946e4c8-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.092143.7b138aa7-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181016.005902.099c8391-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181015.214855.72dcda63-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181015.205624.2fc8af2b-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181015.091941.7782fc80-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181014.000401.c8eeec39-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181009.154848.ca731dec-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181004.063020.a73ea42f-1
- Update to latest snapshot.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git181001.000859.040a19c4-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180927.045318.732ab109-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180926.172716.a1727e24-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180926.143035.5dded93a-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180926.122137.0dc8b778-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180906.043952.2cac046c-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180901.000919.97eb934f-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180831.131020.c0461580-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180829.162055.06766a65-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180829.155230.8a7b1da5-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180829.000401.a5bc5194-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180827.095359.aea90dd0-1
- Update to version 0.1.1.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180827.095359.aea90dd0-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180818.142102.4007d53c-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180813.000410.526dda2c-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180813.000410.526dda2c-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180803.134847.df25aefc-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180724.030908.fccebce3-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180722.120536.fa991cb1-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180722.000404.2bb84cd6-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180721.123205.8ba69242-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180721.000754.cc4314a2-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180718.000648.920d1421-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180716.203633.c10fada9-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180713.181434.ea9546d8-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180713.173146.56d05340-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180713.014015.9e29fc96-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180712.195533.901b506d-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180709.201604.91862079-1
- Update to latest snapshot.

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180708.000922.0d293216-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180702.160226.a38c4fd2-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180608.160923.c7ba44ec-1
- Update to version 0.1.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180608.160923.c7ba44ec-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180602.195251.ac81eda0-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180531.122228.67969cbc-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180531.000347.fdce91a8-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180527.131815.3f67d041-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180521.000947.0958572d-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180517.000443.be5275f9-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180512.001228.5d7c648e-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180511.025616.ee1aa720-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180510.083614.97a6b4f6-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180508.132519.aba33e67-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180505.221011.bffd5fa6-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180503.143223.9e814dcb-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180410.173908.69bf56f7-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180331.212842.427a8c69-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180325.000948.19ada98d-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180308.162515.28fbfeae-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180224.000454.49f6ade1-2
- Adapt to cmake -> meson switch.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180224.000454.49f6ade1-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180220.231707.86c178aa-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180211.000924.a1810189-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180209.001031.69ec18ae-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180205.001218.fb9e079b-1
- Update to latest snapshot.

* Sat Feb 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180203.114909.4016eb2f-1
- Update to latest snapshot.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180202.201104.d9a903ec-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180104.001457.650fc7d0-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git171104.070953.c277c501-2
- Clean up .spec file.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171104.070953.c277c501-1
- Update to latest snapshot.

* Sat Oct 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171007.070521.3030e160-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170818.000142.91c5935f-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170715.154411.c206bbcd-1
- Update to latest snapshot.

* Wed Jul 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170702.102802.983900fc-1
- Initial package.



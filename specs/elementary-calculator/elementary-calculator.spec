%global srcname calculator
%global appname io.elementary.calculator

Name:           elementary-calculator
Summary:        Calculator app designed for elementary
Version:        1.5.2+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  /usr/bin/appstream-util

BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6

Provides:       pantheon-calculator = %{version}-%{release}
Obsoletes:      pantheon-calculator < 0.1.4


%description
A simple calculator for everyday use.

It supports basic and some scientific calculations, including trigonometry
functions (sin, cos, and tan).


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191115.212442.849854b3-1
- Update to latest snapshot.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191115.185338.ee6933d6-1
- Update to latest snapshot.

* Thu Nov 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191114.211113.107c9774-1
- Update to latest snapshot.

* Mon Nov 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191111.122447.187b8688-1
- Update to latest snapshot.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191109.112437.2dde5daa-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191106.192443.ad3e44a8-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191106.174145.8a77d05e-1
- Update to latest snapshot.

* Wed Nov 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191106.164217.c04a298c-1
- Update to latest snapshot.

* Sun Oct 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191027.192422.ce726f47-1
- Update to latest snapshot.

* Thu Oct 24 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191024.212409.ed38d052-1
- Update to latest snapshot.

* Mon Oct 21 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git191021.142340.75a7c4f7-1
- Update to latest snapshot.

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git190531.045802.08db2c7c-1
- Update to latest snapshot.

* Thu May 30 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git190522.070304.b5ff9904-1
- Update to latest snapshot.

* Thu Apr 25 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git190424.232648.ad9ff328-1
- Update to latest snapshot.

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git190312.142643.7f6eb162-1
- Update to latest snapshot.

* Mon Mar 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git190311.142224.09c758e2-1
- Update to latest snapshot.

* Fri Mar 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2+git190308.103829.46d8760d-1
- Update to version 1.5.2.

* Fri Mar 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190308.103829.46d8760d-1
- Update to latest snapshot.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190212.000626.7da5c8f6-1
- Update to latest snapshot.

* Sun Feb 10 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190210.215804.9e9a18a8-1
- Update to latest snapshot.

* Wed Jan 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190116.000314.6a8d7cc5-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190109.114606.8d5acbc6-1
- Update to latest snapshot.

* Wed Jan 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190109.000155.8c22e714-1
- Update to latest snapshot.

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190107.000218.b1c7c2a6-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190103.181742.56234009-1
- Update to latest snapshot.

* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190103.171515.380ae910-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git190102.180210.f46a10af-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181202.061630.816480ed-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181202.053330.c0f4f623-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181202.004435.fe575556-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181122.000157.4b11fbff-1
- Update to latest snapshot.

* Sat Nov 03 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181103.215510.ae77af8f-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181030.000422.566b43df-2
- Occasional mass rebuild.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181030.000422.566b43df-1
- Update to latest snapshot.

* Sat Oct 27 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181027.003024.c2fc4a07-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181025.070538.883c82f1-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181021.105514.9bf4b6d8-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181021.040056.25ce9faf-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181021.033447.6a3490a3-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181020.001012.ca32ad91-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181019.164732.328140c1-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181018.102356.aacab20b-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181017.191832.c66df6dc-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1+git181016.072225.7012636a-1
- Update to version 1.5.1.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git181016.072225.7012636a-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git181015.201611.f2748220-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git181015.195129.4546a284-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git181012.000430.ef97fc60-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git181011.131616.1d51fce8-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git181007.023539.2f4f9fdb-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git181005.000753.3a017633-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git181002.220528.4bf1cfc8-1
- Update to version 0.1.5.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181002.220528.4bf1cfc8-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180930.204039.d47b1e5a-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180930.000919.20d323f6-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180929.172014.01c8eaaf-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180924.000447.fa02a891-1
- Update to latest snapshot.

* Sun Sep 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180923.000609.a9f8ff79-1
- Update to latest snapshot.

* Sat Sep 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180922.012728.9676ab9f-1
- Update to latest snapshot.

* Fri Sep 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180914.154313.56a98d43-1
- Update to latest snapshot.

* Fri Sep 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180914.054338.960b7e53-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180906.022252.76753c7b-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180830.152338.be8b3ca7-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180830.000638.eaa3908f-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180829.033330.e8bbf598-1
- Update to latest snapshot.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180828.121828.9da33140-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180824.000128.b881fa4a-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180823.184229.f63b6ba8-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180821.000148.412f7604-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180819.135437.73682600-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180819.042613.17ad4042-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180818.091624.f1a00613-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180812.110332.382cc2a4-2
- Occasional mass rebuild.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180812.110332.382cc2a4-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180808.000132.bbf1521f-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180721.000655.62beb44f-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180720.110355.b37fb44b-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180720.000629.1fae89c1-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180718.092942.6409cdd5-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180717.000246.7ceb132c-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180715.192102.60323bb6-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180712.213316.708ca4e4-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180712.170755.9edd90a1-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180711.000827.b8555228-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180709.202247.3685fb60-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180709.001007.14780998-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180704.181156.95054cd7-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180703.185405.35e42695-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180615.000954.778b1bd4-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180614.000801.108c766f-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180613.105821.7338e595-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180613.000631.f65889cd-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180612.072223.ccf0a011-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180609.000526.5017c402-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180607.205333.5440150c-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180607.173641.59eca193-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180607.164249.4da56757-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180607.000838.88a5da01-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180606.133738.7209bdf9-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180606.000744.3d3fe4f4-1
- Update to version 0.1.4.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180606.000744.3d3fe4f4-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180605.172641.39826e18-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180605.092859.90248a32-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180604.000816.9c1179db-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180602.000413.dd2d9cfe-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180601.000638.e01c28b1-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180531.154130.3252e5cb-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180529.235019.b812cc2d-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180527.085326.e456d719-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180522.000819.9725c684-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180514.154020.8a3431b9-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180513.163946.db333c6e-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180508.203340.5a8c2945-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180507.000209.dab2b320-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180416.000850.839769e8-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180326.000821.33ddff8e-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180320.001100.1b1508e5-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180318.010025.9cc6da68-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180308.183644.a7c0a2a3-2
- Adapt to upstream file changes.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180308.183644.a7c0a2a3-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180306.214634.17b3591b-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180306.202642.882b2b23-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180306.190254.0e97a7fe-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180225.145705.6cca8d6e-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180205.001047.f528b042-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180128.000728.37803bca-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180104.232914.aff8bd5e-2
- Clean up .spec file.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180104.232914.aff8bd5e-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171116.231410.81be3d74-1
- Initial package.


